---
name: android-native-ui
description: "Build or review Android interfaces in Compose or Views, including Material conventions, accessibility, adaptive layout, and state."
license: MIT
---

# Android Native UI

Build and review Android interfaces around platform contracts: Compose semantics, lifecycle-aware state, adaptive windows, Material/system integration, back navigation, and accessibility—not web ARIA or pixel-only parity.

## Identify the UI boundary

Map Android Views versus Compose, Material 3/custom design system, minimum SDK, navigation library, state holder, and whether the project is Android-only or Compose Multiplatform.

For Compose Multiplatform, keep portable UI in `commonMain`; isolate Android APIs such as `Context`, permissions, back handling, and window APIs at the platform boundary. Verify each shipped target independently.

## Fresh platform guidance

Before prescribing or implementing APIs, behaviour, Material conventions, tooling, or verification that may vary by Android/Compose/Kotlin release, search current primary Android sources: `developer.android.com`, AndroidX release notes, and Kotlin documentation where relevant. Check the project's SDK, Compose BOM/library versions, and shipped Compose Multiplatform targets before recommending an API. The examples here express durable contracts; they are not a substitute for release-specific documentation.

## State, effects, and component APIs

Hoist state only as high as the caller that needs to control it. Model durable screen state separately from one-shot events. Collect flows with lifecycle awareness on Android, and use `LaunchedEffect`, `DisposableEffect`, or other explicit effects for imperative work—not a composable body.

```kotlin
@Composable
fun SaveButton(
    enabled: Boolean,
    onSave: () -> Unit,
    modifier: Modifier = Modifier,
) {
    Button(
        onClick = onSave,
        enabled = enabled,
        modifier = modifier,
    ) {
        Text("Save")
    }
}
```

Reusable composables should expose a `Modifier` at the outer boundary, preserve native control semantics, and avoid growing boolean/primitive parameter lists where a state model or slot is clearer. Check modifier order deliberately: hit targets, clipping, padding, indication, and semantics can change with order.

## Compose performance and motion

Composition, layout, and drawing are different phases. Do not write layout-derived state that a sibling reads during composition without proving the feedback loop is safe. Avoid expensive allocations or collection work in hot composable bodies; use stable keys in lazy collections. Read animation, scroll, and gesture state in the latest phase that can produce the intended effect.

Animations should be state-driven, cancellable where interaction demands it, and usable when Android's animator duration scale is reduced or disabled. Wait for the visible or semantic completion condition before counting animations or reading final state.

## Accessibility and adaptation

Compose uses a semantics tree, not ARIA. Test content descriptions, roles, state descriptions, custom actions, traversal order, merged semantics, focus, TalkBack, touch targets, and disabled state. `contentDescription = null` is correct only for decorative content.

Use window size classes and available space rather than device labels. Test compact and expanded windows, large font scale, dark theme, display cutouts/insets, keyboard, layout direction, and predictive/system back where relevant.

```kotlin
Icon(
    imageVector = Icons.Default.Star,
    contentDescription = null, // decorative beside visible text
)
```

Read [references/android-verification.md](references/android-verification.md) before making rendered Android claims. It contains the minimum evidence lane and semantics-based examples.

## Prefer / reject

| Prefer | Reject |
| --- | --- |
| Material/native control semantics with intentional theming | Clickable layout that loses role, state, or keyboard/accessibility behaviour |
| Immutable UI state and lifecycle-aware collection | Side effects or mutable event handling in composition |
| Stable lazy keys and phase-appropriate reads | Index keys and composition/layout feedback loops |
| Semantics tests plus rendered checks | Screenshot-only claims about accessibility or state |
| Window-size adaptation | Phone-only layouts stretched across tablets, foldables, and desktop |
