---
name: modern-css-html
description: "Choose native CSS and HTML features, assess browser support, or replace legacy workarounds with progressive enhancement."
license: MIT
---

# Modern CSS & HTML

Write CSS and HTML with current platform features. Prefer native materials over legacy hacks and unnecessary JavaScript.

## Composition with other skills

- This skill owns **native implementation choices**.
- `fluid-design` owns **interaction feel** when physics, interruption, or gestures exceed CSS.
- `semantic-html-first` owns **element and ARIA boundaries**.
- If a native CSS/HTML feature can meet the requirement with acceptable support, use it.

## Browser support policy

Target features available in both **WebKit (Safari)** and **Blink (Chrome/Edge)** unless the task explicitly allows a single-engine experiment.

- **Widely available in both engines:** ship as default.
- **Newly available in both:** ship with `@supports` / progressive enhancement.
- **Single-engine or unstable:** mention as optional; provide a cross-engine path.

Do not hardcode volatile global percentage figures in recommendations. Re-check support when unsure, and encode the decision as "both engines / enhance / fallback".

## Core defaults

### HTML

- Use native elements (`button`, `a`, `details`, `dialog`, `select`, form controls) before ARIA widgets.
- Prefer semantic structure (`main`, `nav`, `section`, headings) over div soup.
- Use Popover API + CSS Anchor Positioning before custom floating stacks when support allows.

### Layout

- `gap` over margin hacks; `inset` over four physical offsets; `aspect-ratio` over padding hacks.
- `100dvh` for mobile full-height; logical properties for direction-aware spacing.
- Container queries for component responsiveness; range syntax for media queries.
- `subgrid`, `grid-template-areas`, `position: sticky`, scroll snapping when they replace JS.

### Colour and theme

- Build palettes in `oklch()`.
- Derive states with `color-mix()` and relative colour syntax.
- Prefer `light-dark()` with `color-scheme` over duplicated scheme blocks.

### Motion

- Animate `translate`, `rotate`, `scale`, and `opacity` preferentially.
- Use `@starting-style` and `transition-behavior: allow-discrete` for entry/exit where supported.
- Prefer CSS scroll-driven timelines over Intersection Observer class toggles when support allows.
- Defer to `fluid-design` for springs, gestures, and interruptible physics.

## Review checklist

- [ ] Is there a native HTML element for this control?
- [ ] Can layout/colour/motion be done in CSS without a library?
- [ ] Are colours tokens/`oklch` rather than one-off hex?
- [ ] Are fallbacks expressed with `@supports` where needed?
- [ ] Does reduced-motion get a real alternative path?
- [ ] Are physical left/right properties avoided for direction-sensitive UI?
- [ ] If JS remains, is it covering a gap CSS/HTML cannot?

## References

- Read [Task recipes](references/recipes.md) when implementing a matching pattern.
- Read [Feature notes](references/features.md) when choosing a feature or fallback.
Load only the reference relevant to the current decision.
