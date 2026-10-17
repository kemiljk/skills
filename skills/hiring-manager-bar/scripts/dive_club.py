#!/usr/bin/env python3
"""Index, locally transcribe, and search public Dive Club podcast audio.

Raw research belongs in an ignored working directory, outside the skill package.
Transcription requires macOS 26+, Apple SpeechTranscriber, and the Swift compiler.
"""
import argparse
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
import hashlib
import html
import json
from pathlib import Path
import re
import subprocess
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET

FEED = "https://media.rss.com/diveclub/feed.xml"
ITUNES = "{http://www.itunes.com/dtds/podcast-1.0.dtd}"
TOPICS = r"portfolio|case stud|hir(?:e|ed|ing)|job market|job search|dream job|recruit"
SEARCH = r"portfolio|case stud|recruit|hir(?:e|ed|ing)|interview|candidate|résumé|resume|job (?:hunt|search|market)"


def save_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".part")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
    temporary.replace(path)


def download(url, destination):
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = destination.with_suffix(destination.suffix + ".part")
    with urllib.request.urlopen(url, timeout=90) as response, temporary.open("wb") as out:
        while block := response.read(1024 * 1024):
            out.write(block)
    temporary.replace(destination)


def stamp(seconds):
    seconds = int(seconds)
    return f"{seconds // 3600:02}:{seconds // 60 % 60:02}:{seconds % 60:02}"


def index(args):
    raw = args.feed_file.read_bytes() if args.feed_file else urllib.request.urlopen(FEED, timeout=60).read()
    root = ET.fromstring(raw)
    if root.findtext("channel/title") != "Dive Club 🤿":
        raise ValueError("Expected the Dive Club podcast feed")
    episodes = []
    for item in root.findall("channel/item"):
        enclosure = item.find("enclosure")
        if enclosure is None:
            continue
        url = item.findtext("link", "")
        episode_id = url.rstrip("/").rsplit("/", 1)[-1]
        if not episode_id.isdigit() or not enclosure.get("url", "").startswith("https://"):
            raise ValueError(f"Unexpected episode identity or audio URL: {url}")
        title = item.findtext("title", "")
        description = html.unescape(re.sub(r"<[^>]+>", " ", item.findtext("description", "")))
        duration = item.findtext(ITUNES + "duration", "")
        episodes.append({
            "id": episode_id, "guid": item.findtext("guid"), "title": title,
            "published": parsedate_to_datetime(item.findtext("pubDate")).isoformat(),
            "episode_number": item.findtext(ITUNES + "episode"),
            "url": url, "audio_url": enclosure.get("url"), "duration": duration,
            "metadata_topic_match": bool(re.search(TOPICS, title + " " + description, re.I)),
        })
    save_json(args.workdir / "catalog.json", {
        "feed_url": FEED, "indexed_at": datetime.now(timezone.utc).isoformat(),
        "feed_sha256": hashlib.sha256(raw).hexdigest(), "episodes": episodes,
    })
    (args.workdir / "feed.xml").write_bytes(raw)
    print(f"Indexed {len(episodes)} episodes; {sum(e['metadata_topic_match'] for e in episodes)} metadata topic matches.")


