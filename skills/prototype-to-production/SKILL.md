---
name: prototype-to-production
description: >
  Use when turning vibe-coded demos, prototypes, or happy-path AI builds into
  production software. Trigger for shipping checklists, hardening passes, auth/a11y
  gaps, state edge cases, performance, and maintainability reviews after a fast prototype.
license: MIT
---

# Prototype to Production

Prototypes prove possibility. Production earns trust. Do not confuse a working happy path with a shippable system.

## Defaults

1. Keep the prototype's learning; replace its shortcuts.
2. Enumerate edge cases before polishing visuals.
3. Accessibility, auth, empty states, and failure paths are release requirements.
4. Prefer boring, clear state models over clever demos.
5. Measure what breaks under slow networks, large data, and repeat use.

## Hardening map

| Prototype shortcut | Production replacement |
| --- | --- |
| Mock data only | Real loading/error/empty states |
| Client-only auth theatre | Real session/permission checks |
| Happy-path forms | Validation, constraints, recoverable errors |
| Index keys / remounting tricks | Stable identities |
| Hardcoded values | Tokens and configuration |
| Desktop-only interaction | Keyboard, touch, reduced-motion paths |

## Prefer / Reject

| Prefer | Reject |
| --- | --- |
| Explicit state machines or clear state transitions | Hidden flags that only work in the demo script |
| Progressive enhancement | Single-path demos with no fallback |
| Observability and basic tests around critical flows | "We'll notice if it breaks" |
| Deleting demo-only code | Shipping scaffolding because it already exists |

## Review checklist

- [ ] What happens with zero items, huge lists, and partial failure?
- [ ] Are permissions enforced on the server, not only hidden in the UI?
- [ ] Do forms recover from invalid input and network failure?
- [ ] Is focus management correct for dialogs/menus?
- [ ] Does reduced motion still complete the task?
- [ ] Are secrets, keys, and debug hooks gone?
- [ ] Can another engineer maintain this without the prototype narration?

## Source essays

- On vibe coding vs shipping to production
- On the complexity of production codebases
- Design engineering handshake writing
