---
name: hiring-manager-bar
description: "Review a job-seeking portfolio in Figma Design or Make against Karl Koch's hiring manager bar and recommend prioritized changes to design, content, and implementation."
license: MIT
---

# Hiring Manager Bar

Treat the hiring manager as a user with a job to do: find the work, understand what the candidate contributed, and decide whether their experience warrants a conversation. Creativity should help that reading. A short, specific explanation can be enough; a long case study is not a requirement.

## Scope

Default to review and recommendations. Implement changes only when the user requests fixes; follow any existing authorization. Preserve the portfolio's identity, existing components, and unrelated work.

Use the stated target role, level, and review scope. If the target is unstated, make a provisional assumption from the content and identify it. Ask only when the answer would materially change the review. Do not infer seniority from visual polish or impose job-seeking requirements on a site made primarily for personal enjoyment.

## Read as a visitor, then inspect the construction

1. Follow the ordinary entry path before using hidden design or implementation knowledge to fill in missing context: landing page → work listing → project → about/contact. Record what is easy to answer and where understanding breaks down.
2. Inspect representative projects that support the target role, including contrasting types of work when relevant. Name the pages or frames sampled and omissions; do not imply a whole-portfolio review from one case study.
3. Trace material findings to the actual content and shared construction. Check the full relevant content and accessible linked destinations before claiming something is missing. Separate a fact that is absent from one that exists but is hard to discover.

**Figma Design:** inspect the named frames, editable text, component instances, variants, variables, auto layout, resizing rules, and prototype connections. Preserve useful instance relationships. Review desktop and narrow layouts with representative content. Follow prototype navigation when available; describe missing focus, touch, and reduced-motion behaviour as design requirements to verify in implementation. A static frame cannot prove working navigation, contact delivery, accessibility, or loading speed.

**Make:** inspect available source and the rendered preview. Check the reading path at desktop and narrow widths, with keyboard navigation and touch-compatible controls. Test reduced motion when animation gates access or comprehension. Focus checks on reaching, reading, and returning from the work, and finding contact. Distinguish simulated contact or persistence from functioning services.

Source markup and fetched text do not establish visible layout, interaction behaviour, loading speed, or accessibility. A design, preview, and live deployment may differ: identify which each observation describes. Disclose inaccessible content and checks.

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

- **Design:** Confirmed in a named frame, layer, component, or prototype state; production behaviour remains unverified.
- **Rendered:** Observed in a running Make preview or accessible live page, with a named viewport and relevant interaction state.
- **Source:** Confirmed in available Make source or a content entry; visual or runtime consequences remain unverified unless separately observed.
- **Unverified:** A plausible concern that needs a specified check. Keep it in open checks, outside the confirmed fix list.

Prioritize by the effect on the hiring questions:

- **Blocking:** Prevents reaching or understanding the core work, contribution, or contact path in the reviewed scope.
- **Should fix:** Creates material ambiguity or unnecessary effort, with a bounded correction.
- **Polish:** Improves an already understandable experience.

Do not turn personal taste into a blocker. Missing project facts need the candidate's input; code cannot establish ownership, manufacture metrics, or turn a prototype into shipped work. Respect confidentiality and accept useful qualitative evidence when numbers or public artifacts are unavailable.

## Recommend changes that can be implemented

For each confirmed finding, give the priority, evidence label, affected page or frame and actual layer, component, or source file when available, the unanswered hiring question, the smallest useful change, and an observable acceptance check. Include dependencies when content or assets must come from the candidate. Prefer fixing a shared component or content model when the same verified issue repeats.

For example, if existing project summaries are only revealed on hover, recommend exposing those fields in the shared card's resting layout. In Design, revise the component and check representative instances; in Make, revise the shared implementation and exercise it. Acceptance: a visitor can identify the project and contribution without hovering, including at a narrow viewport and during keyboard navigation. If the contribution is absent from the content, request the facts before populating it; a layout change alone does not resolve the gap.

Recommend exact content, design, or code changes only as far as the evidence allows. For a URL-only review, identify the page and element and describe the implementation target without inventing filenames. Avoid broad redesigns when a label, content field, reading-order change, or removal of a gate solves the problem.

For a reported bug, state the concrete consumer use case, prerequisites and reproduction steps, expected and actual behaviour, and impact. Only call it reproduced when the sequence was executed in the relevant medium. A prototype observation establishes prototype behaviour, not a production bug.

## Report and completion

Lead with **passes**, **needs changes**, or **not assessable**, scoped to the inspected pages and stated role. This judges the portfolio's ability to answer the hiring questions, not the candidate's employability. A pass needs observed support for the core questions; strong visuals do not compensate for unclear ownership. A material unanswered question means needs changes. Missing access or insufficient evidence to judge the core journey means not assessable; still report any confirmed local findings.

Keep the report compact:

1. Verdict, role assumptions, scope, and evidence limitations.
2. Specific strengths to preserve.
3. Prioritized recommendations: **priority / evidence / page or frame + layer, component, or file → problem → change → acceptance check**.
4. Candidate-supplied facts and remaining verification, if any.

A review is complete when each material finding has a traceable cause and implementable recommendation, or an explicit dependency on missing facts. Do not manufacture findings for every rubric row or use numeric readiness scores.

In fix mode, implement the authorised bounded changes using existing portfolio materials. In Design, recheck affected instances, representative layouts, and prototype paths, and annotate remaining runtime requirements. In Make, run checks appropriate to the affected code and repeat the affected visitor journey. Report completed edits, verification results, and unresolved content needs. A successful build proves compilation, not comprehension or rendered behaviour.

## Sources

- [Karl Koch — The hiring manager is your user](https://karlkoch.me/writing/the-hiring-manager-is-your-user/): the core questions, clarity of contribution, and room for experimentation.
- [Won J. You — Portfolio Review](https://github.com/wonjyou/portfolio-review-skill): supplementary review areas covering positioning, project evidence, navigation, and contact. This skill is self-contained; neither source needs to be fetched during a normal review.


## License notice

MIT License

Copyright (c) 2026 Karl Koch

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
