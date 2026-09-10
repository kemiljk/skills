---
name: humane-functionalism
description: "Improve a Figma Design flow or Make interface through Danish functionalism, grounding hierarchy, interaction, human fit, and craft in actual use."
license: MIT
---

# Humane Functionalism

Apply Danish functionalism to the way an interface is organised, used, and experienced. Let human needs, context, construction, and perception guide its form.

The foundation is Danish architectural and product functionalism, with relevant lessons from Danish Modern furniture. These are contemporary UI applications, not a historical manifesto or rules those designers wrote for software. This edition is self-contained; historical sources are linked below.

## Start from use

Infer the primary task, audience, frequency, input methods, platform, and constraints from the request and available design or code. State the intended improvement briefly. Ask only when a missing decision would materially change the work.

**Figma Design:** inspect the named frames, auto layout, resizing, components, variables, and prototype connections. Preserve useful instance relationships. Check representative content and variants. Drawn controls demonstrate intent, not accessible semantics or production behaviour.

**Make:** inspect available source and rendered preview. Use existing components and exercise changed behaviour, including focus and recovery. Distinguish simulated success from real persistence. Disclose unavailable checks.

Review requests produce findings. Requests to improve, redesign, or implement authorize scoped changes. Preserve product requirements, brand identity, useful density, and working conventions. Fit this lens to the requested task rather than expanding a local correction into a complete redesign.

## Design through the Danish references

These connections are an editorial synthesis. Use the relevant lenses to make decisions; do not force a finding or an edit for every designer.

### Human fit — Kaare Klint

Klint's studies of proportions and existing furniture suggest a method: examine use before choosing form.

Size and arrange controls around reading, reach, dexterity, and the input method. Test real content, long labels, text scaling, and varied abilities. Preserve recognisable controls and useful shortcuts while correcting their weaknesses. A single assumed average user is insufficient.

**Check:** can the intended task be completed with the relevant inputs and content variations without clipping, precision targeting, or hidden essential actions?

### A coherent whole — Arne Jacobsen

Jacobsen's integration of architecture and interiors suggests treating the flow and its details as one designed experience.

Connect navigation, terminology, hierarchy, components, and feedback. Use the same language and state meanings from entry through completion. Check the relationship between screens before polishing an isolated component. Coherence does not require replacing platform conventions with bespoke controls.

**Check:** follow one task across screens; do labels, action priorities, focus, and state transitions remain intelligible?

### Perceptual comfort — Poul Henningsen

Henningsen's work on directing light and controlling glare makes the experienced effect a useful starting point.

Give attention a clear destination through type, spacing, grouping, and selective emphasis. Reduce competing accents and unnecessary motion. Preserve readable contrast and visible focus; a quieter screen must still communicate. Choose colour for content, identity, and conditions of use rather than a prescribed Scandinavian palette.

**Check:** can people distinguish content, actions, status, and focus at the intended viewing size? Physical glare and screen contrast are different phenomena; this is a perceptual analogy, not a lighting formula for UI.

### Organisation from activity — Vilhelm Lauritzen

Lauritzen's arrangement of buildings around their functions suggests deriving information architecture from the activities it must support.

Map the user's sequence and the decisions at each step. Place controls and information where they are needed. Separate incompatible activities; keep related ones connected. Expose location, next actions, and routes back. Include interruption, errors, and recovery in the flow.

**Check:** walk from entry to completion and through a failure. Can the user understand what happened and continue without losing work?

### Everyday usefulness — Børge Mogensen

Mogensen's work for ordinary living and production suggests investing quality in repeated, practical use.

Prioritise frequent and consequential tasks. Make defaults useful, common actions discoverable, and recovery forgiving. Support modest devices, slow connections, keyboard navigation, and assistive technology. Keep essential tasks usable without optional media or effects. Low feature count is not inherently more useful.

**Check:** repeat the common task under a relevant constraint. Does the interface still work comfortably without extra setup or avoidable waiting?

### Fit to context — Kay Fisker

Fisker's functional tradition suggests adapting useful conventions and materials to their setting.

