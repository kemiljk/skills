---
name: interface-affordances
description: "Improve unclear actions, interaction cues, control states, and hit targets in Figma designs or Make interfaces."
license: MIT
---

# Interface Affordances

Work within the selected or named scope and the user's request. Review requests produce findings without edits; implement changes when requested. Use available context, disclose inaccessible evidence, and preserve unrelated work.

Make possible actions perceptible. A working handler is insufficient when people cannot discover what to do.

## Inspect the task

Identify the main user action and the controls within the requested surface. Compare appearance with the behavior claimed by labels, prototype links, or running interactions.

- Keep essential actions discoverable without hover.
- Match hit areas and spacing to touch, pointer, and keyboard use.
- Distinguish pressed, selected, expanded, disabled, and loading states where they matter.
- Use labels that name the action and accessible names for ambiguous icons.
- Do not make decoration look draggable, clickable, or interactive unless that behavior exists.
- Preserve clear focus indicators; selection is not a substitute for focus.

## Figma Design

Inspect component states, target bounds, labels, and prototype connections when available. The visible icon and its intended hit area can differ; make the latter explicit rather than assuming a small icon has a large target.

Reuse existing components and add only the states necessary for the scoped interaction. Annotate intended accessible names, roles, state changes, and reading/focus order. Show how an essential action remains available on touch and without motion.

If a design looks disabled, specify whether activation is blocked and how the user can understand the reason. If it shows loading, specify duplicate-activation handling and the outcome on failure.

## Make

Use semantic controls and verify the rendered role, name, keyboard behavior, focus indicator, and disabled behavior when inspectable. Hover may enrich discovery but cannot be the sole path to an essential action.

Test actual hit areas rather than judging from icon dimensions. Check that loading and disabled states affect behavior, and that expandable controls expose their state consistently with the visual presentation.

## Deliver and verify

Tie findings to specific controls. Describe the mismatch and smallest useful correction, then apply it when the user requested a fix.

Check the main path with the relevant input methods and reduced motion when possible. State whether a result is a design specification, a prototype demonstration, or tested browser behavior. Canvas appearance does not prove assistive-technology exposure or native accessibility.

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
