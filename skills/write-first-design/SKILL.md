---
name: write-first-design
description: >
  Use before designing or building UI features, refactors with product impact,
  or exploratory AI implementation work. Trigger when requirements are fuzzy,
  when someone jumps straight to Figma/code, or when a change lacks a written
  hypothesis and rationale. Forces prose decisions before pixels or implementation.
license: MIT
---

# Write-First Design

Decide in writing before opening the design file or generating the implementation. Prose exposes weak thinking while changes are still cheap.

## Defaults

1. Write a hypothesis before mockups or code.
2. Pair every meaningful visual/product change with a reason.
3. If a change cannot be explained in a sentence, cut it.
4. Prefer short decision docs over long slide theatres.
5. Keep the writer close to the builder to avoid handoff translation loss.

## Hypothesis shape

```text
We believe [change]
will produce [outcome]
because [reason].
```

If that sentence cannot be written, the problem is not understood well enough to design.

## Artefacts

1. **Discovery** — goal, why now, success criteria, hypothesis.
2. **Direction** — proposal, alternatives considered, change log with reasons.
3. **Build notes** — what is in scope, what is explicitly out.
4. **Mid-mortem / postmortem** — predicted vs actual, what to keep next time.

## Prefer / Reject

| Prefer | Reject |
| --- | --- |
| Written rationale before pixels | Designing until the file becomes the plan |
| Testable outcomes | Vague "improve UX" goals |
| Cutting unexplained changes | Shipping preferences dressed as decisions |
| Async-readable docs | Decisions that only exist in a meeting memory |

## Review checklist

- [ ] Is there a hypothesis in the required shape?
- [ ] Is success specific enough to evaluate later?
- [ ] Does each major change have a written reason?
- [ ] Are non-goals explicit?
- [ ] Could a teammate disagree with the argument without needing the mockup?
- [ ] Is the doc short enough that people will finish it?

## Source essays

- Write-first design
- Falling in love with the build
- Design for handshakes, not handovers