def transcribe(args):
    catalog = json.loads((args.workdir / "catalog.json").read_text())
    by_id = {e["id"]: e for e in catalog["episodes"]}
    unknown = set(args.ids) - by_id.keys()
    if unknown:
        raise ValueError(f"Unknown episode IDs: {sorted(unknown)}")
    episodes = [by_id[i] for i in args.ids] if args.ids else catalog["episodes"]
    if args.topic_matches:
        episodes = [e for e in episodes if e["metadata_topic_match"]]
    pending = []
    for episode in episodes:
        output = args.workdir / "transcripts" / (episode["id"] + ".json")
        if output.exists():
            old = json.loads(output.read_text())
            if old["episode"]["guid"] != episode["guid"] or old["episode"]["audio_url"] != episode["audio_url"]:
                raise ValueError(f"Source changed for {episode['id']}; review the old transcript before replacing it")
        else:
            pending.append(episode)
    pending = pending[:args.limit]
    if not pending:
        print("No pending episodes in this selection.")
        return
    source = Path(__file__).with_name("transcribe.swift")
    binary = args.workdir / "transcribe"
    if not binary.exists() or binary.stat().st_mtime < source.stat().st_mtime:
        subprocess.run(["swiftc", "-O", "-parse-as-library", "-module-cache-path",
                        str(args.workdir / "swift-cache"), str(source), "-o", str(binary)], check=True)
    failed = []
    for number, episode in enumerate(pending, 1):
        audio = args.workdir / "audio" / (episode["id"] + ".mp3")
        try:
            print(f"[{number}/{len(pending)}] {episode['title']}", flush=True)
            download(episode["audio_url"], audio)
            digest = hashlib.sha256(audio.read_bytes()).hexdigest()
            started = time.monotonic()
            temporary = args.workdir / (episode["id"] + "-apple.json")
            subprocess.run([str(binary), str(audio), str(temporary)], check=True)
            result = json.loads(temporary.read_text())
            if not result.get("segments"):
                raise ValueError("The transcriber returned no segments")
            seconds = round(time.monotonic() - started, 2)
            save_json(args.workdir / "transcripts" / (episode["id"] + ".json"), {
                "schema_version": 1, "episode": episode,
                "provenance": {
                    "kind": "local_machine_transcript", "audio_sha256": digest,
                    "transcribed_at": datetime.now(timezone.utc).isoformat(),
                    "engine": result["engine"], "operating_system": result["operatingSystem"],
                    "model_revision": "System-managed; not exposed by Apple's API",
                    "elapsed_seconds": seconds, "locale": result["locale"],
                    "human_audio_verified": False, "speaker_diarization": False,
                },
                "segments": result["segments"],
            })
            temporary.unlink()
            print(f"Saved {episode['id']}: {len(result['segments'])} segments in {seconds}s", flush=True)
            if not args.keep_audio:
                audio.unlink()
        except Exception as error:
            failed.append({"id": episode["id"], "error": str(error)})
            print(f"Failed {episode['id']}: {error}", file=sys.stderr, flush=True)
    if failed:
        save_json(args.workdir / "failures.json", failed)
        raise SystemExit(1)


def search(args):
    pattern = re.compile(args.query, re.I)
    output = args.workdir / "matches.jsonl"
    count = 0
    with output.open("w") as out:
        for path in sorted((args.workdir / "transcripts").glob("*.json")):
            transcript = json.loads(path.read_text())
            segments = transcript["segments"]
            indexes = [i for i, s in enumerate(segments) if pattern.search(s["text"])]
            # Merge overlapping context windows; a hit is a lead, not a vetted example.
            windows = []
            for i in indexes:
                lo, hi = max(0, i - args.context), min(len(segments), i + args.context + 1)
                if windows and lo <= windows[-1][1]:
                    windows[-1][1] = max(hi, windows[-1][1])
                else:
                    windows.append([lo, hi])
            for lo, hi in windows:
                chosen = segments[lo:hi]
                row = {"episode_id": transcript["episode"]["id"], "title": transcript["episode"]["title"],
                       "episode_url": transcript["episode"]["url"], "start": chosen[0]["start"],
                       "end": chosen[-1]["end"], "timestamp": stamp(chosen[0]["start"]),
                       "text": " ".join(s["text"].strip() for s in chosen),
                       "review_status": "unreviewed_keyword_match"}
                out.write(json.dumps(row, ensure_ascii=False) + "\n")
                count += 1
    print(f"Wrote {count} unreviewed passage windows to {output}")


