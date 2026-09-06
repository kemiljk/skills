---
name: fluid-design
description: "Design or refine gestures, springs, and motion continuity in Figma prototypes or runnable Make interactions."
license: MIT
---

# Fluid Design

Work within the selected or named scope and the user's request. Review requests produce findings without edits; implement changes when requested. Use available context, disclose inaccessible evidence, and preserve unrelated work.

Make interaction feel continuous. The same object should retain its identity as the user moves, releases, reverses, or changes direction.

## Define the interaction

Identify the acted object, resting states, input method, boundaries, cancellation, and what should survive the transition. Use motion to explain that relationship, not to animate every layer equally.

- Prefer direct manipulation when the object can reasonably be grabbed; retain a visible non-gesture alternative.
- Track a drag directly, then settle using release velocity and offset together.
- Allow user-triggered motion to reverse or redirect from its current state.
- Use progressive resistance to communicate boundaries.
- Let the acted object lead, surrounding layout adapt, and the system settle.
- Preserve shared identity across reflows and navigation when the object persists.

## Figma Design

Use consistent layer identity, relevant component variants, and available prototype transitions to illustrate continuity. Specify the trigger, destination, interruption expectation, and cancellation outcome.

Do not label a timed transition as proof of velocity inheritance, spring physics, or interruptibility. When prototype capabilities cannot express the required behavior, show the key states and annotate the runtime requirement. Avoid inventing prototype features that are not available.

## Make implementation

Use CSS transitions for simple color and opacity changes. Prefer transforms and opacity for interactive motion, and avoid broad `transition: all` declarations.

Use a suitable gesture or animation implementation when the requirement needs velocity-aware release, spring physics, or interruption that CSS cannot express adequately. Keep user control and stable state ahead of choreography. Do not add a library solely for a cosmetic easing change.

Springs around stiffness 200–400, damping 20–30, and mass 0.8–1.2 can be starting points in systems with those parameters; tune by observed response and do not copy values between engines as equivalent physics. Choose layout animation techniques according to actual rendering cost.

For dense hover surfaces, prevent fast pointer sweeps from producing distracting repeated engagement while preserving deliberate hover responsiveness.

## Input and reduced motion

Design touch without hover dependence and keep the same task operable by keyboard. Reduced motion should retain content, hierarchy, feedback, and controls through quieter opacity, color, or immediate state changes where appropriate.

## Verify

In Design, inspect the illustrated states and exercise supported connections. In Make, test reversal mid-motion, repeated activation, fast and slow releases, edge behavior, keyboard operation, and reduced motion when the environment permits.

Report illustration separately from observed runtime behavior. A smooth recording does not establish gesture cancellation, performance on other devices, or accessibility.

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
