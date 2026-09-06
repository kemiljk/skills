---
name: apple-native-ui
description: "Design or review Apple app concepts in Figma using platform controls, adaptive layout, navigation, and accessibility contracts."
license: MIT
---

# Apple Native UI

Work within the selected or named scope and the user's request. Review requests produce findings without edits; implement changes when requested. Use available context, disclose inaccessible evidence, and preserve unrelated work.

A native interface preserves platform interaction, accessibility, and adaptation contracts. Design those contracts alongside appearance.

## Establish the target

Identify the intended Apple platforms, supported versions when known, input methods, and form factors. Do not carry an iPhone convention into Mac, iPad multitasking, Watch, TV, or spatial interfaces without considering the workflow.

Use available system library components, semantic colors, and text styles before reconstructing controls. Preserve the existing product system and component relationships. For release-sensitive conventions, consult current Apple Human Interface Guidelines and Developer Documentation when browsing is available; otherwise identify what needs platform verification.

## Design the behavior

- Choose navigation, sheets, dialogs, toolbars, and sidebars for the target platform. Define back, cancel, dismissal, unsaved edits, and focus restoration.
- Show relevant loading, empty, error, selection, disabled, and recovery states.
- Account for larger text, safe areas, narrow windows, rotation, keyboard, pointer, and layout direction.
- Preserve an object's identity through sorting, selection, editing, and transitions. Specify what state survives leaving and returning.
- Give meaningful icons accessible names; distinguish decorative imagery. Describe intended roles, values, grouping, reading order, and focus movement.
- Provide a Reduce Motion path that keeps the task possible and its state understandable.

## Mac-specific decisions

Treat Mac as a distinct workflow. Decide whether the primary objects live in documents, a managed library, a utility, or a multi-window workspace. Let that decision shape windows, navigation, and persistence.

Define important commands and standard keyboard equivalents. Keep selection separate from keyboard focus. Consider multi-selection, undo, native text editing, copy/paste, drag/drop, opening files, and intentional window restoration where they serve the product. A resizable iPad layout does not establish these behaviors.

## Work in Figma

In Design, use auto layout, component properties, appropriate variants, and available variables. Show the scoped flow at the relevant sizes with realistic content. Annotate runtime requirements that prototype connections cannot represent.

A Figma accessibility annotation specifies intent; it does not create a native accessibility tree. A connected prototype demonstrates the paths exercised, not native navigation, VoiceOver, or operating-system integration.

In Make, build an accessible web simulation when requested. Label platform behavior that is simulated; do not describe it as a SwiftUI, UIKit, or AppKit build. Preserve native expectations in the handoff instead of implementing decorative imitations as proof.

## Verify and deliver

Inspect the design at the intended dimensions and with larger text and long content. Exercise supported prototype interactions, including cancellation and recovery. Identify the frame/component and platform for each finding.

Native verification remains a separate step on the actual target: VoiceOver, keyboard, focus, state restoration, window or device adaptation, and system integrations. State which of these have not been tested.

## License notice

MIT License

Copyright (c) 2026 Karl Koch
Copyright (c) 2026 Bart Reardon (adapted macOS workflow guidance)

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
