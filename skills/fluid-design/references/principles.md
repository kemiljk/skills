# Fluid design principle notes

Distilled from *10 Principles for Fluid UI* and follow-on essays on velocity gating, layout choreography, shared context, and reduced motion.

## 1. Physics over mechanical time

Fixed 300ms easings ignore travel distance and release velocity. Springs resolve when energy dissipates, so small nudges settle gently and fast flicks overshoot.

## 2. Interruptibility

If users can change state while motion plays, motion must reverse from the current position and velocity. Prefer spring targets and CSS transitions over locked keyframe timelines for interactive UI.

## 3. Direct manipulation

Let people drag, swipe, pinch, and reorder when the object is the control. Track 1:1 during the gesture; decide settle vs dismiss with velocity plus offset.

## 4. Velocity preservation

On release, continue with the gesture's velocity. Snapping that ignores momentum feels like toggling states instead of moving objects.

## 5. Shared continuity

When an object survives a transition, keep its identity (`layoutId`, `view-transition-name`). The design question is which element persists, not only whether to animate.

## 6. Input-method awareness

Hover physics are not touch physics. Build first-class models per context instead of stretching one interaction across devices.

## 7. Layout choreography

FLIP inverts a completed layout jump into a transform. Animate the reconciliation, not the layout properties themselves.

## 8. Progressive resistance

Boundaries should push back. Elastic drag, overscroll containment, and stronger resistance near edges communicate limits without hard stops.

## 9. Staggered choreography

Acted object responds first. Surroundings adapt second. System settles last. Equal-priority motion on every node makes busy reflows illegible.

## 10. Reduced motion as redesign

`prefers-reduced-motion` means reduce, not delete. Swap interaction models (grid, snap strip, opacity) while preserving content, hierarchy, and affordances.
