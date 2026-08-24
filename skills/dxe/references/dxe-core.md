# DXE core rubric

Use these invariants for every `dxe` pass. Sibling skills deepen a triggered lens; they do not override this precedence.

## Precedence

1. **Intent before decoration.** Know the primary task and desired outcome before judging polish. Remove only what cannot justify its effect on that task.
2. **Semantics and accessibility before visual convenience.** Native roles, state, keyboard behaviour, focus, and form participation are product contracts.
3. **Feel before technique.** Decide how an interaction should behave, then choose the simplest native implementation that preserves interruption, continuity, velocity, and input parity.
4. **Production trust before cleverness.** Failure recovery, stable state, truthful metadata, privacy, security, and maintainability outrank demo impact.

## Shared invariants

- Base judgement on source and rendered evidence appropriate to the claim.
- Preserve working systems and name verified strengths; do not create findings to fill a phase.
- Prefer native HTML before custom controls and ARIA reconstruction.
- Prefer semantic tokens and existing primitives before one-off values or parallel systems.
- Treat keyboard, touch, fine-pointer, and assistive-technology behaviour as one interaction contract.
- Motion must preserve task completion under reduced motion. Avoid broad transitions that animate unrelated properties.
- Loading, empty, error, invalid, unauthorized, and disabled states must be truthful and recoverable where relevant.
- A prototype demonstrates a path; it does not establish production readiness.
- Remove decoration, duplication, and generated residue only when the product becomes clearer or more trustworthy.
- Never infer a user-facing defect solely from framework warnings, stale servers, missing local services, or test-runner noise.

## Evidence discipline

Use the narrowest confidence label the evidence supports:

- `confirmed-rendered`: reproduced in the rendered interface or runtime output.
- `confirmed-source`: directly established by source/SSR output; rendered impact was not claimed.
- `likely`: evidence strongly indicates an issue, but a decisive check is unavailable.
- `unverified`: a hypothesis worth checking, not a finding to act on yet.
- `environment-only`: local tooling, dependency, service, or setup behaviour without confirmed product impact.

When source and runtime disagree, report both and investigate before escalating severity. A browser failure, server failure, expected local-service failure, and framework warning are different evidence classes.

## Review boundary

Review mode is observational. It may inspect files, run existing checks, and render locally when safe, but it must not edit the repository, install or update dependencies, mutate external data, or touch production. Fix mode permits only requested, bounded implementation work.

## Useful review questions

- What is the primary task, and does the visible hierarchy support it?
- What can be removed without reducing comprehension or capability?
- Does visual order match reading and keyboard order?
- Do controls expose the element, name, state, and behaviour users perceive?
- Are important actions discoverable without relying on hover?
- Does motion communicate state and remain usable when reduced?
- Do shared components uphold their contracts in every rendering mode?
- What happens with no data, partial failure, slow responses, invalid input, or missing permission?
- Do metadata, logs, and tests tell the truth about the shipped interface?
- Which existing systems are correct and must be preserved?
