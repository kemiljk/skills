---
name: dxe-hiring-manager-bar
description: "Review a job-seeking portfolio against Karl Koch's hiring manager bar and recommend prioritized changes to site code and content. Use for portfolio readiness, hiring clarity, or a portfolio review with actionable implementation guidance."
license: MIT
---

# Hiring Manager Bar

Treat the hiring manager as a user with a job to do: find the work, understand what the candidate contributed, and decide whether their experience warrants a conversation. Creativity should help that reading. A short, specific explanation can be enough; a long case study is not a requirement.

Artifact evidence is part of that reading. Judge whether the portfolio shows enough of the work for the target role, and whether its current state is finished enough to read as a body of work. Missing context, repeated single views, and placeholder content are findings about the portfolio, not only gaps for the candidate to fill later.

## Scope

Default to review and recommendations. Implement changes only when the user requests fixes; follow any existing authorization. Preserve the site's identity, existing components, and unrelated work. When the user asks a narrow question, answer that question with the evidence it needs and keep unrelated improvements out of the findings unless a broader review is requested.

Use the stated target role, level, and review scope. If the target is unstated, make a provisional assumption from the content and identify it. Ask only when the answer would materially change the review. Do not infer seniority from visual polish or impose job-seeking requirements on a site made primarily for personal enjoyment. Side projects still need enough context and artifact evidence to be judged; assess their status and completeness as work, not as a collection of experiments.

Use relevant [Dive Club examples](references/dive-club-examples.md) for work selection, craft, side projects, and case-study depth. Use [Danny Martinez’s examples](references/danny-martinez.md) for work-first screening, taste, current practice, and role ambiguity, and [Hiring Humans](references/hiring-humans-examples.md) for candidate goals, public-work expectations, and mutual fit. Read the entries that bear on the question before citing them; multiple accounts of the same person or hire are one example, not separate evidence. When an entry says it is linked to another account, read both before drawing the conclusion.

[Design Discipline](references/design-discipline-examples.md) supplies contrasting application preferences, format/access examples, and interdisciplinary work. [Public video and podcast examples](references/video-portfolio-advice.md) cover a first management transition, concise showcases, student evidence, and brand roles. Read only what changes the current judgment: these are attributed preferences and reported examples, not a universal formula. Use the [research workflow](references/dive-club-research.md) when extending the evidence set.

## Read as a visitor, then inspect the implementation

For URL reviews, use the available browser controls. Read [Browser evidence](references/browser-review.md) when collecting rendered, interaction, or accessibility evidence.

1. Follow the ordinary entry path before using repository knowledge to fill in missing context: landing page → work listing → project → about/contact. Record what is easy to answer and where understanding breaks down.
2. Inspect representative projects that support the target role, including contrasting types of work when relevant. Name the pages sampled and omissions; do not imply a whole-site review from one case study.
3. Trace material findings to the actual routes, content entries, shared components, and styles. Check the full relevant content and linked destinations before claiming something is missing. Separate a fact that is absent from one that exists but is hard to discover.
4. When rendering is available, check the reading path at desktop and narrow widths, with keyboard navigation and touch-compatible controls. Test reduced motion when animation gates access or comprehension. Focus checks on reaching, reading, and returning from the work, and finding contact.

Source markup and fetched text do not establish visible layout, interaction behavior, loading speed, or accessibility. A local checkout and a live deployment may also differ: identify which each observation describes.

Assess hosted decks and documents by their actual access and evidence, not their format alone.

## Check the work evidence

Read for coverage before judging quality. For each inspected project, record what the page supplies: audience or user, problem or task, the candidate's contribution, artifacts, status, outcome or learning, and recency. Then record what it leaves out. When the supplied description enumerates the page's content, treat that list as the evidence. Ask about a field it never mentions; do not list it as an omission.

A single view is one view, whatever it shows. One 1440px screenshot of a finished screen can establish a final state and its composition; it cannot establish interaction, a second state, responsive behaviour, system consistency, or whether the artifact is shipped rather than a mockup. Count distinct views, not images: eight exports of the same screen are still one view.

When the same omission repeats, report it once as a systemic finding about the selection. Three projects that each have one image, a title, and no context are one portfolio-level problem with one shared fix, not three separate notes.

Separate missing facts from missing evidence:

- **Candidate facts.** Why the work was prioritised, what the candidate personally decided, who the users were, what the result was. Report the observable absence in the page, and name the fact as a dependency rather than writing it for them.
- **Artifact evidence.** A second state, a narrow viewport, a status label, a date, a working destination, or the removal of a placeholder. The candidate can add these without new information. They are confirmed findings with a bounded fix.

"I cannot write this for you" does not make the omission disappear from the review. The page still fails to answer the question; state that, then note what the candidate must supply.

Assess the current state, not the intended one. Placeholder entries, "coming soon" labels, drafts mixed with shipped work, duplicated projects, dead destinations, and inconsistent status labels are confirmed findings. They reduce what the portfolio establishes now, even when one strong project shows what the rest could be. Name the strongest project as the reason to finish the rest, not as compensation for them.

