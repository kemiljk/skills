# Apple native verification

Use this for rendered claims, not as a mandatory toolchain recipe. Record unavailable checks as limits.

## Minimum evidence

1. Run the repository's Xcode build and test targets when available.
2. Exercise the primary user task on the primary target and one contrasting form factor: iPhone plus iPad split view, resizable macOS window, or the relevant watchOS/tvOS/visionOS target.
3. Repeat relevant surfaces with larger Dynamic Type, dark appearance, Reduce Motion, and right-to-left layout when the product supports it.
4. Inspect VoiceOver behaviour with Accessibility Inspector or a device: names, values, traits, order, grouping, adjustable controls, and focus after presentation/dismissal.
5. Capture simulator/device runtime diagnostics separately from build warnings. Reproduce before describing one as a product defect.

## Settled UI tests

Do not sample a sheet, menu, alert, or animation immediately after its trigger. Wait for the target state.

```swift
let savedNotice = app.staticTexts["Saved"]
app.buttons["Save"].tap()
XCTAssertTrue(savedNotice.waitForExistence(timeout: 2))
XCTAssertTrue(savedNotice.isHittable)
```

For tests that query accessibility state, wait for the native element or visible result that establishes completion. A fixed sleep is only a last-resort diagnostic, never the evidence boundary.

## Platform reminders

- iOS/iPadOS: keyboard avoidance, safe areas, rotation, split view, pointer, and state restoration.
- macOS: window resizing, menu and command validation, toolbar placement, keyboard-only workflows, selection, copy/paste, drag/drop, undo, Finder/open-save integration, and multi-window state restoration across relaunch. Use the behaviour probes in [macos-native-workflows.md](macos-native-workflows.md).
- watchOS/tvOS/visionOS: the platform's focus, navigation, input, and power constraints are primary contracts.

`#Preview` is useful local evidence, but it does not replace accessibility or device/runtime verification.
