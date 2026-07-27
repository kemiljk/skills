---
name: fluid-design
description: >
  Use whenever building interfaces that should feel physically responsive and polished.
  Trigger for springs, gestures, interruptible animation, physics-based motion, drag,
  momentum, layout animation, shared-element transitions, spatial UI, micro-interactions,
  or requests to make UI feel alive, snappy, smooth, natural, or less static. Also trigger
  for interactive components (drawers, sheets, carousels, modals, accordions, reorderable
  lists) without specified motion.
license: MIT
---

# Fluid Design

Make interfaces feel like continuous physical systems, not discontinuous state flips.

## Composition with other skills

- This skill owns **how interaction should feel**.
- `modern-css-html` owns **the most native implementation** that can still deliver that feel.
- Prefer CSS/HTML when they can express the behaviour.
- Use JavaScript/Motion/SwiftUI when you need interruption, velocity inheritance, gesture continuity, or spring physics CSS cannot express cleanly.

## Defaults

1. Prefer springs over fixed-duration easings for interactive translation and scale.
2. Every user-triggerable animation must be interruptible.
3. Prefer direct manipulation over button-only indirection when the object can be grabbed.
4. Preserve velocity across gesture boundaries (release → settle/dismiss).
5. Keep shared identity across state/route changes when the same object survives.
6. Adapt interaction models to input method (mouse, trackpad, touch, keyboard).
7. Animate layout with FLIP / `layout` / View Transitions — never `top`/`left`/`height`/`margin`.
8. Add progressive resistance at edges and rubber-banding at boundaries.
9. Sequence choreography: acted object leads, surroundings yield, then settle.
10. Provide a reduced-motion path that preserves affordances with safer alternatives.

## Prefer / Reject

| Prefer | Reject |
| --- | --- |
| `type: "spring"` for interactive motion | `transition: all` |
| CSS `transition` for colour/opacity | Animating layout properties |
| Alternate reduced-motion layouts | `animation: none !important` as the only a11y plan |
| Velocity-aware hover gating on dense surfaces | Debounced hover that feels dead, or ungated strobing |
| Transform + opacity | Long locked keyframe sequences users must wait out |

## Tuning starting points

- UI springs: stiffness `200–400`, damping `20–30`, mass `0.8–1.2`
- Layout reflow: ~`200–350ms` or a well-damped spring
- Gesture dismiss: combine offset threshold + velocity threshold
- Dense hover surfaces: EMA-smoothed velocity with separate engage/disengage thresholds

## Input and accessibility

- Desktop + motion: springs, deflection, velocity gating as designed.
- Desktop + reduced motion: keep hierarchy and controls; swap spatial physics for quieter opacity/colour/snap models.
- Touch: prefer drag/scroll metaphors over hover-dependent discovery.
- Keyboard: every interactive surface remains operable without pointer precision.

## Review checklist

- [ ] Can the user reverse or redirect mid-motion?
- [ ] Does travel distance/velocity change the motion response?
- [ ] Are only compositor-friendly properties animating for interaction?
- [ ] Does reduced motion keep the same tasks possible?
- [ ] Do list/grid reflows preserve spatial memory?
- [ ] Are hover-dense regions gated against fast pointer sweeps?
- [ ] Is JS justified because CSS cannot express the behaviour?

## References

- [Motion recipes](references/motion-recipes.md)
- [Principle notes](references/principles.md)
