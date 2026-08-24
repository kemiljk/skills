# Android native verification

Use this for rendered claims. Prefer the repository's existing Gradle tasks, test framework, and emulator setup.

## Minimum evidence

1. Run relevant Gradle build, unit, and instrumentation/UI tests when available.
2. Exercise a primary task on a compact and expanded window; include insets, keyboard, font scale, dark theme, and layout direction when relevant.
3. Inspect the Compose semantics tree and test TalkBack-relevant labels, roles, state, focus, traversal, and custom actions.
4. Capture Logcat errors/fatal exceptions and test-runner output separately from expected emulator or tooling noise.
5. Repeat motion-bearing tasks with Android's animator duration scale reduced or disabled.

## Settled semantics tests

Assert the result that establishes completion, not the immediate post-click frame.

```kotlin
composeTestRule.onNodeWithContentDescription("Save").performClick()
composeTestRule.onNodeWithText("Saved").assertIsDisplayed()
```

For async loading, navigation, sheets, and animation, use the test framework's idling/condition facilities or wait for a meaningful semantic/visible state. Do not treat a fixed delay as proof that the final state was reached.

## Release-facing checks

- System and predictive back returns to the expected destination without losing recoverable work.
- Process recreation and configuration changes preserve the state the product promises to preserve.
- Permissions, offline/partial failure, empty content, and retry paths remain navigable with TalkBack.
- Compose Multiplatform targets are verified per target; Android emulator evidence does not establish desktop or iOS behaviour.