def coverage(args):
    """Rebuild provenance from transcripts and an explicitly curated passage map."""
    catalog = json.loads((args.workdir / "catalog.json").read_text())
    curated = json.loads(args.passages.read_text())
    transcripts = {p.stem: json.loads(p.read_text())
                   for p in (args.workdir / "transcripts").glob("*.json")}
    episodes = catalog["episodes"]
    known = {e["id"] for e in episodes}
    if set(curated) - (known & transcripts.keys()):
        raise ValueError("Every curated source needs a catalogue entry and transcript")
    rows = []
    for episode in episodes:
        if episode["id"] not in transcripts:
            continue
        transcript = transcripts[episode["id"]]
        if any(transcript["episode"][key] != episode[key] for key in ("guid", "audio_url")):
            raise ValueError(f"Source changed for {episode['id']}; review provenance before updating coverage")
        provenance = transcript["provenance"]
        passage = curated.get(episode["id"], {})
        ranges = passage.get("ranges_seconds", [])
        end = transcript["segments"][-1]["end"]
        if any(not 0 <= start < stop <= end for start, stop in ranges):
            raise ValueError(f"Invalid passage range for {episode['id']}")
        rows.append({
            "episode_id": episode["id"], "episode_number": episode["episode_number"],
            "title": episode["title"], "published": episode["published"],
            "publisher_url": episode["url"], "audio_url": episode["audio_url"], "guid": episode["guid"],
            **{key: provenance[key] for key in ("audio_sha256", "engine", "operating_system", "locale", "transcribed_at")},
            "final_transcript_timestamp_seconds": end, "segment_count": len(transcript["segments"]),
            "human_audio_verified": False, "speaker_diarization": False,
            "curated_example_id": passage.get("example_id"), "curated_passage_ranges_seconds": ranges,
            "review_status": "selected_passages_reviewed_as_text" if passage else "transcribed_discovery_material_not_promoted",
        })
    suite = json.loads(args.suite.read_text())
    save_json(args.output, {
        "schema_version": 1, "research_date": datetime.now(timezone.utc).date().isoformat(),
        "publisher_feed": catalog["feed_url"], "feed_sha256": catalog["feed_sha256"],
        "catalogue_entries_indexed": len(episodes),
        "metadata_topic_matches": sum(e["metadata_topic_match"] for e in episodes),
        "episodes_transcribed_from_original_audio": len(rows),
        "transcribed_audio_hours": round(sum(r["final_transcript_timestamp_seconds"] for r in rows) / 3600, 2),
        "episodes_with_curated_examples": len(curated), "synthetic_evaluation_cases": len(suite["cases"]),
        "coverage_statement": "Prioritised corpus, not an exhaustive search of all podcast speech. Only cited passage ranges were promoted.",
        "limitations": [
            "Metadata and speech keyword matches can miss relevant discussion or retrieve incidental and sponsor copy.",
            "Speaker attribution depends on context and publisher metadata; the transcriber does not diarize speakers.",
            "Selected text review is not human audio verification.",
            "Repeat accounts of one candidate are not independent evidence.",
            "Transcription coverage does not establish hiring improvement or behavioral evaluation results.",
        ],
        "transcribed_sources": rows,
        "remaining_metadata_matches": [
            {"episode_id": e["id"], "title": e["title"], "publisher_url": e["url"], "status": "not_transcribed_in_this_pass"}
            for e in episodes if e["metadata_topic_match"] and e["id"] not in transcripts
        ],
    })
    print(f"Recorded {len(rows)} transcripts and {len(curated)} curated source episodes in {args.output}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workdir", type=Path, required=True, help="Ignored local research directory")
    commands = parser.add_subparsers(dest="command", required=True)
    p = commands.add_parser("index")
    p.add_argument("--feed-file", type=Path)
    p.set_defaults(run=index)
    p = commands.add_parser("transcribe")
    p.add_argument("--ids", nargs="+", default=[])
    p.add_argument("--topic-matches", action="store_true")
    p.add_argument("--limit", type=int, default=1, help="Maximum new episodes this run")
    p.add_argument("--keep-audio", action="store_true")
    p.set_defaults(run=transcribe)
    p = commands.add_parser("search")
    p.add_argument("--query", default=SEARCH)
    p.add_argument("--context", type=int, default=2, help="Neighbouring segments on each side")
    p.set_defaults(run=search)
    p = commands.add_parser("coverage")
    skill = Path(__file__).resolve().parents[1]
    p.add_argument("--passages", type=Path, default=skill / "references/dive-club-passages.json")
    p.add_argument("--suite", type=Path, default=skill / "evals/portfolio-cases.json")
    p.add_argument("--output", type=Path, default=skill / "references/dive-club-coverage.json")
    p.set_defaults(run=coverage)
    args = parser.parse_args()
    if getattr(args, "limit", 1) < 1 or getattr(args, "context", 0) < 0:
        parser.error("limit must be positive, and context must be nonnegative")
    args.workdir = args.workdir.resolve()
    args.workdir.mkdir(parents=True, exist_ok=True)
    args.run(args)


if __name__ == "__main__":
    main()