Work with the product's existing system, platform, audience, and content. Set density and layout by the work: an expert comparison table may need many visible values; a touch form may need generous spacing. Improve proven patterns before replacing them. A visual style alone cannot establish fitness for use.

**Check:** does the proposed change solve a local problem, and what useful knowledge or capability would the change displace?

### Construction as craft — Hans J. Wegner and Poul Kjærholm

Their related Danish Modern work offers specific lessons in comfort, joinery, structure, and material properties.

Treat semantics, responsive layout, component boundaries, and state transitions as the construction of the interface. Use the platform's strengths. Repair the responsible component and check its other uses. Make loading, saved, failed, and disabled states correspond to actual behaviour. Review the points where components meet as carefully as their resting appearance.

**Check:** exercise long content, resizing, focus movement, and a failed operation. Does the construction support what the visual design promises?

## Resolve tensions through use

| Tension | Decision rule |
| --- | --- |
| Simplicity versus discovery | Keep labels, boundaries, and persistent essential actions when they help people act. A disappearing field is not an improvement. |
| Calm versus density | Preserve information needed for comparison. Improve alignment and grouping before moving useful content behind extra clicks. |
| Coherence versus context | Share meanings and patterns; allow layout and density to vary with the task and device. |
| Restraint versus expression | Retain colour, character, and expressive form when they support meaning, identity, comfort, or pleasure. Finn Juhl is a related Danish Modern counterpoint to strict functionalist form, not evidence for a universal style. |
| Speed versus considered action | Remove redundant steps; retain review where it prevents a costly mistake. Click count alone is not task quality. |

## Make and verify the improvement

For each material issue, connect **observed condition → user consequence → smallest effective change → verification**. For example: a saved indicator appears before the request completes → users may leave with unsaved work → distinguish saving, saved, and failed states → exercise a failed save and retry without losing input.

Prioritise task completion, accessibility, and dependable feedback; then comprehension and recovery; then visual refinement. Use existing system values where they fit. Revise tokens when the problem is systematic.

Revisit the affected task with representative content, a contrasting layout size, and relevant input methods. Exercise changed loading, success, failure, and recovery states. Check visible focus, readable contrast, text scaling, and reduced motion where the change touches them; use current platform guidance for numerical requirements.

Match evidence to the claim: visual comparison for hierarchy, an input sequence for operation, failure simulation for recovery, and network or runtime measurements for performance. If a check is unavailable, say what remains unverified. Do not infer accessibility from appearance or invent usability results.

Deliver the requested design, code, or review with the consequential changes, strengths preserved, checks performed, and remaining limits. Stop when further changes no longer improve the task or experience.

## Historical sources

Sources consulted 10 September 2026. Links support the historical background; UI decisions are contemporary interpretations.

- [Klint: proportions and precedent](https://www.carlhansen.com/en/at/inspiration/stories/the-story-of-danish-modern).
- [Jacobsen: architecture and interiors](https://arnejacobsen.com/life/biography/).
- [Henningsen: the three-shade system](https://www.louispoulsen.com/en-us/catalog/private/table/ph-4-3-glass-table?v=90411-5744161501-01).
- [Lauritzen: organisation from function](https://vilhelmlauritzen.com/we-are/our-founder/) and [the practice's welfare architecture](https://dac.dk/en/exhibitions/our-architecture).
- [Mogensen: everyday living and production](https://www.carlhansen.com/en/pl/designers/borge-mogensen).
- [Fisker and Danish functionalism](https://dac.dk/en/magazine/modernism).
- [Wegner: comfort and construction](https://www.carlhansen.com/en/designers/hans-j-wegner).
- [Kjærholm: materials and structure](https://www.fritzhansen.com/en/inspiration/designers/poul-kjaerholm).
- [Juhl: a sculptural counterpoint](https://finnjuhl.com/about/about-finn-juhl).

These references include museum, designer, practice, and manufacturer accounts. Danish Modern furniture offers related lessons; it is not synonymous with architectural functionalism. The MIT licence covers these original instructions, not the linked sources.

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
