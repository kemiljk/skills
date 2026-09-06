---
name: dxe
description: "Review a Figma Design flow or Figma Make interface for design engineering quality. Use for a DXE pass; apply bounded fixes when requested."
license: MIT
---

# DXE — Karl Koch

Run a design-engineering pass on the selected or named interface. This skill contains its own rubric; no other skills need to be installed.

## Establish scope

Infer the primary user task, target platform, selected frames or named flow, existing system, and requested outcome from the chat and available context. Ask one focused question only when missing context blocks useful work. If the selection is unavailable, say so and request the target instead of claiming to inspect it.

Use attached frames, existing components, variables, styles, Make guidelines and kit components as the starting materials. Retrieve only the specific linked brief or design-system section needed, through an available connector. Missing connectors are a context limit, not a reason to invent requirements.

Default to review with findings in chat and no canvas or code edits. A request to fix permits bounded changes in the named scope; preserve unrelated frames, components, content, and behaviour. Do not publish libraries, skills, or sites as part of a pass.

- **Quick:** one representative screen and its primary action.
- **Review:** representative primary flow, detail/list, form, overlay, and available failure states; state omissions.
- **Fix:** review, implement justified corrections, repeat affected checks.
- **Exhaustive:** enumerate and inspect all accessible screens and states in the requested scope; disclose anything inaccessible. This expands coverage, not dependencies.

## Match the evidence to the surface

**Figma Design:** inspect actual layers, auto layout, resizing, component instances/variants, variable bindings, text, and prototype connections where available. Compare primary and contrasting frame sizes. A drawn focus ring or linked prototype demonstrates intent; it does not establish DOM semantics, screen-reader support, native behaviour, or production readiness.

**Figma Make:** inspect available source and rendered preview. Exercise the primary task, a failure/recovery path, narrow and wide layouts, keyboard focus, and reduced motion when supported by the environment. Use the project's existing components and guidelines. Report checks you cannot execute. A web preview of an iOS or Android design is still web runtime evidence.

## Review in order

1. **Intent.** State the job in one sentence. Check that the hierarchy, labels, and primary action help complete it. Preserve useful density. Identify duplicated actions, unexplained chrome, and generic generated content; cut only where comprehension improves.
2. **Platform.** Check reading order, visible labels, control roles and states, focus intent, error association, and alternatives to gestures. For web implementation, prefer real links, buttons, fields, and native disclosure/dialog behaviour. For Apple or Android targets, specify native navigation, controls, insets, text scaling, and input contracts; leave runtime validation to that platform.
3. **Feel.** Make actions discoverable across relevant inputs. Preserve continuity when views change. Gestures need cancellation and alternatives; repeated input should not queue obsolete motion. Provide reduced-motion behaviour without losing meaning. Add delight only where it improves feedback, anticipation, or care.
4. **Bridge.** Trace recurring patterns to existing components and semantic variables. Prefer auto layout and deliberate resizing over fragile fixed positioning. Check long labels, large text, narrow widths, and variant/state coverage. Explain the mapping to implementation without assuming a layer name creates semantics.
5. **Trust.** Inspect available loading, empty, error, invalid, disabled, and permission states. Distinguish simulated data and actions from real persistence or authorization. Check recovery and repeat use where executable. Identify concrete generated residue rather than rejecting work merely for looking AI-assisted.

Choose depth from observed problems. Do not force a finding in each phase or redesign working patterns to match personal taste.

## Report and act

Give a compact report with scope, primary task, evidence inspected, strengths to preserve, prioritized findings, useful cuts, and verification limits.

For each finding, name the frame/layer/component or source location, user consequence, smallest useful correction, and confidence:

- **Confirmed design:** directly observed in canvas structure or appearance.
- **Confirmed runtime:** reproduced in a runnable preview with the input sequence noted.
- **Confirmed source:** visible in code; runtime effect not yet established.
- **Likely / unverified:** needs the named decisive check.
- **Environment only:** missing tool or service without established product impact.

Prioritize task blockers and confirmed serious failures, then comprehension/recovery issues, then optional polish. Never describe an unverified suspicion as a confirmed blocker.

In fix mode, apply related changes together to the smallest responsible component or frame. Reinspect edited states and contrasting sizes; exercise changed behaviour where possible and wait for transitions to settle. Summarize what changed, what was verified, and what remains unproven. If a check is unavailable, report that limit instead of claiming completion of it.

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
