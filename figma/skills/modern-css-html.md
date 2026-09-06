---
name: modern-css-html
description: "Translate Figma web designs into native HTML and CSS choices or simplify a Make implementation with progressive enhancement."
license: MIT
---

# Modern CSS & HTML

Work within the selected or named scope and the user's request. Review requests produce findings without edits; implement changes when requested. Use available context, disclose inaccessible evidence, and preserve unrelated work.

Prefer web platform materials that express the required behavior clearly. Avoid unnecessary JavaScript and layout workarounds without sacrificing support or interaction quality.

## Choose the working mode

In Figma Design, describe implementation intent through layout rules, component states, and concise annotations. A frame cannot execute CSS or establish browser support.

In Make, implement the requirement using the available project structure and inspect the running result. Reuse existing tokens and component conventions before creating parallel systems.

## Browser support

Respect the stated browser matrix. Otherwise consider both WebKit and Blink; do not infer support from the Make preview's single engine. Verify current support using primary platform documentation or compatibility data when browsing is available.

- Supported across the required browsers: use as a normal implementation choice.
- Newly supported or uncertain: use a meaningful fallback and feature detection where appropriate.
- Limited to one engine: keep it optional unless the user requested that experiment.

If support cannot be checked, label it unverified and choose a conservative base experience. Do not use global usage percentages as a substitute for the actual target matrix.

## Implementation choices

- Start with semantic headings, landmarks, links, buttons, and form controls.
- Consider native disclosure, dialog, and popover behavior before building custom equivalents; choose according to modality and supported behavior.
- Use flex/grid, `gap`, `aspect-ratio`, and logical properties instead of positional and spacing hacks.
- Use container queries when a component should respond to its own available space. Use viewport queries when the whole page changes arrangement.
- Consider subgrid, sticky positioning, and scroll snapping when they remove custom layout code.
- Account for mobile viewport and keyboard changes in full-height layouts; `100dvh` is a candidate, not a substitute for testing.
- Reuse semantic color tokens. Consider `oklch()`, `color-mix()`, relative colors, and `light-dark()` where support and the existing theme system make them useful.
- Prefer transform and opacity for interaction motion. Consider modern entry/exit or scroll-driven CSS only with an appropriate support path.
- Use JavaScript or an animation system when gestures, velocity, or interruption require behavior CSS cannot adequately express.

## Verify and deliver

Check responsive layout, overflow, long content, keyboard operation, native states, and reduced motion in the available runtime. Verify fallbacks by exercising them where possible; `@supports` alone does not prove the fallback is useful.

Report what was implemented or specified, which browsers were actually checked, and any remaining support assumptions. A Figma design or one browser preview cannot establish cross-browser compatibility.

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