A gate you cannot pass is a limit on the review, not a confirmed portfolio defect. If the candidate can give authorised access privately, scope the gated work as not assessable and ask for that access or a permitted summary; do not infer weak work from what you cannot open.

Criticality is not inference. Name a gap only when the supplied or inspected material shows it. If the page already provides a working route or field, a second location is optional. If the description does not say whether something exists, ask; do not turn the question into a finding. A conditional improvement — "if the full summary does not already do this" — belongs in optional opportunities, not the priority list.

A hedge is not a finding. If the prose says "potential", "possible", "may", or "could" about whether the problem exists, the observation is not confirmed; verify it or move it to optional opportunities.

Explicit credits settle authorship. When the page names who did what, or credits individuals on a project, do not invent a competing owner from the employer, studio, or site name. Ask only if the page contradicts itself.

Match coverage to the role. A content, research, or brand role may need one clear final artifact and a sound explanation; a design engineering or interaction role needs enough views to show behaviour. Do not apply interaction-evidence requirements to roles that do not ask for them, and do not accept a single view as sufficient when the role is judged on the interface in use.

## The bar

| Hiring question | Evidence to look for |
| --- | --- |
| What are you good at, and where might you fit? | A clear introduction and selected work that supports the target role; claims connected to concrete examples |
| What did you make and ship? | Identifiable projects, enough problem and user context to understand them, visible artifacts early in the reading path, and honest status such as shipped, prototype, or experiment |
| Is there enough evidence to judge the work? | Context, contribution, status, and as many distinct artifact views as the target role needs; current-state content rather than placeholders or drafts |
| What was your contribution? | Specific ownership and decisions, with collaborators and constraints where relevant; distinguish personal work from team outcomes |
| How do you work? | Useful examples of judgment, tradeoffs, collaboration, and results; enough detail to understand the work without prescribing a process-heavy case-study template |
| Can I find and understand the work? | Familiar navigation, descriptive links, legible text and images, scannable hierarchy, and core information accessible without hover or compulsory novelty |
| Can I take the next step? | One findable, working contact route and any résumé or professional context needed for the stated goal |

Resolve broad titles into actual responsibilities before judging fit. For Design Engineering, distinguish product design, prototype iteration, production implementation, and refinement of an interaction. Match brand work to its audience, message, and medium, assessing these from the work and its context rather than requiring the page to state them; a brand system may demonstrate tools that help other people work, beyond a gallery of assets. Do not equate lifecycle ownership with working alone. For leadership roles, look for evidence of direction and influence where the target calls for it; do not apply leadership criteria to every candidate.

Distinguish the public screening experience from a later portfolio presentation. A concise introduction and strong artifacts can earn a conversation without a process essay. Do not demand an interview deck, exhaustive process, or every project on the public site. Preserve enough context and attribution to understand the work. Recommend deeper interview preparation only when it is in scope.

Judge selection by how well the work supports the target role, not its quantity or employer prestige. Large-company tenure is not evidence of stale thinking. A résumé can serve application requirements and experience context; its absence alone does not disqualify otherwise sufficient work evidence. A relevant self-initiated project can lead the selected work. Identify what it demonstrates and what remains unproven, such as team collaboration or production delivery. Specialist depth and breadth can both be valuable; match the evidence to the actual role. For complex product roles, connect the output to the user need, business reason, and decisions it serves.

Assess taste through specific choices, reasons, and effects on users. When workflow evidence matters, identify what the candidate framed, selected, corrected, and checked, including with AI. Tool fluency alone cannot establish production depth. A separate taste page or workflow essay is optional.

Experiments can add valuable evidence of curiosity and craft. Recommend a discoverable playground or a clearer separation only when experiments obscure the core work journey. Keep distinctive typography, writing, and interactions that support understanding. Do not require a new page or a generic portfolio layout merely to satisfy the rubric.

For explicitly requested interview or hiring-process advice, use Danny’s notes on mutual evaluation and bounded, paid collaboration. Keep an ordinary portfolio review focused on the portfolio.

## Evidence and priority

Every finding needs one evidence label:

- **Rendered:** Personally inspected pixels or a running page; name the page, viewport, and relevant state. A description of a screenshot is supplied text, not an inspected image.
- **Source:** Confirmed in a named file or content entry; visual or runtime consequences remain unverified unless separately observed.
- **Supplied:** Stated in the request or the user's description; treat it as the user's account, not as independently inspected. Name what was supplied and what still needs checking.
- **Unverified:** A plausible concern that needs a specified check. Keep it in open checks, outside the confirmed fix list.

Attribute supplied descriptions to the user; do not turn them into source inspections or rendered observations you performed. A reported failure is Supplied evidence for the report, not a reproduction.

Prioritize by the effect on the hiring questions:

- **Blocking:** Prevents reaching or understanding the core work, contribution, or contact path in the reviewed scope.
- **Should fix:** Creates material ambiguity or unnecessary effort, with a bounded correction.
- **Polish:** Improves an already understandable experience.

