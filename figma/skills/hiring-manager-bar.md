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

**Figma Design:** inspect named frames, text, components, variants, variables, auto layout, resizing, and prototype connections. Preserve instance relationships. Review representative desktop and narrow layouts. Follow available prototype navigation; treat focus, touch, and reduced motion as implementation requirements to verify. Static frames cannot prove working navigation, contact delivery, accessibility, or speed.

**Make:** inspect available source and the rendered preview. Check the reading path at desktop and narrow widths, with keyboard navigation and touch-compatible controls. Test reduced motion when animation gates access or comprehension. Focus checks on reaching, reading, and returning from the work, and finding contact. Distinguish simulated contact or persistence from functioning services.

Source markup and fetched text do not establish visible layout, interaction behaviour, loading speed, or accessibility. A design, preview, and live deployment may differ: identify which each observation describes. Disclose inaccessible content and checks.

Attribute supplied descriptions to the user; a described screenshot is not an inspected image or frame.

## The bar

| Hiring question | Evidence to look for |
| --- | --- |
| What are you good at, and where might you fit? | A clear introduction and selected work that supports the target role; claims connected to concrete examples |
| What did you make and ship? | Identifiable projects, enough problem and user context to understand them, visible artifacts, and honest status such as shipped, prototype, or experiment |
| What was your contribution? | Specific ownership and decisions, with collaborators and constraints where relevant; distinguish personal work from team outcomes |
| How do you work? | Useful examples of judgment, tradeoffs, collaboration, and results; enough detail to understand the work without prescribing a process-heavy case-study template |
| Can I find and understand the work? | Familiar navigation, descriptive links, legible text and images, scannable hierarchy, and core information accessible without hover or compulsory novelty |
| Can I take the next step? | Discoverable, working contact and any résumé or professional context needed for the stated goal |

For Design Engineering, distinguish product design, production implementation, and interaction refinement. Match brand work to its audience, message, and medium. Do not equate lifecycle ownership with working alone. For leadership roles, look for direction and influence where relevant; do not apply leadership criteria to every candidate.

Distinguish public screening from interview depth. Show relevant output early; select for quality and role fit over volume or prestige. Self-initiated work can lead, with honest status and ownership; it does not establish teamwork or production delivery. Match specialist depth or breadth to actual responsibilities; a broad title does not establish production engineering depth. Recognise craft without requiring elaborate motion or inferring AI authorship from familiar styling. Assess taste through reasons and user effects, and current workflow through personal decisions and checks. Preserve required CVs; employer prestige neither qualifies nor disqualifies.

Keep experiments that demonstrate curiosity or craft. Separate them only if they obscure core work. Preserve distinctive typography, writing, and interactions that support understanding; do not require a new page or generic layout. Public following, personal disclosure, and social similarity are not competence tests. Assess hosted decks by actual access and evidence.

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

Prioritize supported defects only; unavailable copy cannot establish a wording defect. Keep unrelated optional advice outside fixes; allow dependencies and safe alternatives for confirmed problems.

Do not turn personal taste into a blocker. Missing project facts need the candidate's input; code cannot establish ownership, manufacture metrics, or turn a prototype into shipped work. Respect confidentiality and accept useful qualitative evidence when numbers or public artifacts are unavailable.

## Recommend changes that can be implemented

Choose one primary category: **Discoverability** (finding work or contact), **Clarity** (understanding contribution, decisions, and evidence), **Experience** (reading and interaction effort), **Dependability** (reliable, accessible, predictable behaviour), or **Delight** (craft and personality). Categories describe what improves; priorities describe urgency. Order by impact; do not fill every category or duplicate findings. Delight can name a strength to preserve.

Present confirmed recommendations as **Category · Priority — Specific action.** Follow with concise prose covering the problem, hiring impact, and smallest useful change. Include evidence, page/frame and actual layer, component, or file when available, acceptance check, and candidate dependencies. Prefer shared fixes for repeated issues.

Use only evidenced content, design, or code changes. For URL-only reviews, name the page and element without inventing files. Prefer bounded corrections over redesigns.

For bugs, include the consumer's task, prerequisites, reproduction steps, expected and actual behaviour, and impact. Call it reproduced only after execution; prototype behaviour does not establish a production bug.

## Report and completion

Lead with **passes**, **needs changes**, or **not assessable**, scoped to the inspected pages and stated role. This judges the portfolio's ability to answer the hiring questions, not the candidate's employability. A pass needs observed support for the core questions; strong visuals do not compensate for unclear ownership. A material unanswered question means needs changes. Missing access or insufficient evidence to judge the core journey means not assessable; still report any confirmed local findings.

Keep the report compact: verdict, role assumptions, scope, limitations, strengths, then recommendations ordered by priority. Keep optional opportunities separate, categorised without a fix priority. Finish with candidate-supplied facts and remaining checks.

A review is complete when each material finding has a traceable cause and implementable recommendation, or an explicit dependency on missing facts. Do not manufacture findings for every rubric row or use numeric readiness scores.

In fix mode, implement the authorised bounded changes using existing portfolio materials. In Design, recheck affected instances, representative layouts, and prototype paths, and annotate remaining runtime requirements. In Make, run checks appropriate to the affected code and repeat the affected visitor journey. Report completed edits, verification results, and unresolved content needs. A successful build proves compilation, not comprehension or rendered behaviour.

## Sources

- [Karl Koch — The hiring manager is your user](https://karlkoch.me/writing/the-hiring-manager-is-your-user/): the core questions, clarity of contribution, and room for experimentation.
- [Won J. You — Portfolio Review](https://github.com/wonjyou/portfolio-review-skill): supplementary review areas covering positioning, project evidence, navigation, and contact.
- Dive Club: [Nad Chishtie](https://rss.com/podcasts/diveclub/2400906), [Matt Sellers](https://rss.com/podcasts/diveclub/2474921), and [Polly D’Arcy](https://rss.com/podcasts/diveclub/2774321) illustrate screening, selection, and interview depth. Their preferences are contextual. [Danny Martinez](https://www.linkedin.com/pulse/5-tips-hiring-designers-2026-danny-martinez-9wgbc) adds work-first screening and mutual evaluation.


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
