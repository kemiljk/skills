# Feature notes

Keep this file practical. Re-validate engine support before recommending newly shipping APIs as defaults.

## Safe defaults in both major engines (typical)

- Flex/grid `gap`, `aspect-ratio`, `inset`, logical properties
- Container queries, `:has()`, `:focus-visible`
- `oklch()`, `color-mix()`, `clamp()`
- Scroll snap, `position: sticky`, `object-fit`

## Progressive enhancement candidates

Confirm current WebKit + Blink support before requiring these without fallbacks:

- CSS Anchor Positioning
- Popover API combinations with anchors
- Scroll-driven animations (`animation-timeline: view()`)
- `@starting-style` / discrete transitions
- `text-wrap: balance` / `pretty`
- View Transitions for multi-page/app navigation

## Defer or gate

- Single-engine-only proposals
- Experimental syntax that still needs flags
- Anything that breaks the core task when unsupported

When gated, keep a readable non-enhanced path. Enhancement should add fidelity, not basic access.
