# Motion recipes

Use these only when the activated skill rules are not enough.

## Motion (`motion/react`)

```tsx
<motion.div
  animate={{ x: targetX }}
  transition={{ type: "spring", stiffness: 300, damping: 25, mass: 0.8 }}
/>
```

```tsx
<motion.div
  drag="y"
  dragConstraints={{ top: 0, bottom: 0 }}
  dragElastic={0.2}
  onDragEnd={(_, info) => {
    if (info.velocity.y > 500 || info.offset.y > 200) onDismiss();
  }}
/>
```

```tsx
<AnimatePresence mode="popLayout" initial={false}>
  {items.map((item) => (
    <motion.div
      key={item.id}
      layout
      initial={{ opacity: 0, scale: 0.96 }}
      animate={{ opacity: 1, scale: 1 }}
      exit={{ opacity: 0, scale: 0.96 }}
      transition={{ type: "spring", stiffness: 400, damping: 30 }}
    />
  ))}
</AnimatePresence>
```

## CSS for simple state

```css
.panel {
  translate: 0 100%;
  transition: translate 250ms ease-out, opacity 180ms ease;
}
.panel.open {
  translate: 0 0;
}
@media (prefers-reduced-motion: reduce) {
  .panel {
    transition: opacity 160ms ease;
  }
}
```

Use transitions (interruptible) for interactive state. Reserve keyframes for decorative, non-interactive sequences.

## SwiftUI

```swift
withAnimation(.spring(response: 0.35, dampingFraction: 0.82)) {
  isOpen.toggle()
}
```

## When CSS is enough vs when JS is required

| Behaviour | Prefer |
| --- | --- |
| Colour / opacity / simple show-hide | CSS transitions, `@starting-style` |
| Scroll-linked reveals | CSS `animation-timeline: view()` |
| Shared page/object transitions | View Transitions API |
| Gesture velocity, rubber-banding, interruptible springs | Motion / JS / SwiftUI |
| Dense hover velocity gating | JS (EMA + thresholds) |
