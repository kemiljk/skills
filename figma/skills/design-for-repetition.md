---
name: design-for-repetition
description: "Improve repeated workflows in Figma Design or Make by examining recurring effort, waiting, setup, interruption, retained context, and discoverable expert paths."
license: MIT
---

# Design for Repetition

Evaluate a workflow across repeated use, while preserving what someone needs to learn it and perform it safely. Familiarity changes the experience; it does not make everyone an expert.


## Figma Design and Make

**Figma Design:** follow available prototype paths and inspect the frames for first use, repeat use, changed context, and return from interruption. Add only the states and annotations needed to express the proposed behaviour. A linked prototype cannot prove retained settings, cancellation, or elapsed production time.

**Make:** inspect the running preview and available implementation. Exercise the repeated task and relevant interrupted returns. Check which context actually survives navigation or reload and distinguish mocked behaviour from persistence. Verify ordinary and faster paths with the relevant input methods.

Keep existing component relationships and product conventions. Do not infer user fatigue from a static design or claim a shortcut works because its label is drawn. State assumptions about frequency and disclose unavailable checks.

## Establish the pattern of use

Infer the audience, task, frequency, consequence, and conditions of interruption from the request and available evidence. Identify assumptions when usage data or research is absent. Repetition can mean several operations in one session or returning after a long gap; those require different support.

Follow the named task once before proposing shortcuts. Then inspect what repeats: setup, navigation, decisions, data entry, waiting, feedback, and recovery. Preserve the user's scope. Reviews produce recommendations; requests to improve or implement authorise bounded changes.

## Find the accumulating cost

| Recurring burden | Useful direction | Preserve |
| --- | --- | --- |
| Re-entering stable context | Suitable defaults or retained settings | Visible current context and a way to change it |
| Repeated navigation | A discoverable direct path or return position | Orientation and a usable ordinary path |
| Repeated item operations | Batch action when items share valid semantics | Item scope, partial-failure reporting, and recovery |
| Waiting for nonessential effects | Earlier access to the completed result | Truthful completion feedback and relevant explanation |
| Repeated consequential decisions | Remember safe choices or offer a suitable preset | Review where context, cost, or reversibility warrants it |
| Interrupted work | Retain the useful draft or place in the task | An account of what was saved and what remains pending |

Measure task effort, not clicks alone. An extra comparison step may reduce costly mistakes. A shorter path may demand more memory or hide the current scope. Treat timing and error observations as evidence from the sampled conditions, not universal usability results.

## Support familiarity without requiring it

Keep the primary route understandable. Add keyboard shortcuts, repeat actions, presets, or batch operations only when they solve a supported recurring need. Make faster paths discoverable and avoid moving essential actions exclusively into shortcuts or hover states.

Retain context at the appropriate boundary. Decide whether a setting belongs to a task, session, project, device, or account. A remembered destination or filter can become stale; expose it before an action when a mistaken context would matter. Do not persist sensitive or destructive choices merely to remove a step.

Distinguish harmless acknowledgement from consequential confirmation. Simplify repetitive feedback when it obstructs use, while retaining confirmation, undo, or review where the action warrants it. Never remove an established approval requirement to make a workflow faster.

Evaluate motion and celebration over repeated encounters. Useful feedback should remain legible and interruptible where appropriate. Do not assume every expressive detail becomes annoying; inspect whether it delays work, competes with attention, or still carries meaning.

## Try the repeated and interrupted paths

Use representative sequences rather than a prescribed number of loops. Check first use, a repeat with context retained, a changed context, and an interrupted return when these apply. For batch changes, inspect mixed eligibility and partial success if the real workflow supports them.

For example, a person exporting several project revisions may benefit from retained format settings and immediate access to each finished file. Verify that changing projects does not silently retain the wrong destination. This is a hypothetical scenario, not a reproduced bug.

In a working implementation, exercise changed paths with relevant input methods and realistic data. A repeated automated sequence can expose mechanical friction; it does not establish that people feel less fatigue. Seek user evidence when the decision depends on comfort or learning. Disclose checks that remain unavailable.

For any reported bug, include the affected consumer and task, prerequisites and steps, expected and actual behaviour, and impact. Separate an observed failure from a hypothesis about cumulative frustration.

## Deliver

Explain the recurring burden, the bounded change, what the ordinary path retains, and the evidence or experiment supporting the recommendation. Implement scoped improvements when requested. Stop when the identified repetition cost is addressed without hiding necessary context, weakening recovery, or expanding the workflow into a redesign.

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
