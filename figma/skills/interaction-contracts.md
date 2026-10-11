---
name: interaction-contracts
description: "Define or review interaction behaviour in Figma Design or Make, covering triggers, states, persistence, interruption, recovery, and observable acceptance checks."
license: MIT
---

# Interaction Contracts

Make the behaviour of a named interaction explicit enough that designers and engineers can build and verify the same experience. A contract describes observable promises; it does not require a state-machine library or a particular architecture.


## Figma Design and Make

**Figma Design:** inspect the named frames, component properties, variants, and prototype connections. Represent consequential states and transitions using editable components and the existing system. Annotate persistence, request cancellation, validation, and focus requirements that the prototype cannot demonstrate. Prototype execution establishes only prototype behaviour.

**Make:** inspect available source and the running preview. Connect the contract to actual controls, state ownership, and service boundaries. Exercise the affected sequences, including failures where they can be simulated honestly. Distinguish a mocked success from a confirmed service result. Report inaccessible services and checks.

Preserve instance relationships and unrelated work. Deliver the contract without edits for specification or review requests; implement only authorised changes.

## Find the unresolved promise

Use the existing brief, interface, component API, and implementation to identify the person, task, starting state, and supported inputs. Preserve established behaviour unless the task calls for changing it. Distinguish a requirement from observed behaviour and a proposed change.

Cover the consequential uncertainty, not every possible event. An already specified local edit needs only the affected promise. Ask when a missing product decision would materially change the contract; otherwise state a reasonable assumption and proceed. A request for a specification authorises a specification; implementation requires an implementation request.

## Describe the observable contract

Use a compact table, annotated flow, or the team's existing format. Include what matters for the interaction:

| Contract element | Resolve |
| --- | --- |
| Entry and trigger | Preconditions, available inputs, and what initiates the operation |
| State and feedback | What changes immediately, what is pending, and what confirms completion |
| Ownership and persistence | Where the authoritative value lives, when it is committed, and what survives leaving or returning |
| Interruption | What cancel, Escape, navigation, another input, or a second submission means where supported |
| Failure and recovery | What remains intact, how failure is explained, and how the person can continue |
| Focus and access | Control meaning, supported keyboard or assistive input, focus movement, and a reduced-motion equivalent where relevant |

Separate cancelling an edit from cancelling a request and undoing a committed change. If cancellation cannot reverse a remote effect, do not promise that it does. Optimistic feedback needs an account of failure and reconciliation. Distinguish local acceptance from server confirmation or later processing when that difference matters to the task.

Inspect plausible overlapping actions: repeated submission, editing during a pending save, leaving and returning, or an older response arriving after a newer one. Include a sequence only when supported use can reach it. Resolve which result may update the UI without prescribing an unnecessary implementation mechanism.

## Example: editing a project title

This is a hypothetical contract, not a product finding. Suppose the existing product uses explicit Save and Cancel:

| Starting state and action | Required result | Acceptance check |
| --- | --- | --- |
| Open the editor | Current title appears; committed value is unchanged | Open an existing project and inspect the input |
| Change the title, then Cancel | Draft is discarded; original title remains | Reopen and confirm the original value |
| Submit a valid title | Show pending feedback; confirm saved only after success | Observe a successful save and revisit the project |
| Save fails | Preserve the draft, explain failure, and offer a useful retry | Cause a failed save, then retry without retyping |

Decide validation, navigation during saving, and focus return from product context. Do not infer that every editor should use this save model.

## Carry the contract into the work

For design, represent the needed states and transitions and annotate requirements the medium cannot demonstrate. For code, map the contract to existing state ownership, controls, and service boundaries. Avoid replacing an architecture merely to make the specification look tidy.

Verify representative sequences against observable results. Use behavioural tests for consequential state or persistence changes; visual inspection alone cannot establish those promises. A mock service proves only the behaviour it simulates. Disclose unavailable checks and unresolved decisions.

When reporting a bug, identify the affected consumer and task, prerequisites and reproduction steps, expected and actual behaviour, and impact. Keep unexecuted concerns as hypotheses; do not report an imagined event sequence as a reproduced failure.

Deliver the requested contract, review, or scoped implementation, with the decisions made, acceptance checks performed, and remaining limits. This skill defines behaviour; it does not expand a local interaction into a whole-product hardening pass.

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