Apply priorities only to confirmed findings. Keep optional advice unrelated to a confirmed problem outside the fix list; unavailable copy cannot establish a wording or ordering defect. Dependencies, conditional repairs, and confidentiality-safe alternatives may accompany a supported finding without becoming separate defects.

Do not turn personal taste into a blocker. Missing project facts need the candidate's input; code cannot establish ownership, manufacture metrics, or turn a prototype into shipped work. That limits what you can write, not whether you can report that the page omits it: state the absence and name the missing fact as the dependency. Respect confidentiality and accept useful qualitative evidence when numbers or public artifacts are unavailable.

Recognize observable craft in typography, composition, copy, and interaction details. Preserve distinctive choices that help communicate ability. A restrained site can carry strong evidence; elaborate motion is optional. Familiar styling does not establish AI authorship, and use of AI does not establish weak judgment. Public following, personal disclosure, and a preferred social style are not competence tests; assess collaboration through work-relevant evidence.

## Recommend changes that can be implemented

Choose one primary category for each recommendation:

- **Discoverability:** Finding relevant work, positioning, project details, and contact information.
- **Evidence:** The coverage and completeness of work evidence: audience and problem, contribution, status, distinct artifact views, outcomes, and whether the current content is finished.
- **Clarity:** Understanding the work once its evidence is present: the contribution, decisions, and connection between claim and artifact.
- **Experience:** The effort involved in reading, navigating, interacting, and making contact.
- **Dependability:** Working links, accurate descriptions, keyboard access, and predictable behaviour.
- **Delight:** Craft, personality, and details that make an already usable portfolio memorable.

Categories describe what improves; **Blocking / Should fix / Polish** describe priority. Order recommendations by impact, not category. Use only categories supported by the findings; do not fill every category or duplicate a finding across them. Delight can also describe a strength to preserve, without requiring an embellishment.

Distinguish a review finding from advice. When the user asks what to add or lead with and has not shown the current presentation, describe the proposed evidence and its purpose without labelling an unobserved omission as a defect or assigning it a fix priority.

Present each confirmed recommendation as **Category · Priority — Specific action.** Follow with short prose connecting the observed problem, its effect on the hiring reader, and the smallest useful change. Include the evidence label, affected page and actual file/component when available, and an observable acceptance check alongside the recommendation. Include dependencies when content or assets must come from the candidate. Prefer fixing a shared component or content model when the same verified issue repeats. When the same gap repeats across projects, recommend one shared change — the card or content model, the selection, or the evidence each project must include — rather than repeating a per-project note. For thin artifact coverage, name the specific evidence to add and the question it would answer, then stop; more images are not automatically more evidence.

For example, if existing project summaries are only revealed on hover, recommend exposing those fields in the shared card's resting layout. Acceptance: a visitor can identify the project and contribution without hovering, including at a narrow viewport and during keyboard navigation. If the contribution is absent from the content, request the facts before populating it; a layout change alone does not resolve the gap.

Recommend exact content or code changes only as far as the evidence allows. For a URL-only review, identify the page and element and describe the implementation target without inventing filenames. Avoid broad redesigns when a label, content field, reading-order change, or removal of a gate solves the problem.

For a reported bug, state the concrete consumer use case, prerequisites and reproduction steps, expected and actual behavior, and impact. Only call it reproduced when the sequence was executed in the relevant medium.

## Report and completion

Lead with **passes**, **needs changes**, or **not assessable**, scoped to the inspected pages and stated role. This judges the portfolio's ability to answer the hiring questions, not the candidate's employability. A pass needs observed support for the core questions; strong visuals do not compensate for unclear ownership. A material unanswered question means needs changes. Missing access or insufficient evidence to judge the core journey means not assessable; still report any confirmed local findings.

Keep the report compact:

1. Verdict, role assumptions, scope, and evidence limitations.
2. Work evidence coverage: for each inspected project, what is present and what is missing; report a shared gap once.
3. Specific strengths to preserve.
4. Recommendations ordered by priority, with **category · priority — action** headings and supporting evidence, hiring impact, change, and acceptance checks.
5. Optional opportunities, if useful: use category headings without a fix priority and distinguish suggestions from observed defects.
6. Candidate-supplied facts and remaining verification, if any.

A review is complete when each material finding has a traceable cause and implementable recommendation, or an explicit dependency on missing facts. It also needs a coverage statement for each inspected project. Do not manufacture findings for every rubric row or use numeric readiness scores.

In fix mode, implement the authorized bounded changes using existing site materials. Run the checks appropriate to the affected code and repeat the affected visitor journey. Report completed edits, verification results, and unresolved content needs. A successful build proves compilation, not comprehension or rendered behavior.

## Sources

- [Karl Koch — The hiring manager is your user](https://karlkoch.me/writing/the-hiring-manager-is-your-user/): the core questions, clarity of contribution, and room for experimentation.
- [Won J. You — Portfolio Review](https://github.com/wonjyou/portfolio-review-skill): supplementary review areas covering positioning, project evidence, navigation, and contact. This skill is self-contained; neither source needs to be fetched during a normal review.
