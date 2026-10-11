---
name: intentional-craft
description: "Develop or refine ideas in Figma Design or Make through Apple's Intention film, connecting a human outcome to focused scope, component behaviour, and evidence of craft."
license: MIT
---

# Intentional Craft

Make the intended human experience a decision criterion from the first idea through the working result. This skill translates Apple's 2013 *Intention* film into contemporary design engineering practice. It does not prescribe an Apple visual style or claim to document Apple's internal process.

This edition is self-contained. The working method below is an editorial interpretation, not instructions quoted from Apple. Source context is included below.

## Establish the intention

Infer the person, task, context, and constraints from the request and available work. Identify the practical outcome and the feeling it should support. Confidence, agency, relief, curiosity, or connection may fit; surprise is not desirable in every task.

Turn the feeling into an observable design promise. For example: someone finishing an important edit should know whether it is saved and how to recover if saving fails. Emotional intent without a behaviour that supports it is too vague to guide the work. Do not claim to have measured a feeling through a screenshot or a passing test.

Use the existing brief when it supplies this direction. Ask only when an unresolved choice would materially change the result. Scale the method to the task; a precise local edit does not require a new manifesto.

## Work in the available medium

**Figma Design:** inspect the named frames, components, variants, variables, auto layout, and prototype connections. Express the intended behaviour through editable structure, representative states, and concise annotations for runtime requirements. Preserve useful instance relationships. A prototype can demonstrate a proposed flow; it cannot establish real persistence, recovery, accessibility, or performance.

**Make:** inspect the available source and rendered preview. Reuse existing components, tokens, and conventions. Exercise changed behaviour with representative content, relevant input methods, and failure states where available. Distinguish simulated behaviour from working services. Report unavailable checks.

Stay within the named scope. Review requests produce findings; requests to improve or implement authorise scoped changes.

## Choose what deserves attention

Evaluate an idea against the intended experience, its frequency or consequence, and the cost of building and maintaining it. Prefer a coherent experience that fulfils the task over a larger set of incomplete promises.

For material choices, explain what earns inclusion and what can be deferred. A useful rejection names the competing user benefit, attention cost, or complexity it avoids. Do not manufacture a quota of rejected ideas or remove a requirement to make the result look simpler.

Compare the strongest plausible approaches when the choice is genuinely open. Keep the user's platform, brand, useful information density, and established conventions. More options can help experts; fewer options can obstruct them. Judge the quality of choice by what people can understand and accomplish.

## Carry the intention into construction

Trace the human promise into the design and engineering decisions that make it credible:

| Intended experience | Supporting decisions | Evidence to seek |
| --- | --- | --- |
| Confidence that work is safe | Accurate saving states, preserved input, and recoverable failures | Observe a successful save and an interrupted or failed save |
| Agency during a long operation | Understandable progress, cancellation where feasible, and an honest account of partial effects | Interrupt the operation and inspect the resulting state |
| Clarity when choosing | Meaningful labels, comparable information, and a useful default where appropriate | Walk through a representative decision using real content |
| Continuity across a task | Stable identity, retained context, and consistent state meanings | Leave and return, resize, or change input method as relevant |

These are examples, not mandatory features. For an API, workflow, or architecture idea, make the same connection through understandable contracts, predictable failure behaviour, and the effort imposed on its consumers. Internal elegance earns its place when it supports useful behaviour or maintainable delivery.

Inspect the seams: input to feedback, local state to persisted state, one screen to another, and a component to its other uses. Typography, layout, copy, motion, semantics, and runtime behaviour should support the same promise. Spend effort where a mismatch has a meaningful effect; invisible implementation complexity is acceptable when it makes use simpler and remains maintainable.

## Refine with a purpose

Prototype the uncertain experience before investing in a large implementation. Exercise the central task with representative content and the conditions most likely to challenge the promise. Change the responsible design or implementation, then recheck that task.

Simplify actual effort, ambiguity, or fragility. Retain labels, affordances, confirmation, and recovery when people need them. Restart a direction when evidence shows its premise is wrong; do not discard sound work because a new aesthetic is more exciting.

Allocate refinement by consequence and uncertainty. Stop when the agreed outcome is supported, the relevant checks pass, and further changes offer little benefit within the task's constraints. Record consequential limits rather than implying perfection.

## Deliver an accountable result

Match the deliverable to the request. An ideas request should receive concrete proposals, tradeoffs, and the cheapest useful experiment. A review should receive evidence and recommendations. An implementation request should receive scoped changes and verification.

Explain the intended experience, the consequential decisions, and the evidence that supports the result. Distinguish what was observed from what remains a hypothesis. For any reported bug, give a credible consumer use case, prerequisites and reproduction steps, expected and actual behaviour, and impact; do not claim reproduction without executing it.

Readiness means meeting the task's quality bar with honest evidence. It does not authorise publication or deployment.

## Source context

Research checked 11 October 2026. Karl supplied [this WWDC 2013 opening film](https://www.youtube.com/watch?v=XAEPqUtra6E). Contemporaneous [MacStories coverage](https://www.macstories.net/news/apple-posts-wwdc-2013-keynote-ios-7-designed-by-apple-videos/) and [MacDailyNews coverage](https://macdailynews.com/2013/06/11/new-apple-video-describes-what-goes-into-creating-each-apple-product-with-video/?noamp=mobile) reproduce the on-screen copy and identify the film as *Designed by Apple – Intention*.

The supplied upload was identified through its indexed title; no frame-by-frame inspection, exact typographic line breaks, or timestamp verification is claimed. Published transcriptions underpin this interpretation. The complete copy is linked above rather than reproduced here.

In sequence, the film questions broad production, separates quantity from a rewarding experience, establishes emotional intention, describes selective and patient refinement, and ends with responsibility for human benefit. The software practices and stopping criteria in this skill are our translation, not a documented Apple development process. Its original instructions use the MIT licence; the film and linked material retain their own rights.


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
