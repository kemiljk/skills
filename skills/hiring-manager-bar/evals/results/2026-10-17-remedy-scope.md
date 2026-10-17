# Remedy-scope follow-up — 17 October 2026

**Result: pass.** 6 of 6 cases passed; criterion outcomes: {'pass': 36}.

Each case used a fresh, ephemeral, read-only Codex reviewer followed by a separate grader. Reviewers received frozen instructions, public source notes, and their own synthetic request/artifacts, without expected answers. The local reporter checked immutable input hashes, complete grading, and literal quotation support. The configured model was `gpt-6.1-sol` with `xhigh` reasoning through Codex CLI `0.162.0-alpha.17.2`.

| Case | Result |
| --- | --- |
| team-result-without-personal-ownership | pass |
| qualitative-evidence-under-confidentiality | pass |
| source-only-hover-gate | pass |
| unseen-copy-no-defect | pass |
| mutual-fair-work-evaluation | pass |
| source-content-extraction-and-team-credit | pass |

[Actual answers, expectations, grades, frozen hashes, and recorded review actions](2026-10-17-remedy-scope.json) are retained. Full frozen inputs and CLI logs remain local under `.research/skill-evals/remedy-scope-01/`.

Rejected grading attempts retained: 0.

This is one run of synthetic cases. It does not measure real hiring outcomes or establish a stable failure frequency. The separate live-portfolio exercise is exploratory public-content research, with its own access and rendering limits.

This targeted run checks the corrected rule on the affected case and five adjacent boundaries. It does not replace or erase the original 29-case result, and the other 23 cases were not freshly rerun on this snapshot. See the [expanded run](2026-10-17-expanded.md) for the broader prior result.

A [separate calibration check](2026-10-17-remedy-calibration.json) also regraded the unchanged earlier answer under the clarified criterion: all six criteria passed. That is a grading check, not an additional fresh portfolio review. The original failing grade remains preserved.
