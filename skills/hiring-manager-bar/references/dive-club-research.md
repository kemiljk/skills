# Extending the Dive Club evidence set

This is reference and evaluation material for a skill, not a model fine-tune. Keep evidence small enough to change a review decision. Full transcripts are working material; they are not the skill's runtime context.

## Current coverage

The 17 October 2026 research used two passes: an initial 33 episodes selected for portfolio and hiring relevance, followed by 32 more covering staff influence, career transitions, design engineering, product judgment, storytelling, and less obvious hiring discussions. Together they cover 65 episodes and approximately 52.92 hours of speech. Selected passages from 26 source episodes became notes, including nine sources added in the second pass. The [coverage record](dive-club-coverage.json) preserves identities, hashes, cited ranges, and 9 remaining metadata leads. The [passage map](dive-club-passages.json) records the explicit curation decisions used to regenerate that record.

This is a prioritised corpus, not an exhaustive search of the show's speech. Metadata matches can include incidental references and recruitment links. Repeated advice, host compilations, sponsor copy, and unrelated product discussions are not automatically promoted. Audio-hour totals approximate final speech timestamps; keyword misses do not establish that an episode contains no useful discussion.

The [evaluation guide](../evals/README.md) separates local tool checks from behavioral testing. An initial independent blind run of 12 synthetic cases produced 9 passes, 2 cases needing reporting/evidence changes, and 1 uncertain source fixture. Actual answers and independent grading are retained in the [initial result](../evals/results/2026-10-17-initial.md). After guidance and fixture corrections, the [revised snapshot](../evals/results/2026-10-17-revised.md) passed 18 cases and 108 criteria. The suite has since expanded; consult the evaluation guide for results tied to each frozen version. These records do not establish improved hiring outcomes.

## Collect from the original audio

Use Dive Club's [publisher feed](https://media.rss.com/diveclub/feed.xml) for episode identity, publication date, audio URL, and catalogue coverage. The feed includes numbered interviews and shorter unnumbered episodes. Metadata keyword matches are discovery leads; they do not establish transcript coverage or relevance.

The included Python helper indexes that feed, downloads selected audio, runs the adjacent Swift helper, and searches timestamped results. It uses Apple's on-device `SpeechAnalyzer` and `SpeechTranscriber` on macOS 26+. English assets must be available; the system may download them on first use. Swift command-line tools are required. No paid transcription service or Python packages are required.

From the repository root:

```sh
python3 skills/hiring-manager-bar/scripts/dive_club.py --workdir .research/dive-club index
python3 skills/hiring-manager-bar/scripts/dive_club.py --workdir .research/dive-club transcribe --ids 2474921 2400906 2552458 --limit 3
python3 skills/hiring-manager-bar/scripts/dive_club.py --workdir .research/dive-club search
python3 skills/hiring-manager-bar/scripts/dive_club.py --workdir .research/dive-club coverage
```

For an installed copy, invoke the Python helper by its actual installation path and choose an ignored working directory in the current project.

`--topic-matches --limit N` processes up to N new episodes matching the metadata keywords. Explicit IDs preserve a chosen priority order. Completed transcripts are skipped. Changed episode identities or audio URLs require review before replacing prior results. Audio is deleted after successful transcription unless `--keep-audio` is passed. Failed episodes remain pending and are reported; interrupted runs can be resumed with the same selection.

The ignored `.research/` directory contains the catalogue, feed snapshot, working transcripts, executable, and passage matches. Keep it separate from versioned skill material. Provenance records the episode GUID, audio URL, audio SHA-256, OS version, locale, and transcription engine. Apple's model is system-managed; the API does not expose its version. Re-downloaded audio can contain different advertisements, so preserve the hash and recheck timestamps before reusing an old passage reference.

API sources: [SpeechAnalyzer](https://developer.apple.com/documentation/speech/speechanalyzer), [Apple's file transcription example](https://developer.apple.com/videos/play/wwdc2025/277/).

## Other publishers and formats

The same Swift helper accepts a local audio file and a JSON output path. After the Dive Club helper has compiled it, a file from another public publisher can be transcribed with:

```sh
.research/dive-club/transcribe path/to/public-audio.mp3 .research/another-transcript.json
```

That output contains speech, timings, and engine details; record the publisher identity, original media URL, publication date, audio hash, and download method separately before curating it. Distinguish locally generated ASR, platform captions, written articles, and publisher highlights. Inspect accessible public material without bypassing subscriber or sign-in boundaries. If a download fails, record the access limit rather than infer that the source has no useful advice.

[Design Discipline coverage](design-discipline-coverage.json), [video/podcast provenance](video-portfolio-sources.json), [Hiring Humans sources](hiring-humans-sources.json), and [Danny Martinez sources](danny-martinez-sources.json) preserve those distinctions. Their notes contain short attributed paraphrases. A source repeated across articles, interviews, supplied screenshots, or captions remains one evidence family; Danny’s Design Discipline episode is recorded under DM07 rather than counted again as a new curated example.

## Review, then promote

1. Search broadly, including portfolio, case study, hiring, interview, and role-specific terms. Read surrounding discussion, not just the matched sentence. A search miss is not proof that an episode has no relevant discussion.
2. Identify the speaker from the conversation and publisher metadata. The helper does not diarize speakers. Separate a guest's experience, a hiring manager's stated preference, the host's anecdote, and a hypothetical suggestion.
3. Confirm the mechanism: what concrete work or presentation choice did the speaker value, for which role and hiring stage? Capture counterexamples, qualifications, and disagreements.
4. Record a short original paraphrase, episode link, publication date, timestamp range, evidence type, useful review action, and boundary. Check critical names and claims against the audio before quoting or marking them audio-verified. Machine transcription and comparison with another ASR engine are not human listening.
5. Update the passage map with the source episode, example ID, and reviewed timestamp ranges, then run `coverage` to rebuild provenance. The command rejects missing transcripts, changed source identities, and out-of-bounds ranges.
6. Add a synthetic evaluation case only when it tests a meaningful decision. Label invented inputs and expected behavior clearly. Do not imply that a synthetic case is a real candidate, an observed hire, or a completed evaluation run.

Use `references/dive-club-examples.md` for the curated set and `evals/portfolio-cases.json` for evaluation requests and expected behavior. Follow the evaluation guide to test the skill with the request and supplied artifacts before consulting expectations. Record actual outcomes separately, preserve failures, and rerun changed cases plus broader regressions. Writing expectations or passing local integrity checks does not establish behavioral improvement.

## Interpretation limits

Reported hiring success does not establish that a portfolio choice caused the offer. Repeated discussion of the same candidate across episodes is one example, not independent corroboration. Prominent guests and featured successful candidates are a selected sample; it does not represent all roles, employers, or unsuccessful candidates.

Do not reproduce full transcripts in the distributed skill. Keep concise attributed paraphrases and links, preserve source ownership, and avoid importing sponsor claims as hiring evidence. Existing reference notes do not establish the current state of a portfolio website.
