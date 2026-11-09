# kemiljk/skills

Personal agent skills distilled from [Karl Koch](https://karlkoch.me)'s writing on design engineering, fluid interfaces, semantic HTML, and AI judgement, with researched design traditions translated into practical UI and UX guidance.

Install individual specialists for focused work, or use `dxe` for a coordinated design engineering review.

## Figma Design and Make

The [Figma editions](figma/skills/) are self-contained Markdown files adapted to Figma Design and Make. Each has the same skill name as its regular edition, including `dxe` and `dxe-fluid-design`. Use these files for Figma skill uploads; the installer commands below install the regular agent editions.

The Figma `dxe` edition contains its own rubric. Its exhaustive mode expands coverage of accessible screens and states; it does not require sibling skills.

## Install

### Selective (recommended)

Use the [skills CLI](https://github.com/vercel-labs/skills) to list the available skills, then install the workflows you need:

```bash
npx skills add kemiljk/skills --list
npx skills add kemiljk/skills -g --skill dxe-fluid-design --skill dxe-modern-css-html
```

Omit `-g` for a project-local installation. Choose the appropriate agents with `-a`, and keep one discoverable copy per skill in each host. Cross-host links to the same source are useful; duplicate entries in one host are not.

### Full collection

Install every regular agent skill, then choose the agents to install to:

```bash
npx skills add kemiljk/skills -g --skill '*'
```

Use `-a` to target specific agents, such as `-a codex` or `-a claude-code`. The CLI’s `--all` option installs every skill to every agent without prompting. See the [installer reference](https://github.com/vercel-labs/skills/blob/main/docs/commands.md) for the available options.

Verify installed skills with `npx skills ls -g`. Update global installations with `npx skills update -g`; for project installations, use `npx skills update -p`. Renaming an installed skill requires installing its new name; see [Migration](#migration).

## Master skill: `dxe`

`dxe` is the orchestrator — paired with [d×e](https://designengineer.xyz). It starts with a compact shared rubric, gathers repository and rendered evidence, then loads specialist sibling skills only when the target warrants them.

Install `dxe` and the relevant specialists for a normal pass. If a required lens is unavailable, the pass continues with the shared rubric and discloses the missing guidance. For `dxe exhaustive`, install all specialists in its [routing table](skills/dxe/SKILL.md#progressive-sibling-routing); installing the full collection above includes them. Standalone specialists such as `dxe-hiring-manager-bar` and `dxe-intentional-craft` remain separately invocable and are not automatically routed by `dxe`.

### How to invoke

In an agent with the skills installed, ask for a pass using the prompts below. Explicit invocation syntax depends on the host; you can also ask “Use the dxe skill to review this interface.”

| Prompt | Behaviour |
| --- | --- |
| `dxe` / “run a dxe pass” | Review representative surfaces in the workspace; report findings and proposed changes without edits |
| `dxe quick` | Compact review of one representative surface |
| `dxe src/components` | Review that path; a path can scope any mode |
| `dxe review` | Findings only; no edits |
| `dxe fix` | Review, implement bounded high-confidence fixes, and verify affected behaviour |
| `dxe exhaustive` | Read every routed specialist and inspect all discoverable surfaces and states in scope; no edits unless fixes are also requested |
| “apply all skills” | Alias for `dxe exhaustive` |

### What it reviews

Phases in order:

1. **Intent** — `dxe-write-first-design`, `dxe-subtractive-design`  
   Hypothesis for the pass; cut unexplained chrome and generative residue.
2. **Platform** — web: `dxe-semantic-html-first`, `dxe-modern-css-html`; native: `dxe-apple-native-ui`, `dxe-android-native-ui`
   Native controls and platform semantics before custom reconstructions.
3. **Feel** — `dxe-fluid-design`, `dxe-interface-affordances`, `dxe-product-delight`  
   Interruptible motion, discoverable controls, care over novelty.
4. **Bridge** — `dxe-design-engineering`  
   Map design structure to code structure; keep taste attached to materials.
5. **Shipping** — `dxe-ai-output-judgement`, `dxe-prototype-to-production`  
   Name concrete AI-median failures; harden empty/error/auth/focus paths.

Every phase is considered, but sibling skills are loaded progressively from evidence rather than up front. You get a single report with the hypothesis, evidence, verified strengths, confidence-tagged findings, subtractive cuts, verification status, and explicit limits.

Use individual skills when you want a narrow lens. Use `dxe` for a coordinated review of a repository or interface; normal review uses representative sampling and reports its limits.

## Skills

| Skill | Use when |
| --- | --- |
| `dxe` | **Coordinated review** — shared rubric and relevant routed specialists for a repository or interface |
| `dxe-hiring-manager-bar` | Review a job-seeking portfolio and recommend prioritized site code and content changes |
| `dxe-fluid-design` | Interfaces need physical motion, gestures, layout continuity |
| `dxe-modern-css-html` | Choosing native features, checking support, or replacing legacy workarounds |
| `dxe-semantic-html-first` | Building controls, forms, disclosure, dialogs |
| `dxe-apple-native-ui` | SwiftUI, UIKit, AppKit, and Apple-platform UI work, with a dedicated behaviour-first macOS workflow |
| `dxe-android-native-ui` | Kotlin, Jetpack Compose, Android Views, and Compose Multiplatform UI work |
| `dxe-interface-affordances` | Discoverability and perceptible interaction cues matter |
| `dxe-write-first-design` | Substantial product decisions need clarification before implementation |
| `dxe-design-engineering` | Bridging design intent and production implementation |
| `dxe-interaction-contracts` | Resolving the behaviour a component or flow promises, including interruption, persistence, and recovery |
| `dxe-design-system-evolution` | Choosing bounded component, variant, API, or token changes and planning compatibility and migration |
| `dxe-design-for-repetition` | Reducing recurring effort while preserving discoverability, context, and safe recovery |
| `dxe-real-content-design` | Using representative content to shape hierarchy, comparison, layout, and component structure |
| `dxe-intentional-craft` | Developing design and engineering ideas through human intention, focused scope, and evidence of craft, inspired by Apple's *Intention* film |
| `dxe-product-delight` | Adding polish without confusing novelty for care |
| `dxe-subtractive-design` | Removing noise and requiring purpose |
| `dxe-humane-functionalism` | Applying Danish functionalism to UI structure, perception, human fit, everyday use, and craft |
| `dxe-software-needs-hierarchy` | Prioritising software improvements through basic function, trust, belonging, competence, and growth, inspired by Maslow |
| `dxe-ai-output-judgement` | Critiquing generated UI, prose, or code when a quality review is requested |
| `dxe-prototype-to-production` | Hardening happy-path prototypes for real use |

## Composition / precedence

Use `dxe-interaction-contracts` when behaviour is unresolved, `dxe-design-system-evolution` when a shared model needs to change, `dxe-design-for-repetition` when a task's cost accumulates, and `dxe-real-content-design` when placeholder content is hiding structural decisions. Each supports a focused proposal, review, or authorised implementation without requiring a full suite pass. All four have self-contained Figma Design and Make editions.

For an experience-led craft pass, ask “Use `dxe-intentional-craft` to develop this idea” or “Use `dxe-intentional-craft` to refine this flow.” It translates Apple's 2013 *Intention* film into general design engineering decisions. Its [source and translation notes](skills/dxe-intentional-craft/references/source-and-translation.md) link the published copy, preserve an ordered paraphrase, and distinguish the film's message from the skill's software applications.

For a focused functionalist pass, ask “Use `dxe-humane-functionalism` to improve this flow.” It balances reduction with discoverability, useful density, accessibility, and product character. Its [research notes](skills/dxe-humane-functionalism/references/research.md) distinguish historical sources from contemporary UI applications.

For a needs-based quality review, ask “Use `dxe-software-needs-hierarchy` to prioritise improvements to this flow.” It translates Maslow's hierarchy into software decisions while allowing needs to overlap and vary by task. Its [source and translation notes](skills/dxe-software-needs-hierarchy/references/source-and-translation.md) distinguish the original framework from the software interpretation. A standalone Figma Design and Make edition is included.

Select skills for the task, not merely because their subject appears in a file. For a requested broad pass, `dxe` considers these lenses and loads only relevant guidance:

1. **Intent** — `dxe-write-first-design`, `dxe-subtractive-design`
   Add `dxe-humane-functionalism` when a Danish functionalist lens is requested.
   Add `dxe-software-needs-hierarchy` when a Maslow-inspired needs lens or needs-based prioritisation is requested.
2. **Platform** — web: `dxe-semantic-html-first`, `dxe-modern-css-html`; native: `dxe-apple-native-ui`, `dxe-android-native-ui`
3. **Feel** — `dxe-fluid-design`, `dxe-interface-affordances`, `dxe-product-delight`
4. **Bridge** — `dxe-design-engineering`
5. **Shipping** — `dxe-ai-output-judgement`, `dxe-prototype-to-production`

When motion taste and CSS purity disagree:

- `dxe-fluid-design` decides how the interaction should feel
- `dxe-modern-css-html` chooses the most native implementation that can deliver it
- JavaScript/Motion/SwiftUI remain appropriate for interruption, velocity, and gesture continuity CSS cannot express

## Migration

All specialist skill names now use `dxe-` (for example, `fluid-design` → `dxe-fluid-design`). The main `dxe` entry point keeps its name. Folder names, invocation names, and standalone Figma filenames use the same names.

Install the renamed skills using the commands above, then remove the corresponding old unprefixed installations from the same agents and scope to avoid duplicate discovery. Preserve any local customizations before replacing an installation. An update of an old name is not a substitute for this migration. For Figma, replace old uploads with the renamed standalone files.

`dxe-fluid-design` and `dxe-modern-css-html` previously lived in standalone repositories:

- https://github.com/kemiljk/fluid-design
- https://github.com/kemiljk/modern-css-html

Their repository URLs remain unchanged. The skill names now use the `dxe-` prefix; the main `dxe` entry point keeps its name. New installs should use this collection.

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
- [The hiring manager is your user](https://karlkoch.me/writing/the-hiring-manager-is-your-user/)

## Validation

From the repository root, check that the standalone Figma editions cover the regular skills and meet the collection’s metadata, licensing, and dependency rules:

```bash
python3 scripts/validate-figma.py
```

Each skill should stay:

- trigger-precise in frontmatter `description`
- compact in activated `SKILL.md`
- focused on useful decisions and project constraints, without mandatory process for routine edits
- progressively disclosed when examples are long enough for `references/`

## License

MIT. The Apple native guidance also preserves its upstream MIT attribution and license notice.
