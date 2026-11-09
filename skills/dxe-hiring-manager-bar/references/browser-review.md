# Browser evidence

Use the browser controls available in the current environment. Follow the visible visitor journey using current page or accessibility snapshots: landing page → work listing → project → about/contact. Do not substitute guessed routes or repository knowledge for testing discoverability. Use separate sessions for concurrent reviews, and close sessions you create when finished.

If the project or environment provides a Playwright or axe toolkit, read its documentation for commands, browser requirements, readiness conditions, and capture options. This skill does not require a particular toolkit, local directory, or browser installation. If browser access is unavailable, identify the checks that remain unverified and scope the review to the evidence available.

## Capture the journey

Inspect a desktop viewport and a narrow viewport appropriate to the intended audience. Record dimensions, browser, input mode, URL, and relevant state with each capture. Exercise observed links to reach project and contact pages; a list of independently opened URLs does not demonstrate that the navigation works.

Capture screenshots alongside page structure, rendered text, links, headings, and relevant diagnostics when the tools support them. Exercise keyboard navigation, visible focus, overlays, and touch alternatives where relevant. Compare normal and reduced motion for consequential animations. Wait for known readiness conditions or settled transitions; inspect lazy content after the scroll or action that reveals it.

Keep captured evidence in the task's output directory. An evidence index is not the review: inspect screenshot pixels and execute the relevant interactions before claiming rendered behaviour. Chromium mobile emulation is not Safari or a physical phone. ARIA, DOM, and text alone cannot prove visual hierarchy, legibility, focus visibility, or complete accessibility. DOM inventories can include hidden content, and full-page screenshots can omit unloaded content.

## Interpret the evidence

Treat axe violations, incomplete rules, overflow measurements, and browser errors as investigation leads. Confirm their effect on a plausible visitor journey before including them in the fix list, with the consumer use case, prerequisites, reproduction sequence, expected and actual behaviour, and impact. Do not turn scan counts into a hiring verdict or treat an unexecuted check as a failure.

Inspect the contact destination without sending a message or submitting a form. A reachable contact page supports a navigation claim; it does not prove successful message delivery.
