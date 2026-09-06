---
name: semantic-html-first
description: "Specify or implement semantic HTML and accessible control behavior for Figma web designs and Make prototypes."
license: MIT
---

# Semantic HTML First

Work within the selected or named scope and the user's request. Review requests produce findings without edits; implement changes when requested. Use available context, disclose inaccessible evidence, and preserve unrelated work.

Native HTML is interaction infrastructure. Choose the element that matches the action before styling it.

## Choose the contract

| Intent | Starting element |
| --- | --- |
| Performs an action | `button` |
| Navigates to a destination | `a` with `href` |
| Reveals related content | `details`/`summary` or disclosure button |
| Collects information | Labeled native controls inside `form` |
| Opens a modal task | Modal `dialog` with appropriate focus behavior |
| Shows a nonmodal transient surface | Popover when its behavior fits |

A popover is not automatically a modal dialog or a fully accessible menu. Choose the pattern according to interaction behavior, and verify the resulting keyboard and focus contract.

## Figma Design

Annotate web control intent alongside component states: role, name, value, disabled/expanded/selected state, and expected keyboard behavior. Represent labels and focus indicators visibly where appropriate.

Keep navigation and actions distinct even when their styling is similar. Define modal entry, Escape/dismissal, and focus return. Mark decorative images as decorative and provide names for meaningful icon actions.

These are implementation requirements. Layer names, component variants, and prototype links do not create HTML semantics or a working accessibility tree.

## Make implementation

- Prefer native elements over clickable `div` or `span` replacements.
- Use explicit button types to avoid accidental form submission.
- Give inputs associated labels and useful validation feedback.
- Use ARIA to refine a valid semantic structure, not to replace native behavior unnecessarily.
- Prefer native state selectors such as `:disabled`, `:checked`, and `:invalid` over competing state systems when they express the same fact.
- Inspect what a library component actually renders. Its name alone does not establish semantics.
- Preserve native form submission, reset, disabled behavior, and keyboard activation.

## Verify

Exercise Tab and Shift-Tab navigation, Enter/Space activation where appropriate, form submission, disabled controls, and dialog dismissal/focus return. Inspect accessible names, roles, and states when the runtime permits.

Check that a visual state and its exposed semantic state agree. Report which checks were run and which remain specifications. Browser behavior cannot establish native Apple or Android accessibility.

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
