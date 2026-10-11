---
name: design-system-evolution
description: "Decide how an existing Figma Design library or Make component system should evolve through reuse, composition, variants, contract changes, and bounded migration."
license: MIT
---

# Design System Evolution

Evolve a system through representative use. The goal is a clearer shared model that supports real consumers, with an understandable cost of adoption.


## Figma Design and Make

**Figma Design:** inspect main components, representative instances, properties, variants, variables, and overrides. Check how the proposed change affects existing instances, content, and resizing. Preserve useful instance relationships; do not detach instances to conceal an incompatible library change. Make property and token meanings explicit.

**Make:** inspect component APIs, tokens, and representative consumers in available source and preview. Exercise affected behaviour and inspect defaults, valid combinations, and layout changes. Design naming and code naming may differ while their meanings agree.

A frame or library definition cannot prove runtime compatibility, accessibility, or correct persistence. Record the intended contract and remaining implementation checks. Publishing a library or deploying a preview requires the corresponding authorisation; an evolution proposal alone does not provide it.

## Establish the pressure to change

Inspect the named pattern, existing component and token definitions, documentation, and representative consumers. Include contrasting uses when they reveal different content, behaviour, platform, or density requirements. Record what is shared, what differs, and which differences are intentional. State the sample; do not imply every consumer was inspected.

Identify the problem before proposing consolidation: repeated workarounds, an API that cannot express a valid use, inconsistent meanings, or a new product requirement. Visual similarity alone is insufficient evidence that two things should share a component. A one-off layout difference may belong in composition rather than a new system primitive.

Preserve working conventions and unrelated components. A proposal request produces a proposal. Implement and migrate only the authorised scope; do not turn a screen correction into a library rewrite.

## Choose the smallest useful system change

| Option | Prefer when | Check before choosing |
| --- | --- | --- |
| Reuse as-is | The existing contract supports the task | Is the apparent mismatch actually content or misuse? |
| Compose existing pieces | The arrangement varies, but the parts retain their meanings | Can the layout live outside the shared primitive? |
| Add a property or variant | A meaningful, coherent difference recurs or meets a concrete new requirement | Are allowed combinations understandable and valid? |
| Change the shared contract | The current model obstructs supported use across consumers | Which defaults, behaviours, and consumers would change? |
| Add a distinct pattern | Responsibility or interaction differs materially | Is a separate name clearer than expanding the old abstraction? |

Do not use a fixed occurrence count as permission to abstract. One consequential requirement can justify a system change; many similar screenshots can still conceal different responsibilities.

Prefer properties that express intent over a collection of styling switches. Avoid flags that allow nonsensical combinations or expose implementation details to every consumer. Allow purposeful variation rather than forcing all cards, forms, or dialogs into one visual template.

## Make the compatibility decision explicit

Map the design model to its code counterpart when both are available: variant meanings to properties, variables to semantic tokens, composition to component boundaries, and states to behaviour. The structures need not be identical; their promises should agree.

For each consequential change, account for default behaviour, existing content, interaction and accessibility contracts, themes, and platform-specific uses where affected. Distinguish source compatibility from unchanged visual or runtime behaviour. A retained property name does not guarantee the same result.

Keep migration proportional. Identify consumers to update, the old-to-new mapping, any temporary compatibility path, and the condition for removing it. Do not add indefinite aliases or deprecations when an atomic change to a small internal system is clearer. Do not promise atomic migration of consumers outside the available scope.

## Example: project cards

This is a hypothetical decision. Three cards share a title, summary, and destination, but differ in metadata placement. First investigate a common content structure with composable metadata. A selectable card that supports bulk actions may need a different interaction contract from a navigation card. Do not merge them solely because both have a thumbnail and border.

## Verify and deliver

Check representative consumers before and after the change, including a contrasting variant, realistic content, and relevant layout sizes. Exercise affected input, focus, and state behaviour in a working implementation. Check design instances and overrides when editing a library. Run meaningful compatibility or behaviour checks for changed code contracts.

Match claims to evidence: source inspection establishes API usage, a frame establishes design structure, and a running sequence establishes observed behaviour. Report unavailable consumers and checks. For any reported bug, supply the concrete consumer use case, prerequisites and reproduction steps, expected and actual behaviour, and impact; label unexecuted concerns as hypotheses.

Deliver the decision, rationale, affected consumers, compatibility implications, migration plan or completed scoped migration, and verification. Success is a system that serves its consumers more clearly, not merely fewer components or a more uniform screenshot.

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
