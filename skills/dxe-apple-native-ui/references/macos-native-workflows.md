# Native macOS workflows

Read this whenever macOS is an intended target. A native-looking screen is insufficient: the app must preserve Mac interaction contracts, interoperate with the rest of the system, and respect how people arrange long-lived work.

Use current Apple Human Interface Guidelines, Developer Documentation, and relevant WWDC sessions before making release-sensitive API claims. Confirm the deployment target first. Treat framework examples below as candidate substrates, not guarantees that an API exists or behaves identically on every supported macOS release.

## 1. Establish the Mac shape

Classify the app before choosing its shell:

- **Document-based:** independent files people open, edit, save, duplicate, version, and compare.
- **Library or shoebox:** app-managed collections such as notes, mail, photos, or tasks.
- **Utility or menu bar app:** a focused job, often with transient or lightweight windows.
- **Professional workspace:** dense, configurable tools, inspectors, panels, and multi-window workflows.
- **Viewer or browser:** navigation and inspection dominate editing.
- **Hybrid:** name which model owns each major workflow instead of forcing everything into one container.

Inventory the core objects. For each one, decide whether people can create, open, save, select, multi-select, rename, edit, drag, copy, paste, import, export, print, reveal in Finder, show in another window, automate, persist, and undo it. This object model should shape the UI before visual styling does.

For design or planning work, state the Mac identity explicitly: app shape, primary workflows, window/document model, conventions embraced, and any deliberate departure with its user benefit.

## 2. Choose the substrate by behaviour

Prefer SwiftUI for new work when it satisfies the required interaction contracts. Keep an existing AppKit-first architecture when rewriting it would not improve the product. Bridge only the surface whose behaviour needs AppKit rather than replacing an otherwise sound architecture.

Common decision points include:

| Contract | Start with | Consider a targeted AppKit path when |
| --- | --- | --- |
| Ordinary app or document scenes | SwiftUI scenes, `WindowGroup`, or `DocumentGroup` | The document lifecycle or window behaviour needs capabilities the supported SwiftUI release cannot provide |
| Lists and tables | SwiftUI `List` or `Table` | Complex outline/table editing, selection, focus, row views, or drag sessions are incomplete |
| Text | Native SwiftUI text controls | The workflow needs rich editing, layout, selection, or responder-chain behaviour from `NSTextView` |
| Commands | SwiftUI commands, focused values, and shortcuts | Responder-chain routing or menu/toolbar validation cannot be expressed reliably |
| Toolbars and inspectors | SwiftUI toolbar and scene APIs | Precise customisation, placement, panel behaviour, or persistence requires `NSToolbar`/AppKit windows or panels |
| Transfer and files | `Transferable`, file APIs, and SwiftUI drag/drop | Multiple pasteboard representations, file promises, or source/destination session control require `NSPasteboard` or AppKit dragging APIs |

Do not choose custom UI merely for visual control if it discards focus rings, active/inactive window state, keyboard navigation, selection semantics, accessibility, text behaviour, drag/drop, or undo. If a framework gap matters, verify it on the minimum supported OS and bridge that specific gap.

## 3. Build an affordance map

Before implementing a non-trivial screen, editor, list, or inspector, map the implied Mac behaviour. Use one row per meaningful surface or object.

| Surface/object | Native substrate | Selection and focus | Commands and keyboard | Copy/paste and drag/drop | Undo | State to restore | Accessibility |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Example document list | `Table` or `NSTableView` | Empty/single/multiple selection; Shift range; Command toggle; focused and inactive states | Arrows, Return, Delete, Command-A; menu validation follows selection | Plain-text names plus file URLs; reorder and drag to Finder if meaningful | Rename, move, delete, reorder | Columns, sort, selection policy, sidebar width | Table semantics, labelled rows, keyboard and VoiceOver actions |

The map is a design contract, not paperwork. Omit an affordance only because it does not fit the object or workflow, not because it was forgotten.

## 4. Design the command model before chrome

- Put important actions in the menu bar or an appropriate context menu, even when a toolbar also exposes them.
- Preserve standard menu locations, names, and shortcuts. Never repurpose a familiar shortcut for an unrelated action.
- Route commands to the focused editor, selected object, or active window. Validate enabled state and titles from that context.
- Give toolbar-only actions keyboard or menu equivalents when they matter to the primary workflow.
- Make Return, Escape, Delete, Tab/Shift-Tab, arrow keys, type-to-select, and search focus behave according to context.
- Register undo for meaningful reversible changes and use action names that describe the operation.
- Verify the main task without a pointing device.

Menus are the app's command inventory. If an action exists only behind an ambiguous icon or gesture, it is probably under-specified.

## 5. Design windows and documents intentionally

Choose among a document window, tab, secondary window, inspector or utility panel, sheet, popover, sidebar, and transient alert according to ownership and duration:

