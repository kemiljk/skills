---
name: interface-affordances
description: >
  Use when designing or reviewing controls, interactive surfaces, empty states,
  or any UI where users must understand what they can do. Trigger for affordance
  issues, discoverability problems, hover-only features, weak hit targets, or
  mismatched visual cues versus actual behaviour.
license: MIT
---

# Interface Affordances

Affordances make possible actions perceptible. If people cannot tell what they can do, the interaction is incomplete even when the code works.

## Defaults

1. Visual cues must match real behaviour.
2. Critical actions cannot depend on hover alone.
3. Hit targets and spacing should match the input method.
4. State changes should explain themselves (pressed, selected, expanded, disabled, loading).
5. Decorative motion must not impersonate an affordance.

## Prefer / Reject

| Prefer | Reject |
| --- | --- |
| Persistent cues for primary actions | Hover-only discovery of essential controls |
| Clear pressed/selected/expanded states | Identical resting and active styles |
| Cursor/keyboard/touch-appropriate targets | Tiny click areas with large visual icons |
| Disabled styles that also disable behaviour | Greyed-out controls that still fire handlers |
| Labels that name the action | Icon-only controls with no accessible name |

## Checks by input mode

- **Pointer:** hover can enrich, not gate, essential actions.
- **Touch:** provide visible tap targets and avoid hover-dependent UI.
- **Keyboard:** focus styles are part of the affordance, not an afterthought.
- **AT:** names, roles, and states expose the same possibilities the visuals claim.

## Review checklist

- [ ] Can a new user tell what is interactive?
- [ ] Does every interactive element have a perceptible state change?
- [ ] Are essential actions visible without hover?
- [ ] Do icons have names?
- [ ] Do disabled and loading states look and behave disabled/loading?
- [ ] Could reduced-motion or touch users still discover the action?

## Source essays

- On affordances
- Ten principles for product delight
- On reduced motion
