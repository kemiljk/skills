---
name: design-engineering
description: "Connect Figma design intent to implementable component behavior, tokens, and production requirements."
license: MIT
---

# Design Engineering

Work within the selected or named scope and the user's request. Review requests produce findings without edits; implement changes when requested. Use available context, disclose inaccessible evidence, and preserve unrelated work.

Design engineering shares responsibility for the interface people use. Reduce translation loss by bringing implementation constraints into design decisions early.

## Start from the actual product

Read the supplied brief, selected surface, existing components, and available variables. Infer routine choices from the product. Ask only when an unresolved decision changes the work materially.

Reuse the system before inventing new structures. Preserve instance relationships and naming conventions where possible. Do not restructure an entire library to solve a local screen problem.

## Translate deliberately

| Figma concept | Implementation intent |
| --- | --- |
| Auto layout and resizing | Content flow, flex/grid constraints, wrapping, overflow |
| Components and variants | Component boundaries, properties, state |
| Variables and styles | Semantic tokens and theme behavior |
| Prototype connections | Navigation, state transitions, cancellation |
| Repeated spacing and alignment | Component defaults that survive content changes |

These are mappings to decide, not guarantees of automatic code conversion. A frame may describe a visual group without needing a new production component.

## Encode the contract

- Separate content, appearance, and interactive state in component properties when it improves reuse.
- Explain which values are semantic tokens and which dimensions respond to content or available space.
- Design meaningful loading, empty, error, disabled, and success states alongside the normal path.
- Include keyboard/focus and reduced-motion requirements, with touch behavior for essential actions.
- Resolve wrapping, overflow, long text, and compact layouts before calling the design complete.
- Document consequential tradeoffs next to the affected design or in the response, using the existing team format.

## Design and Make

In Figma Design, express intent with editable structure, component variants, variables, and targeted prototype connections. Make behavior that cannot be represented explicit in concise annotations.

In Make, translate the intent into real web state, semantic controls, responsive layout, and meaningful feedback. Use the existing implementation system when available. Verify the component behavior in the preview rather than assuming a matching screenshot means a successful translation.

Treat prototype interactions, simulated data, and browser behavior as evidence only for what they actually demonstrate. They cannot prove production authorization, persistence, performance, or native platform accessibility.

## Deliver

Explain the decisions that reduce ambiguity for the builder: component/state mapping, layout behavior, reused tokens, and remaining runtime requirements. Keep the explanation proportional to the change.

Report the requested design or implementation, the checks performed, and the remaining uncertainty. Shared quality continues through implementation; visual completion alone is not a production sign-off.

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