- Independent documents usually deserve independent windows and standard open/save behaviour.
- A document-scoped modal action belongs in a sheet attached to that document, not a global dialog.
- Persistent secondary controls belong in an inspector or panel; lightweight contextual choices fit a popover.
- Let people open multiple windows when comparison, reference, or parallel work benefits from it.
- Preserve standard title-bar, traffic-light, full-screen, tabbing, key-window, and active/inactive behaviours.
- Restore intentional arrangement: window frames, sidebar and inspector state, split positions, columns, toolbars, view modes, sort/group choices, and per-document view state.
- Do not restore accidental transient state that would surprise someone after relaunch.

For file-backed work, evaluate document type registration, recent documents, autosave, versions, duplicate/revert, Quick Look, Open With, drag-open, sensible open/save locations, export, and recovery. A library app still needs intelligible ownership, backup, import, export, and migration paths.

## 6. Preserve selection, text, pasteboard, and drag contracts

For selectable collections, verify click, Shift-click ranges, Command-click toggles, Command-A, arrow navigation, Delete, dragging the full selection, and context-menu actions on the intended selection. Keep keyboard focus distinct from selection and respect active versus inactive windows. Use multi-selection when it removes repetitive work.

Keep native text controls unless the replacement preserves system editing and input behaviour: movement and selection shortcuts, undo, spelling and substitutions, Services, drag selection, Unicode and composed characters, bidirectional text, and input methods.

For every selected domain object, ask what Command-C should place on the pasteboard. Offer useful public representations alongside any private one: plain or rich text, URLs, file URLs, images, tabular data, or files/file promises as appropriate. Accept common external representations on paste rather than only the app's private format.

Design drag/drop in every meaningful direction: within a collection, between app windows, into the app from Finder or another app, and out to Finder or another app. Preserve multi-item semantics, modifier-key intent, cancellation, invalid-drop recovery, source-side feedback, keyboard/VoiceOver alternatives, and undo where practical.

## 7. Participate in the Mac ecosystem

Choose integrations because they complete a workflow, not to fill a feature checklist. Consider:

- Finder, Open With, document types and UTTypes, Quick Look, and Spotlight metadata.
- Standard import/export formats and plain-text fallbacks that prevent lock-in.
- Share, Services, Shortcuts/App Intents, URL schemes, and scripting for repeated professional workflows.
- Printing and PDF output when the object has a printable or portable form.
- Dock and menu-bar behaviour appropriate to the app category.
- Continuity, Handoff, and iCloud only when they preserve a real cross-device workflow.

## 8. Add depth without hiding the common path

Start with useful defaults, then make recurring choices configurable. Appropriate depth can include adjustable split views, saved columns and sort order, configurable toolbars, inspectors, context menus, tooltips, Option-key alternatives, searchable settings/help, and reset-to-default paths.

Avoid both extremes: exposing every control at once and removing capability in pursuit of superficial simplicity.

## 9. Deliver and verify a Mac workflow

For a design or implementation plan, include:

1. Mac identity and core-object inventory.
2. Affordance map.
3. Command/menu and keyboard plan.
4. Window/document and restoration plan.
5. Pasteboard, drag/drop, file, and system-interoperability plan.
6. Settings, accessibility, and verification plan.

For a review, tie every claim to a source path or observed macOS runtime and name the input method. Distinguish source-only risks from rendered behaviour. Do not infer a Mac defect from an iOS simulator or preview.

Run the relevant behaviour probes on macOS:

- Use standard shortcuts and the primary workflow with keyboard only.
- Exercise arrow navigation, Return, Escape, Delete, Tab/Shift-Tab, type-to-select, and search while navigating results.
- Test empty, single, range, and discontiguous selections; open a context menu on selected and unselected items.
- Copy domain objects into plain-text and rich targets; paste common external forms back into the app.
- Drag into, out of, within, and between windows; cancel a drag and drop on an invalid target.
- Undo edits, deletions, moves, reorders, imports, and other meaningful mutations.
- Open multiple windows/documents; inspect the Window menu; quit and relaunch to verify intentional restoration.
- Resize windows, sidebars, columns, splits, and inspectors; verify saved configuration and reset paths.
- Exercise Finder/open/save/import/export flows with spaces, emoji, non-Latin text, long filenames, and unexpected but valid locations.
- Test VoiceOver, Full Keyboard Access, dark appearance, increased contrast, Reduce Motion, and reduced transparency where relevant.
- Keep typing, menus, selection, resizing, and dragging responsive while background work runs.

If runtime access is unavailable, provide the probes as a manual checklist and label verification as unperformed.

## Current primary references

- [Designing for macOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-macos/)
- [Menus](https://developer.apple.com/design/human-interface-guidelines/menus)
- [Windows](https://developer.apple.com/design/human-interface-guidelines/windows)
- [Keyboards](https://developer.apple.com/design/human-interface-guidelines/keyboards/)
- [Drag and drop](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop)

## Source acknowledgement

The behaviour-first framing and affordance-map approach are adapted from Bart Reardon's [mac-arsed-mac-app skill](https://github.com/bartreardon/skills/tree/main/mac-arsed-mac-app), used under the MIT License. See [macos-source-license.txt](macos-source-license.txt) for the upstream copyright and license notice.
