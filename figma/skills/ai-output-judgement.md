---
name: ai-output-judgement
description: "Critique generated Figma designs or Make output for concrete quality problems when asked to review AI work."
license: MIT
---

# AI Output Judgement

Work within the selected or named scope and the user's request. Review requests produce findings without edits; implement changes when requested. Use available context, disclose inaccessible evidence, and preserve unrelated work.

Treat generated output as a draft that needs specific judgement. Fix the last mile by naming failures in hierarchy, tokens, semantics, state, motion, and product fit.

## Establish the evidence

Work on the selected frame, component, flow, or Make surface. Read the supplied brief and nearby product context before treating a default as a mistake. Preserve deliberate brand choices.

In Figma Design, inspect editable layers, component properties, variables, layout rules, and prototype connections when available. A screenshot alone cannot establish those properties. In Make, inspect the implementation as well as the running preview when available.

## Review and revise

1. **Meaning:** Do labels and controls communicate the actual task? Is copy specific to this product?
2. **System:** Replace disconnected repeating colors, spacing, type, and elevation with existing styles or variables. Avoid inventing a second system.
3. **Hierarchy:** Identify generic padding, shadows, radii, decorative cards, and equal-weight actions that weaken the intended reading order.
4. **States:** Include the relevant focus, disabled, loading, empty, error, selected, and recovery states.
5. **Motion:** Establish what persists between states and whether users can interrupt or reverse the interaction.
6. **Fit:** Compare with neighboring product surfaces, including narrow layouts and long content.

In Make, also inspect native control elements, accessible names, stable list identities, state resets, and overly broad transitions. A polished preview can conceal an inaccessible control or a list that loses edits when reordered.

## Deliver

Anchor each finding to the frame, component, or observed interaction. Explain the consequence and smallest useful change. Apply revisions when requested; a critique alone should remain a critique.

Prefer “use the existing spacing variable and align this label with the field” to “make it nicer.” Defend the defaults that remain as deliberate decisions.

Report what was inspected and what was actually exercised. Design annotations express accessibility and runtime requirements; they do not prove those requirements work. Keep human judgement on the path to publication.

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
