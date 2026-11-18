# Work-evidence coverage — 17 November 2026

**Result: the revised skill passes all five new coverage cases and 33 of 34 cases in a full-suite run. The one failure passed on a fresh repeat. The unchanged skill failed the single-view case in a blind baseline.**

This run addresses one piece of reviewer feedback: the skill was too willing to accept a portfolio whose side projects were unfinished, missing context, and supported by one image each. It did not consistently pick up that the current state was the problem. Visual taste was deliberately left out of scope.

## What changed

- A new [Check the work evidence](../../SKILL.md) section records, per project, what the page supplies and what it leaves out: audience, problem, contribution, artifacts, status, outcome, and recency.
- One view is treated as one view. The skill names what a single 1440px screenshot cannot establish — interaction, a second state, responsive behaviour, consistency, or shipped status — and counts distinct views rather than images.
- A repeated omission is reported once as a portfolio-level finding with a shared fix, not as one note per project.
- Missing facts are separated from missing evidence. Candidate facts remain dependencies; a second state, status label, date, or removed placeholder is a confirmed, bounded finding.
- The current state is assessed as it is: placeholders, drafts, duplicates, dead destinations, and inconsistent labels are findings.
- An inaccessible project is a limit on the review, not a portfolio defect when the candidate can share access privately.
- Coverage is matched to the role, so a content role is not required to show interaction states and an interface role is not let off with one frame.
- A **Supplied** evidence label was added, so facts stated by the candidate are confirmed as their account rather than demoted to unverified checks.
- **Evidence** joins the recommendation categories, and the report must state coverage for each inspected project.
- Precision guards keep the new criticality from becoming inference: a conditional or hedged improvement is optional advice, not a confirmed finding; explicit credits settle authorship; advice about material the user has not shown is not framed as a defect.
- The example index now groups hiring-outcome and causal-claim notes, and the skill says to read linked accounts of the same hire together.

## Cases

Five synthetic cases were added:

| Case | What it checks |
| --- | --- |
| `single-view-projects-lack-context` | Three side projects, one finished-state image each, no audience, contribution, or status; the repeated gap is one finding and the single view has a stated limit. |
| `messy-in-progress-listing` | Placeholders, a duplicate project, a reported-broken demo, inconsistent labels, and one complete project; the current state is not ready. |
| `one-screenshot-interaction-question` | One checkout frame cannot establish interaction; say what is needed without inventing runtime behaviour. |
| `single-artifact-sufficient-for-content-role` | One final artifact is enough for a content role with sound context; do not over-correct into demanding more views. |
| `image-count-is-not-coverage` | Twelve images that repeat one view are still one view. |

## Results

Each case used a fresh, ephemeral, read-only Codex reviewer followed by a separate grader. The configured model was `gpt-6.1-terra` with `low` reasoning through Codex CLI `0.167.0`; four workers ran independent cases.

| Case | Baseline (unchanged skill) | Revised |
| --- | --- | --- |
| single-view-projects-lack-context | fail | pass |
| messy-in-progress-listing | pass | pass |
| one-screenshot-interaction-question | pass | pass |
| single-artifact-sufficient-for-content-role | pass | pass |
| image-count-is-not-coverage | pass | pass |

Baseline: 4 of 5 cases passed; 36 of 38 criteria passed. Full revised run: 33 of 34 cases passed; 210 of 212 criteria passed.

The full run's only failure was the existing `source-content-extraction-and-team-credit` case. The reviewer promoted a hedged concern about the Lab listing to a `Should fix`, and did not list accessibility among the checks it left unverified. A fresh repeat of that case passed all six criteria. The failure did not reproduce on the repeat, so it looks like an inconsistent overreach rather than a stable gap in the coverage behaviour.

The baseline failure matches the reported behaviour: the old skill treated the single view as a problem mainly for the strongest project and did not state what the view could not establish about responsive behaviour or shipped status. In two earlier local baseline attempts with slightly different case wording, `messy-in-progress-listing` also failed; those attempts are retained locally and are not counted in the distributed baseline.

## Integrity and limits

One baseline grade was rejected because its quotation did not match the recorded answer. The attempt was preserved locally as `grade.invalid-attempt-1.json` and regraded without editing the answer or the quotation; its hash is recorded in the baseline file. The full run had no rejected grades.

- The full suite is one run on the final snapshot. Several earlier intermediate snapshots were also run and exposed overreach in adjacent cases; those runs informed the precision guards but are retained locally, not counted here.
- The changed ratings are evidence of behaviour on invented cases, not a measured increase in hiring effectiveness.
- The reviewer configuration is the local Codex account and model recorded above; another model or reasoning level may vary.
- The reviewed evidence is supplied text or local fixtures, not a rendered live site. Layout, interaction, and link operation remain untested where each case says so.
- The baseline is 4 of 5, not a uniform failure. The targeted claim is narrower: the old skill did not pick up the single-view gap in this case, and the revised skill did.

[Baseline inputs, answers, grades, hashes, and rejected-attempt record](2026-11-17-work-evidence-baseline.json) and [the full run with the reliability repeat](2026-11-17-work-evidence-full.json) are retained.
