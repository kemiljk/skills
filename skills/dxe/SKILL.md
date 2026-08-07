---
name: dxe
description: >
  Master DXE design-engineering pass that applies the full kemiljk/skills suite to a
  repository or UI surface. Use when the user asks for dxe, DXE, a design-eng pass,
  "apply all skills", repo-wide interface review, ship-ready hardening with Karl Koch
  design taste, or composing write-first, subtractive, semantic, fluid, delight, and
  production checks at once.
license: MIT
---

# dxe

One invocation. Full suite. Apply every skill in this collection to the target repo (or scoped paths) in precedence order.

## Required setup

All sibling skills from `kemiljk/skills` must be installed. Before work, **read each skill's `SKILL.md`** (and linked `references/` only when that phase needs depth):

| Phase | Skills to read |
| --- | --- |
| 1. Intent | `write-first-design`, `subtractive-design` |
| 2. Platform | `semantic-html-first`, `modern-css-html` |
| 3. Feel | `fluid-design`, `interface-affordances`, `product-delight` |
| 4. Bridge | `design-engineering` |
| 5. Shipping | `ai-output-judgement`, `prototype-to-production` |

If a skill is missing, stop and tell the user which install is needed. Do not invent a substitute.

## Invocation shapes

- **`dxe`** / **design-eng pass** / **apply all skills** — full repo (or workspace) pass
- **`dxe <path>`** — scope to that file/directory
- **`dxe review`** — findings only; do not edit
- **`dxe fix`** — findings then implement high-confidence fixes

Default: review + propose fixes; only write code when the user asked to fix/apply/ship, or chose `fix`.

## Workflow

Copy and track:

```text
dxe pass:
- [ ] 0. Scope & materials map
- [ ] 1. Intent (write-first, subtractive)
- [ ] 2. Platform (semantic HTML, modern CSS/HTML)
- [ ] 3. Feel (fluid, affordances, delight)
- [ ] 4. Bridge (design-engineering)
- [ ] 5. Shipping (AI judgement, prototype→production)
- [ ] 6. Report & next actions
```

### 0. Scope & materials map

1. Identify the target: whole repo, app package, or given paths.
2. Map stack (framework, styling system, component primitives, motion library).
3. Prefer existing tokens, primitives, and patterns over inventing new ones.
4. List primary user tasks the UI must support (for subtractive and affordance checks).

### 1. Intent

From `write-first-design` + `subtractive-design`:

- State the hypothesis for what this pass is improving (or note if the product already has one).
- Mark unexplained chrome, duplicate actions, and generative residue for removal.
- Prefer fewer decisions per screen; cut what cannot earn its place in one sentence.

### 2. Platform

From `semantic-html-first` + `modern-css-html`:

- Native elements before `div`+ARIA theatre.
- Native CSS/HTML features before JS/CSS hacks when support is acceptable.
- Pseudo-classes and real disabled/open/invalid states over parallel `data-*` shadow systems.

### 3. Feel

From `fluid-design` + `interface-affordances` + `product-delight`:

- Continuous, interruptible motion where interaction needs physics; not decoration.
- `fluid-design` owns feel; `modern-css-html` owns the most native implementation that can deliver it.
- Affordance cues must match real behaviour; no hover-only critical actions.
- Delight = anticipation, reliability, care — not novelty for its own sake.

### 4. Bridge

From `design-engineering`:

- Map design structure to code structure deliberately.
- Keep taste attached to materials (tokens, rendering, a11y), not handoff documents alone.

### 5. Shipping

From `ai-output-judgement` + `prototype-to-production`:

- Treat median AI output as scaffolding; name concrete failures.
- Harden happy paths: empty/error/loading, auth, focus, reduced motion, stable identity, real validation.
- Remove demo-only shortcuts before calling it done.

## Conflict rules

When skills disagree, resolve in this order:

1. **Intent** beats decoration (`subtractive-design` / write-first rationale).
2. **Correct semantics & accessibility** beat visual convenience.
3. **Feel** (`fluid-design`) decides how interaction should behave; **platform** (`modern-css-html`) picks native implementation; JS/Motion/SwiftUI only when CSS cannot express interruption, velocity, or gesture continuity.
4. **Production trust** beats prototype cleverness.

## Output format

Deliver a single report:

```markdown
# dxe pass — [repo or scope]

## Hypothesis
We believe [change] will produce [outcome] because [reason].

## Findings
### Critical
- [skill] path — issue — fix

### Should fix
- …

### Nice to have
- …

## Cuts (subtractive)
- …

## Proposed changes
1. …
```

Quote exact snippets for violations. Tie each finding to a skill name. Prefer system tokens and existing primitives in fixes.

## Prefer / Reject

| Prefer | Reject |
| --- | --- |
| Reading every sibling `SKILL.md` then acting | One mega-prompt of vague taste |
| Phase-ordered pass with a checklist | Random drive-by nits |
| Specific, path-anchored findings | "Make it nicer" |
| Scoped edits that match stack materials | Rewrites that ignore the design system |
| Review-only unless asked to fix | Silent mass refactors |

## Done when

- [ ] Every phase checklist above was considered
- [ ] Findings reference skills by name
- [ ] Critical a11y/semantics/production gaps are called out or fixed
- [ ] Subtractive cuts are explicit
- [ ] Remaining work is ordered by severity
