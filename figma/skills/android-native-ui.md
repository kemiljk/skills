---
name: android-native-ui
description: "Design or review Android app concepts in Figma using native interaction, adaptive layout, and accessibility contracts."
license: MIT
---

# Android Native UI

Work within the selected or named scope and the user's request. Review requests produce findings without edits; implement changes when requested. Use available context, disclose inaccessible evidence, and preserve unrelated work.

Design an Android workflow around platform behavior, rather than matching a screenshot. Use this skill for Android concepts and handoff requirements; a Make web prototype is a simulation of those requirements.

## Establish the target

Identify the intended Android form factors, input methods, supported versions when known, Material or custom system, and whether the product also ships on other platforms. Use supplied Android library components when available. Do not invent access to a library or detach its instances merely to change appearance.

For release-sensitive recommendations, consult current Android Developer and Material guidance if browsing is available. Otherwise label the recommendation for platform verification instead of asserting a particular API or release behavior.

## Design the contract

- Use available window space to decide navigation and layout. A compact phone screen stretched across a tablet or foldable is not an adaptive design.
- Define back, dismiss, cancel, and unsaved-change behavior. Preserve the user's place and edits where appropriate.
- Make loading, empty, error, disabled, and permission states explicit for the affected flow.
- Keep selection and screen state stable when items move or a view is recreated. Record persistence expectations separately from transient feedback.
- Account for system bars, insets, keyboard obstruction, display cutouts, dark theme, large text, and right-to-left layout.
- Match target size and spacing to touch; provide keyboard and assistive-technology alternatives for custom gestures.

## Work in Figma

In Design, use auto layout, meaningful layer names, reusable components, properties, and available variables to encode intent. Create only the variants and example frames needed to resolve the task. Show compact and expanded behavior when both are in scope.

Annotate meaningful icons with intended names and decorative imagery as decorative. Specify role, selected/expanded state, reading order, focus movement, and any custom action. Android exposes a native semantics tree; an annotation or ARIA attribute is not a TalkBack implementation.

Prototype the principal path and recovery path when supported. Record behavior the prototype cannot express, including lifecycle restoration, system back, and gesture cancellation.

## Make and handoff

In Make, use accessible web controls to demonstrate the interaction and identify Android behavior that is only simulated. Do not present a browser preview as Compose, Views, or a native Android build.

For implementation handoff, preserve native control semantics, explicit state ownership, stable collection identity, and state-driven motion that still completes the task with animation reduced or disabled.

## Verify

Inspect layouts with long content, large text examples, empty content, and the intended window sizes. Exercise available prototype paths and report their coverage.

Native confidence requires an Android runtime: test TalkBack, keyboard/focus, system back, restoration, insets, and relevant compact/expanded configurations. If that runtime is unavailable, list the remaining checks as unperformed.

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
