# kemiljk/skills

Personal agent skills distilled from [Karl Koch](https://karlkoch.me)'s writing on design engineering, fluid interfaces, semantic HTML, and AI judgement.

Install selectively. Compose deliberately. Or run the full suite with `dxe`.

## Install

### Selective (recommended)

List the available skills, then install the workflows you need:

```bash
npx skills add kemiljk/skills --list
npx skills add kemiljk/skills -g --skill fluid-design --skill modern-css-html
```

Omit `-g` for a project-local installation. Choose the appropriate agents with `-a`, and keep one discoverable copy per skill in each host. Cross-host links to the same source are useful; duplicate entries in one host are not.

### Full collection

Install the full collection when you want every specialist available, including exhaustive DXE passes:

```bash
npx skills add kemiljk/skills -g --all
```

Verify installed skills with `npx skills ls -g`. Update with `npx skills update -g`.

## Master skill: `dxe`

`dxe` is the orchestrator — paired with [d×e](https://designengineer.xyz). It starts with a compact shared rubric, gathers repository and rendered evidence, then loads specialist sibling skills only when the target warrants them.

Install the full collection (`-g --all` above) when you need every specialist lens. A normal pass can still proceed with the shared rubric when an unneeded sibling is absent; `dxe exhaustive` requires the full collection.

### How to invoke

In Cursor / Claude Code (or any agent that has the skills installed), ask for a pass:

| Prompt | Behaviour |
| --- | --- |
| `dxe` / “run a dxe pass” | Full workspace review; propose fixes |
| `dxe quick` | Compact review of one representative surface |
| `dxe src/components` | Scope to that path |
| `dxe review` | Findings only; no edits |
| `dxe fix` | Findings, then high-confidence fixes |
| `dxe exhaustive` | Load the full suite and inspect every available surface |
| “apply all skills” | Alias for `dxe exhaustive` |

### What it runs

Phases in order:

1. **Intent** — `write-first-design`, `subtractive-design`  
   Hypothesis for the pass; cut unexplained chrome and generative residue.
2. **Platform** — web: `semantic-html-first`, `modern-css-html`; native: `apple-native-ui`, `android-native-ui`
   Native controls and platform semantics before custom reconstructions.
3. **Feel** — `fluid-design`, `interface-affordances`, `product-delight`  
   Interruptible motion, discoverable controls, care over novelty.
4. **Bridge** — `design-engineering`  
   Map design structure to code structure; keep taste attached to materials.
5. **Shipping** — `ai-output-judgement`, `prototype-to-production`  
   Name concrete AI-median failures; harden empty/error/auth/focus paths.

Every phase is considered, but sibling skills are loaded progressively from evidence rather than up front. You get a single report with the hypothesis, evidence, verified strengths, confidence-tagged findings, subtractive cuts, verification status, and explicit limits.

Use individual skills when you want a narrow lens. Use `dxe` when you want the full design-engineering pass on a repo.

## Skills

| Skill | Use when |
| --- | --- |
| `dxe` | **Master pass** — full design-engineering suite on a repo or path |
| `fluid-design` | Interfaces need physical motion, gestures, layout continuity |
| `modern-css-html` | Choosing native features, checking support, or replacing legacy workarounds |
| `semantic-html-first` | Building controls, forms, disclosure, dialogs |
| `apple-native-ui` | SwiftUI, UIKit, AppKit, and Apple-platform UI work, with a dedicated behaviour-first macOS workflow |
| `android-native-ui` | Kotlin, Jetpack Compose, Android Views, and Compose Multiplatform UI work |
| `interface-affordances` | Discoverability and perceptible interaction cues matter |
| `write-first-design` | Substantial product decisions need clarification before implementation |
| `design-engineering` | Bridging design intent and production implementation |
| `product-delight` | Adding polish without confusing novelty for care |
| `subtractive-design` | Removing noise and requiring purpose |
| `ai-output-judgement` | Reviewing generated drafts before shipping |
| `prototype-to-production` | Hardening happy-path prototypes for real use |

## Composition / precedence

Select skills for the task, not merely because their subject appears in a file. For a requested broad pass, `dxe` considers these lenses and loads only relevant guidance:

1. **Intent** — `write-first-design`, `subtractive-design`
2. **Platform** — web: `semantic-html-first`, `modern-css-html`; native: `apple-native-ui`, `android-native-ui`
3. **Feel** — `fluid-design`, `interface-affordances`, `product-delight`
4. **Bridge** — `design-engineering`
5. **Shipping** — `ai-output-judgement`, `prototype-to-production`

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
- focused on useful decisions and project constraints, without mandatory process for routine edits
- progressively disclosed when examples are long enough for `references/`

## License

MIT
