# Modern CSS task recipes

Original guidance for common upgrades. Prefer these over legacy patterns when support allows.

## Layout

```css
/* Centre */
.center { display: grid; place-items: center; }

/* Full viewport on mobile */
.screen { min-height: 100dvh; }

/* Component responsiveness */
.card-wrap { container-type: inline-size; }
@container (width < 400px) {
  .card { grid-template-columns: 1fr; }
}
```

## Colour

```css
:root {
  color-scheme: light dark;
  --accent: oklch(0.7 0.14 45);
  --accent-soft: color-mix(in oklch, var(--accent) 18%, transparent);
  --text: light-dark(oklch(0.25 0.02 260), oklch(0.95 0.01 260));
}
```

## Native overlay

```html
<button popovertarget="menu">Open</button>
<div id="menu" popover anchor="trigger">…</div>
```

```css
#menu {
  position: absolute;
  position-anchor: --trigger;
  top: anchor(bottom);
  left: anchor(center);
  translate: -50% 0.5rem;
}
```

## Scroll-driven reveal

```css
@media (prefers-reduced-motion: no-preference) {
  .reveal {
    animation: fade-up linear both;
    animation-timeline: view();
    animation-range: entry 10% cover 30%;
  }
}
```

## Replace these habits

| Old habit | Modern default |
| --- | --- |
| Absolute centre with translate(-50%, -50%) | `place-items: center` |
| Padding-top aspect ratio hack | `aspect-ratio` |
| JS sticky header | `position: sticky` |
| Hex palette + Sass lighten | `oklch` + `color-mix` |
| IO + `.is-visible` class toggles | CSS view timelines |
| Floating UI for simple menus | Popover + anchor positioning |
| `100vh` mobile shells | `100dvh` |
