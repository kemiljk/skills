---
name: hiring-manager-bar
description: "Review a job-seeking portfolio against Karl Koch's hiring manager bar and recommend prioritized changes to site code and content. Use for portfolio readiness, hiring clarity, or a portfolio review with actionable implementation guidance."
license: MIT
---

# Hiring Manager Bar

Treat the hiring manager as a user with a job to do: find the work, understand what the candidate contributed, and decide whether their experience warrants a conversation. Creativity should help that reading. A short, specific explanation can be enough; a long case study is not a requirement.

## Scope

Default to review and recommendations. Implement changes only when the user requests fixes; follow any existing authorization. Preserve the site's identity, existing components, and unrelated work.

Use the stated target role, level, and review scope. If the target is unstated, make a provisional assumption from the content and identify it. Ask only when the answer would materially change the review. Do not infer seniority from visual polish or impose job-seeking requirements on a site made primarily for personal enjoyment.

## Read as a visitor, then inspect the implementation

1. Follow the ordinary entry path before using repository knowledge to fill in missing context: landing page → work listing → project → about/contact. Record what is easy to answer and where understanding breaks down.
2. Inspect representative projects that support the target role, including contrasting types of work when relevant. Name the pages sampled and omissions; do not imply a whole-site review from one case study.
3. Trace material findings to the actual routes, content entries, shared components, and styles. Check the full relevant content and linked destinations before claiming something is missing. Separate a fact that is absent from one that exists but is hard to discover.
4. When rendering is available, check the reading path at desktop and narrow widths, with keyboard navigation and touch-compatible controls. Test reduced motion when animation gates access or comprehension. Focus checks on reaching, reading, and returning from the work, and finding contact.

Source markup and fetched text do not establish visible layout, interaction behavior, loading speed, or accessibility. A local checkout and a live deployment may also differ: identify which each observation describes.

## The bar

| Hiring question | Evidence to look for |
| --- | --- |
| What are you good at, and where might you fit? | A clear introduction and selected work that supports the target role; claims connected to concrete examples |
| What did you make and ship? | Identifiable projects, enough problem and user context to understand them, visible artifacts, and honest status such as shipped, prototype, or experiment |
| What was your contribution? | Specific ownership and decisions, with collaborators and constraints where relevant; distinguish personal work from team outcomes |
| How do you work? | Useful examples of judgment, tradeoffs, collaboration, and results; enough detail to understand the work without prescribing a process-heavy case-study template |
| Can I find and understand the work? | Familiar navigation, descriptive links, legible text and images, scannable hierarchy, and core information accessible without hover or compulsory novelty |
| Can I take the next step? | Discoverable, working contact and any résumé or professional context needed for the stated goal |

For Design Engineering, distinguish product design, production implementation, and refinement of an interaction. Do not equate lifecycle ownership with working alone. For leadership roles, look for evidence of direction and influence where the target calls for it; do not apply leadership criteria to every candidate.

Experiments can add valuable evidence of curiosity and craft. Recommend a discoverable playground or a clearer separation only when experiments obscure the core work journey. Keep distinctive typography, writing, and interactions that support understanding. Do not require a new page or a generic portfolio layout merely to satisfy the rubric.

## Evidence and priority

Every finding needs one evidence label:

- **Rendered:** Observed on a named page, viewport, and relevant interaction state.
- **Source:** Confirmed in a named file or content entry; visual or runtime consequences remain unverified unless separately observed.
- **Unverified:** A plausible concern that needs a specified check. Keep it in open checks, outside the confirmed fix list.

Prioritize by the effect on the hiring questions:

- **Blocking:** Prevents reaching or understanding the core work, contribution, or contact path in the reviewed scope.
- **Should fix:** Creates material ambiguity or unnecessary effort, with a bounded correction.
- **Polish:** Improves an already understandable experience.

Do not turn personal taste into a blocker. Missing project facts need the candidate's input; code cannot establish ownership, manufacture metrics, or turn a prototype into shipped work. Respect confidentiality and accept useful qualitative evidence when numbers or public artifacts are unavailable.

## Recommend changes that can be implemented

For each confirmed finding, give the priority, evidence label, affected page and actual file/component when available, the unanswered hiring question, the smallest useful change, and an observable acceptance check. Include dependencies when content or assets must come from the candidate. Prefer fixing a shared component or content model when the same verified issue repeats.

For example, if existing project summaries are only revealed on hover, recommend exposing those fields in the shared card's resting layout. Acceptance: a visitor can identify the project and contribution without hovering, including at a narrow viewport and during keyboard navigation. If the contribution is absent from the content, request the facts before populating it; a layout change alone does not resolve the gap.

Recommend exact content or code changes only as far as the evidence allows. For a URL-only review, identify the page and element and describe the implementation target without inventing filenames. Avoid broad redesigns when a label, content field, reading-order change, or removal of a gate solves the problem.

## Report and completion

Lead with **passes**, **needs changes**, or **not assessable**, scoped to the inspected pages and stated role. This judges the portfolio's ability to answer the hiring questions, not the candidate's employability. A pass needs observed support for the core questions; strong visuals do not compensate for unclear ownership. A material unanswered question means needs changes. Missing access or insufficient evidence to judge the core journey means not assessable; still report any confirmed local findings.

Keep the report compact:

1. Verdict, role assumptions, scope, and evidence limitations.
2. Specific strengths to preserve.
3. Prioritized recommendations: **priority / evidence / page + file → problem → change → acceptance check**.
4. Candidate-supplied facts and remaining verification, if any.

A review is complete when each material finding has a traceable cause and implementable recommendation, or an explicit dependency on missing facts. Do not manufacture findings for every rubric row or use numeric readiness scores.

In fix mode, implement the authorized bounded changes using existing site materials. Run the checks appropriate to the affected code and repeat the affected visitor journey. Report completed edits, verification results, and unresolved content needs. A successful build proves compilation, not comprehension or rendered behavior.

## Sources

- [Karl Koch — The hiring manager is your user](https://karlkoch.me/writing/the-hiring-manager-is-your-user/): the core questions, clarity of contribution, and room for experimentation.
- [Won J. You — Portfolio Review](https://github.com/wonjyou/portfolio-review-skill): supplementary review areas covering positioning, project evidence, navigation, and contact. This skill is self-contained; neither source needs to be fetched during a normal review.
