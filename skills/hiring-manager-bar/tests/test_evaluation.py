"""Deterministic checks for evaluation integrity; behavioral grading uses fresh agents."""
import argparse
from contextlib import redirect_stdout
import importlib.util
from html.parser import HTMLParser
import io
import json
from pathlib import Path
import re
import tempfile
import unittest
from urllib.parse import urlparse
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


def module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / (name + ".py"))
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


evaluation = module("evaluate")
podcast = module("dive_club")


class EvaluationIntegrity(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.skill = self.root / "source"
        self.skill.mkdir()
        (self.skill / "SKILL.md").write_text("Review the supplied material honestly.")
        self.suite = self.root / "suite.json"
        evaluation.write(self.suite, {
            "cases": [{"id": "ownership", "request": "Review attribution.",
                       "supplied_evidence": "The team shipped a flow.",
                       "expected_behavior": ["PRIVATE_EXPECTATION_MARKER"]}],
            "shared_criteria": [{"id": "evidence", "criterion": "Do not claim an inspection."}],
        })
        self.run = self.root / "run"
        evaluation.prepare(self.skill / "SKILL.md", self.suite, self.run)

    def grade(self, status="pass", quote="Team credit is clear."):
        directory = self.run / "cases/ownership"
        evaluation.write(directory / "response.json", {"response": "Team credit is clear."})
        evaluation.write(directory / "grade.json", {"checks": [
            {"id": "case-1", "status": status, "reason": "Attribution is explicit.", "evidence_quote": quote},
            {"id": "evidence", "status": "pass", "reason": "No inspection claimed.", "evidence_quote": ""},
        ]})
        return directory

    def result(self):
        with redirect_stdout(io.StringIO()):
            code = evaluation.report(self.run)
        return code, evaluation.read(self.run / "summary.json")

    def test_reviewer_inputs_exclude_expectations(self):
        directory = self.run / "cases/ownership"
        self.assertEqual(set(evaluation.read(directory / "input.json")), {"id", "request", "supplied_evidence"})
        self.assertNotIn("PRIVATE_EXPECTATION_MARKER", (directory / "prompt.txt").read_text())
        self.assertFalse((directory / "expected.json").exists())
        self.assertIn("PRIVATE_EXPECTATION_MARKER", (self.run / "expected.json").read_text())

    def test_input_changes_invalidate_a_run(self):
        (self.run / "skill/SKILL.md").write_text("Changed after evaluation.")
        with self.assertRaisesRegex(ValueError, "Frozen evaluation input changed"):
            evaluation.verify_snapshot(self.run)

    def test_missing_grades_are_incomplete(self):
        code, summary = self.result()
        self.assertEqual(code, 2)
        self.assertEqual(summary["case_counts"]["incomplete"], 1)

    def test_missing_criterion_does_not_pass(self):
        directory = self.grade()
        grade = evaluation.read(directory / "grade.json")
        grade["checks"].pop()
        evaluation.write(directory / "grade.json", grade)
        self.assertEqual(self.result()[0], 2)

    def test_invented_grader_evidence_does_not_pass(self):
        self.grade(quote="The reviewer never said this.")
        self.assertEqual(self.result()[0], 2)

    def test_empty_review_does_not_pass(self):
        directory = self.grade(quote="")
        evaluation.write(directory / "response.json", {"response": ""})
        self.assertEqual(self.result()[0], 2)

    def test_failure_is_retained(self):
        self.grade(status="fail")
        code, summary = self.result()
        self.assertEqual(code, 1)
        self.assertEqual(summary["overall"], "fail")

    def test_uncertainty_is_not_a_pass(self):
        self.grade(status="uncertain")
        self.assertEqual(self.result()[0], 2)

    def test_complete_evidence_backed_grades_can_pass(self):
        self.grade()
        self.assertEqual(self.result()[0], 0)

    def test_existing_runs_are_not_overwritten(self):
        with self.assertRaises(FileExistsError):
            evaluation.prepare(self.skill / "SKILL.md", self.suite, self.run)

    def test_completed_model_calls_are_not_reissued_on_resume(self):
        self.grade()
        with patch.object(evaluation, "codex_call") as call:
            evaluation.execute(self.run, "unused", "all", 1, jobs=3)
        call.assert_not_called()

    def test_ungraded_review_is_preserved_when_resuming(self):
        directory = self.grade()
        grade = evaluation.read(directory / "grade.json")
        (directory / "grade.json").unlink()
        response = (directory / "response.json").read_bytes()
        with patch.object(evaluation, "codex_call", return_value=grade) as call:
            with redirect_stdout(io.StringIO()):
                evaluation.execute(self.run, "unused", "all", 1, jobs=3)
        self.assertEqual(call.call_count, 1)
        self.assertEqual(call.call_args.args[3].name, "grade.json")
        self.assertEqual(response, (directory / "response.json").read_bytes())

    def test_artifacts_are_frozen_without_revealing_expectations(self):
        fixture = self.root / "fixture"
        fixture.mkdir()
        (fixture / "project.html").write_text("<a href='credits.html'>Credits</a>")
        (fixture / "credits.html").write_text("The candidate owned interaction design.")
        suite = evaluation.read(self.suite)
        suite["cases"][0]["fixture"] = "fixture"
        evaluation.write(self.suite, suite)
        run = self.root / "with-artifacts"
        evaluation.prepare(self.skill / "SKILL.md", self.suite, run)
        directory = run / "cases/ownership"
        artifacts = Path(evaluation.read(directory / "input.json")["artifact_directory"])
        self.assertTrue((artifacts / "credits.html").is_file())
        self.assertFalse(any("PRIVATE_EXPECTATION_MARKER" in p.read_text() for p in directory.rglob("*") if p.is_file()))
        (artifacts / "credits.html").write_text("Altered credit after the review.")
        with self.assertRaisesRegex(ValueError, "Frozen evaluation input changed"):
            evaluation.verify_snapshot(run)


class PodcastResearchIntegrity(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.episode = {"id": "42", "guid": "stable-guid", "title": "A portfolio conversation",
                        "audio_url": "https://example.com/episode.mp3", "url": "https://example.com/42",
                        "metadata_topic_match": True}
        podcast.save_json(self.root / "catalog.json", {"episodes": [self.episode]})

    def args(self, **extra):
        return argparse.Namespace(workdir=self.root, ids=["42"], topic_matches=False, limit=1, keep_audio=False, **extra)

    def transcript(self, episode=None):
        podcast.save_json(self.root / "transcripts/42.json", {
            "episode": episode or self.episode,
            "segments": [{"start": i * 10, "end": i * 10 + 8,
                          "text": "portfolio" if i in (1, 3, 9) else "Surrounding qualification."}
                         for i in range(12)],
        })

    def test_completed_episode_is_not_redownloaded_or_retranscribed(self):
        self.transcript()
        before = (self.root / "transcripts/42.json").read_bytes()
        with patch.object(podcast, "download") as download, patch.object(podcast.subprocess, "run") as execute:
            with redirect_stdout(io.StringIO()):
                podcast.transcribe(self.args())
        download.assert_not_called()
        execute.assert_not_called()
        self.assertEqual(before, (self.root / "transcripts/42.json").read_bytes())

    def test_changed_source_is_not_silently_reused(self):
        self.transcript({**self.episode, "audio_url": "https://example.com/old.mp3"})
        with patch.object(podcast, "download") as download:
            with self.assertRaisesRegex(ValueError, "Source changed"):
                podcast.transcribe(self.args())
        download.assert_not_called()

    def test_search_keeps_qualifications_and_separates_distant_passages(self):
        self.transcript()
        with redirect_stdout(io.StringIO()):
            podcast.search(self.args(query="portfolio", context=1))
        rows = [json.loads(line) for line in (self.root / "matches.jsonl").read_text().splitlines()]
        self.assertEqual([(r["start"], r["end"]) for r in rows], [(0, 48), (80, 108)])
        self.assertTrue(all(r["review_status"] == "unreviewed_keyword_match" for r in rows))
        self.assertTrue(all("Surrounding qualification." in r["text"] for r in rows))
        self.assertTrue(all(r["episode_id"] == "42" for r in rows))

    def test_coverage_rejects_untranscribed_curated_sources(self):
        passages = self.root / "passages.json"
        podcast.save_json(passages, {"42": {"example_id": "DC42", "ranges_seconds": [[0, 10]]}})
        with self.assertRaisesRegex(ValueError, "needs a catalogue entry and transcript"):
            podcast.coverage(self.args(passages=passages))


class DistributedEvidenceIntegrity(unittest.TestCase):
    def test_linked_fixtures_have_resolvable_local_destinations(self):
        class Links(HTMLParser):
            def __init__(self):
                super().__init__()
                self.targets = []

            def handle_starttag(self, tag, attrs):
                if tag == "a":
                    self.targets += [value for key, value in attrs if key == "href" and value]

        for page in (ROOT / "evals/fixtures").rglob("*.html"):
            links = Links()
            links.feed(page.read_text())
            for target in links.targets:
                parsed = urlparse(target)
                if not parsed.scheme and parsed.path:
                    self.assertTrue((page.parent / parsed.path).is_file(), (page.name, target))

    def test_design_discipline_sources_keep_audio_and_written_evidence_distinct(self):
        record = evaluation.read(ROOT / "references/design-discipline-coverage.json")
        notes = (ROOT / "references/design-discipline-examples.md").read_text()
        audio = []
        for source in record["sources"]:
            self.assertIn("## " + source["id"] + " —", notes)
            self.assertIn(source["url"], notes)
            self.assertTrue(source["verification"])
            transcript = source.get("transcription")
            if transcript:
                audio.append(source)
                self.assertRegex(transcript["audio_sha256"], r"^[0-9a-f]{64}$")
                self.assertRegex(source["transcript_sha256"], r"^[0-9a-f]{64}$")
                self.assertFalse(transcript["human_audio_verified"])
                self.assertFalse(transcript["speaker_diarization"])
                for start, end in source["ranges_seconds"]:
                    self.assertTrue(0 <= start < end <= transcript["final_transcript_timestamp_seconds"])
            else:
                self.assertRegex(source["source_content_sha256"], r"^[0-9a-f]{64}$")
                self.assertTrue(source["locators"])
        summary = record["transcription_summary"]
        self.assertEqual(summary["new_original_audio_transcripts"], len(audio))
        self.assertAlmostEqual(summary["new_audio_seconds"],
                               sum(s["transcription"]["final_transcript_timestamp_seconds"] for s in audio))
        danny = evaluation.read(ROOT / "references/danny-martinez-sources.json")
        by_id = {s["id"]: s for s in danny["sources"]}
        for reused in record["reused_sources"]:
            self.assertEqual(reused["transcription"]["audio_sha256"],
                             by_id[reused["source_id"]]["transcription"]["audio_sha256"])
        self.assertEqual(summary["total_original_audio_transcripts"], len(audio) + len(record["reused_sources"]))

    def test_case_references_resolve_to_curated_examples(self):
        example_ids = set()
        for path in (ROOT / "references").glob("*.md"):
            example_ids.update(re.findall(r"^## ([A-Z]+[0-9]+) —", path.read_text(), re.M))
        suite = evaluation.read(ROOT / "evals/portfolio-cases.json")
        for case in suite["cases"]:
            self.assertFalse(set(case.get("related_examples", [])) - example_ids, case["id"])

    def test_video_notes_preserve_audio_identity_and_reviewed_bounds(self):
        record = evaluation.read(ROOT / "references/video-portfolio-sources.json")
        notes = (ROOT / "references/video-portfolio-advice.md").read_text()
        self.assertEqual(record["coverage"]["original_recordings_transcribed"], len(record["sources"]))
        for source in record["sources"]:
            self.assertIn("## " + source["id"] + " —", notes)
            self.assertTrue(any(url in notes for url in (
                source["url"], source["discovery"].get("publisher_page_url", source["url"]))))
            transcript = source["transcription"]
            for key in ("audio_sha256", "transcript_sha256"):
                self.assertRegex(transcript[key], r"^[0-9a-f]{64}$")
            self.assertFalse(transcript["human_audio_verified"])
            self.assertFalse(transcript["speaker_diarization"])
            for start, end in source["ranges_seconds"]:
                self.assertTrue(0 <= start < end <= transcript["last_speech_end_seconds"])
        self.assertEqual(record["coverage"]["transcript_segments"],
                         sum(s["transcription"]["segment_count"] for s in record["sources"]))

    def test_hiring_humans_notes_have_traceable_primary_sources(self):
        record = evaluation.read(ROOT / "references/hiring-humans-sources.json")
        notes = (ROOT / "references/hiring-humans-examples.md").read_text()
        sources = record["sources"]
        self.assertEqual(len(sources), len({s["id"] for s in sources}))
        self.assertEqual(record["discovery"]["selected_articles_read"], len(sources))
        for source in sources:
            self.assertIn("## " + source["id"] + " —", notes)
            self.assertIn(source["url"], notes)
            self.assertTrue(source["verification"])
            self.assertRegex(source["rss_content_sha256"], r"^[0-9a-f]{64}$")

    def test_danny_sources_preserve_origin_and_transcript_bounds(self):
        record = evaluation.read(ROOT / "references/danny-martinez-sources.json")
        notes = (ROOT / "references/danny-martinez.md").read_text()
        sources = record["sources"]
        self.assertEqual(len(sources), len({s["id"] for s in sources}))
        for source in sources:
            self.assertIn("## " + source["id"] + " —", notes)
            self.assertTrue(source["verification"])
            if source["url"]:
                self.assertIn(source["url"], notes)
            for supplied in source.get("provided_images", []):
                self.assertRegex(supplied["sha256"], r"^[0-9a-f]{64}$")
            transcript = source.get("transcription")
            if transcript:
                self.assertRegex(transcript["audio_sha256"], r"^[0-9a-f]{64}$")
                self.assertFalse(transcript["human_audio_verified"])
                self.assertFalse(transcript["speaker_diarization"])
                for start, end in source["ranges_seconds"]:
                    self.assertTrue(0 <= start < end <= transcript["final_transcript_timestamp_seconds"])
        by_id = {s["id"]: s for s in sources}
        self.assertIsNone(by_id["DM01"]["url"])
        self.assertEqual(len(by_id["DM01"]["provided_images"]), 6)
        self.assertEqual(len(by_id["DM02"]["provided_images"]), 6)
        self.assertIn("same source", by_id["DM02"]["verification"])

    def test_cases_have_unique_ids_and_real_fixture_paths(self):
        suite = evaluation.read(ROOT / "evals/portfolio-cases.json")
        ids = [c["id"] for c in suite["cases"]]
        self.assertEqual(len(ids), len(set(ids)))
        for case in suite["cases"]:
            self.assertTrue(all(case.get(k) for k in ("request", "supplied_evidence", "expected_behavior")))
            checks = evaluation.criteria(suite, case)
            self.assertEqual(len(checks), len({c["id"] for c in checks}))
            if case.get("fixture"):
                self.assertTrue((ROOT / "evals" / case["fixture"]).is_dir())

    def test_every_curated_source_has_provenance_and_a_note(self):
        coverage = evaluation.read(ROOT / "references/dive-club-coverage.json")
        passages = evaluation.read(ROOT / "references/dive-club-passages.json")
        notes = (ROOT / "references/dive-club-examples.md").read_text()
        sources = {s["episode_id"]: s for s in coverage["transcribed_sources"]}
        self.assertEqual(coverage["episodes_with_curated_examples"], len(passages))
        self.assertEqual(coverage["episodes_transcribed_from_original_audio"], len(sources))
        for episode_id, passage in passages.items():
            source = sources[episode_id]
            self.assertIn("## " + passage["example_id"] + " —", notes)
            self.assertIn(source["publisher_url"], notes)
            self.assertRegex(source["audio_sha256"], r"^[0-9a-f]{64}$")
            self.assertFalse(source["human_audio_verified"])
            self.assertEqual(source["curated_passage_ranges_seconds"], passage["ranges_seconds"])
            for start, end in passage["ranges_seconds"]:
                self.assertTrue(0 <= start < end <= source["final_transcript_timestamp_seconds"])


if __name__ == "__main__":
    unittest.main()
