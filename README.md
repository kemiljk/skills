# kemiljk/skills

Personal agent skills distilled from [Karl Koch](https://karlkoch.me)'s writing on design engineering, fluid interfaces, semantic HTML, and AI judgement.

Install selectively. Compose deliberately.

## Install

List available skills:

```bash
npx skills add kemiljk/skills --list
```

Install specific skills:

```bash
npx skills add kemiljk/skills \
  --skill fluid-design \
  --skill modern-css-html \
  --skill ai-output-judgement
```

## Skills

| Skill | Use when |
| --- | --- |
| `fluid-design` | Interfaces need physical motion, gestures, layout continuity |
| `modern-css-html` | Writing/reviewing CSS & HTML with current platform features |
| `semantic-html-first` | Building controls, forms, disclosure, dialogs |
| `interface-affordances` | Discoverability and perceptible interaction cues matter |
| `write-first-design` | Decisions should be written before pixels or code |
| `design-engineering` | Bridging design intent and production implementation |
| `product-delight` | Adding polish without confusing novelty for care |
| `subtractive-design` | Removing noise and requiring purpose |
| `ai-output-judgement` | Reviewing generated drafts before shipping |
| `prototype-to-production` | Hardening happy-path prototypes for real use |

## Composition / precedence

Skills overlap on purpose. Use this order when several activate:

1. **Intent** — `write-first-design`, `subtractive-design`
2. **Platform** — `semantic-html-first`, `modern-css-html`
3. **Feel** — `fluid-design`, `interface-affordances`, `product-delight`
4. **Shipping** — `ai-output-judgement`, `prototype-to-production`

When motion taste and CSS purity disagree:

- `fluid-design` decides how the interaction should feel
- `modern-css-html` chooses the most native implementation that can deliver it
- JavaScript/Motion/SwiftUI remain appropriate for interruption, velocity, and gesture continuity CSS cannot express

## Migration

`fluid-design` and `modern-css-html` previously lived in standalone repositories:

- https://github.com/kemiljk/fluid-design
- https://github.com/kemiljk/modern-css-html

Those names are preserved here with tighter activation files, clearer checklists, and on-demand references. New installs should use this collection.

## Source writing

These skills compress lessons from essays such as:

- [10 Principles for Fluid UI](https://karlkoch.me/writing/10-principles-for-fluid-ui)
- [On the semantic web](https://karlkoch.me/writing/on-the-semantic-web)
- [Write-first design](https://karlkoch.me/writing/write-first-design)
- [The slop isn't the models](https://karlkoch.me/writing/the-slop-isnt-the-models)
- [Ten principles for product delight](https://karlkoch.me/writing/ten-principles-for-product-delight)
- [Beauty comes from absence](https://karlkoch.me/writing/beauty-comes-from-absence)
- [Design for handshakes, not handovers](https://karlkoch.me/writing/design-for-handshakes-not-handovers)
- [On teaching AI how you work](https://karlkoch.me/writing/on-teaching-ai-how-you-work)

## Validation

Each skill should stay:

- trigger-precise in frontmatter `description`
- compact in activated `SKILL.md`
- actionable via prefer/reject rules and checklists
- progressively disclosed when examples are long enough for `references/`

## License

MIT
