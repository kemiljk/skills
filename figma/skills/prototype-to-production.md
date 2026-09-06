---
name: prototype-to-production
description: "Identify and address production gaps in a Figma concept or Make prototype, including failure, accessibility, and real data boundaries."
license: MIT
---

# Prototype to Production

Work within the selected or named scope and the user's request. Review requests produce findings without edits; implement changes when requested. Use available context, disclose inaccessible evidence, and preserve unrelated work.

Keep what the prototype taught you and replace its shortcuts. A successful happy path establishes possibility, not readiness for real users.

## Establish the boundary

Identify the intended release surface and what access is actually available. Distinguish a Figma Design specification, a running Make prototype, and production services. Inventory simulated data, interactions, authorization, persistence, and external dependencies.

Work within the requested scope. Publishing, configuring production services, and changing external accounts require authorization; a hardening request is not a reason to invent or silently activate them.

## Hardening priorities

| Prototype shortcut | Required production behavior |
| --- | --- |
| Ideal mock content | Loading, empty, long content, large lists, partial failure |
| Hidden controls presented as permissions | Real server-side authorization |
| Success-only form | Validation, pending state, recoverable errors, preserved input |
| Reordered items lose state | Stable identity and clear ownership |
| Disconnected styling | Existing semantic tokens and responsive rules |
| Pointer-only interaction | Keyboard, touch, focus, and reduced-motion paths |

Keep state transitions intelligible. Define cancellation, retry, repeated activation, and what happens when leaving and returning to the flow.

## Figma Design work

Inspect and complete the affected component states, responsive examples, copy, focus requirements, and recovery paths. Annotate server-side and persistence requirements without pretending to implement them in a frame.

Keep the deliverable useful for implementation: identify the user trigger, expected outcome, failure behavior, and unresolved dependency. A fully connected prototype remains a specification of behavior.

## Make work

Inspect the available implementation and running behavior. Replace demo shortcuts within the accessible code: native controls, stable identity, validation, meaningful async states, and tokenized layout.

Check critical flows against representative zero/large data and slow or failed responses when supported. Inspect focus management for dialogs and menus. Keep credentials out of client code and never treat a client-only guard as authorization.

If a service, test environment, or production configuration is unavailable, deliver the concrete local improvements and name the dependency. Do not fabricate successful integration or security testing.

## Completion evidence

Separate completed changes, observed runtime checks, and remaining release blockers. Prioritize blockers by the user harm they cause rather than producing an indiscriminate checklist.

A build or preview is not proof of secure permissions, persistence, performance, accessibility, or native platform behavior. State the relevant unverified requirements plainly and leave a maintainable result that does not depend on the prototype narration.

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
