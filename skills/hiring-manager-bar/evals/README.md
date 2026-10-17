# Testing Hiring Manager Bar

Two layers serve different purposes. Local Python tests check the integrity of the evaluation and research tools. Fresh reviewers exercise the skill's decisions on synthetic portfolio requests; separate graders assess their actual answers. Neither layer measures real hiring success.

## Local regression checks

From the repository root:

```sh
PYTHONPYCACHEPREFIX=/tmp/hmb-test-cache python3 -m unittest discover -s skills/hiring-manager-bar/tests -v
```

These checks require only Python's standard library. They verify that expectations stay out of reviewer inputs, fixtures are frozen, incomplete or invented grading evidence cannot pass, completed transcripts are reused safely, retrieval retains context, and curated source notes have matching provenance. They make no model calls and do not download audio.

## Behavioral evaluation

The [suite](portfolio-cases.json) contains invented cases and expected decisions. It covers role fit, ownership, confidentiality, concise evidence, side projects, specialist roles, senior and leadership contribution, source-only interactions, inaccessible work, linked credits, evidence attribution, optional advice, unsupported impact claims, and bounded use of hiring advice. Some cases describe supplied information; others contain actual local artifacts. None are real candidates. Each result records the exact suite and skill snapshot it exercised.

Prepare an immutable run in an ignored directory:

```sh
python3 skills/hiring-manager-bar/scripts/evaluate.py prepare --output .research/skill-evals/revised-01
```

`--case ID` selects individual cases. The snapshot includes the skill, its references, and only the selected cases. Each reviewer's directory contains its request and artifacts, without expected answers. Expected decisions live outside that directory. This separation is prompt-based isolation, not an operating-system security boundary.

With permission to send those frozen instructions, public source notes, and synthetic fixtures to the configured Codex model provider:

```sh
python3 skills/hiring-manager-bar/scripts/evaluate.py run --run .research/skill-evals/revised-01 --jobs 3
python3 skills/hiring-manager-bar/scripts/evaluate.py report --run .research/skill-evals/revised-01
```

The runner uses the installed `codex` CLI and its configured account and model. It starts a fresh, ephemeral, read-only review process for each case, followed by a separate grading process. It makes model-service calls and consumes account usage. Review processes can inspect local fixture files but are instructed not to edit artifacts, access live services, read expectations, or self-grade. No reviewer model is hardcoded.

Grade each expected decision and each shared evidence contract semantically as pass, fail, or uncertain, with a reason and an exact quotation from the answer. Empty quotations are permitted for absence-based criteria with an explanation. The local reporter checks completeness, input hashes, and quotation integrity; it does not judge meaning through keywords. A missing, invalid, failed, or uncertain result cannot become an overall pass. Inspect grader reasoning as well as the summary. If a saved grade is invalid, preserve it and its event log under attempt-specific filenames before running `--phase grade` again. Do not repair quotations by rewriting the recorded model output. Failed or uncertain semantic decisions remain test results, rather than formatting retries.

`--jobs` bounds concurrent independent cases from 1 to 4 (default 1); each case is reviewed before its separate grading call. `--phase respond` and `--phase grade` run the phases separately. Completed outputs are retained for resumability; prepare a new run directory for fresh repeats. `import --run RUN --responses FILE...` accepts independently produced `{"cases": [{"id": "...", "response": "..."}]}` responses. Importing answers does not grade them. Record execution context and limitations when using a different evaluator path.

For change evaluation, preserve a baseline, fix the observed failure, then rerun affected cases and the broader suite. Repeat important cases before claiming reliability. One passing synthetic run is a regression signal, not a measured increase in hiring effectiveness.

## Recorded results

The [initial run](results/2026-10-17-initial.md) used 12 blind cases, three independent reviewers, and a separate grader. It found two evidence/reporting failures and one ambiguous source fixture. The [revised run](results/2026-10-17-revised.md) passed all 18 cases and 108 criteria after correcting those issues. An invalid grader quotation was rejected and independently regraded; both attempts are retained. That snapshot predates the subsequent Danny Martinez, Design Discipline, Hiring Humans, and video research. The actual responses, frozen input hashes, and grading are retained alongside each summary.

The [expanded run](results/2026-10-17-expanded.md) exercised all 29 cases: 28 passed and one failed a literal placement rule. Independent adjudication found the rule overbroad: it penalised a safe conditional remedy within a supported finding. The rule and criterion were narrowed, and [six fresh affected/adjacent cases](results/2026-10-17-remedy-scope.md) passed all 36 criteria. A [separate calibration regrade](results/2026-10-17-remedy-calibration.json) also accepted the unchanged earlier answer under the clarified criterion. The original failure remains recorded. The other 23 cases were not freshly rerun after this narrow correction; do not describe the latest snapshot as a fresh 29/29 pass.

The separate [live-portfolio exercise](results/2026-10-17-live-portfolios.md) applied a frozen candidate to eight established designers’ public sites. Six supported scoped source-content passes and two were not assessable through the available reader. No rendered readiness pass or clear skill instruction failure was established. It is exploratory research with one reviewer and provisional roles, rather than a blind accuracy test. Its contact-extraction, attribution, and verdict-scope observations informed one new synthetic fixture.
