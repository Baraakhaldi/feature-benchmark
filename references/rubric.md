# Feature scoring rubric (8 dimensions, 0-10)

Score each product's version of the feature per dimension. Default weights are equal; raise the dimensions linked to the user's top 3 needs and to the research, and state the weights in the report. Mark a score "(inferred)" when judged from docs, videos or text, not by walking the flow. Use half points sparingly.

| # | Dimension | 3 looks like | 6 looks like | 9 looks like |
|---|---|---|---|---|
| 1 | Discoverability | Hidden in a menu, unclear label, hard to find on mobile | Visible on main screens, clear label | Right where the need arises, contextual entry points, keyboard shortcut or deep link |
| 2 | Flow efficiency | Many screens, repeated inputs, forced sign-up, no defaults | Reasonable steps, some smart defaults | Fewest possible steps, prefilled and remembered inputs, progress clear, can resume |
| 3 | Completeness (needs coverage) | Covers the basic case only | Covers most needs in the checklist | Covers all needs plus thoughtful extras that users praise |
| 4 | States and errors | Blank screens, generic errors, no loading feedback, dead ends | Basic empty, loading and error states | Every state designed, errors say how to fix, undo, no dead ends, works offline or slow |
| 5 | Clarity and copy | Jargon, vague buttons, unclear outcomes | Mostly clear labels and messages | Plain words, specific buttons, outcomes and costs clear before acting |
| 6 | Interaction and visual quality | Inconsistent, cramped, clunky on mobile | Clean and consistent, works on mobile | Polished, fast-feeling, purposeful motion, native-feeling on each platform |
| 7 | Accessibility and inclusion | Fails keyboard or contrast, unlabeled controls, one language only | Mostly accessible, some gaps | Meets the WCAG 2.2 AA criteria for this feature, screen-reader friendly, proper RTL and localisation where relevant |
| 8 | Trust and control | Surprises (hidden costs, auto opt-ins), hard to undo or cancel | Clear but some friction | Transparent, user stays in control, privacy respected, easy to undo or leave |

## Linking needs to dimensions
- "Fast" / "fewer steps" → 2 · "Easy to find" → 1 · "Does everything we need" → 3 · "Fewer errors / tickets" → 4, 5 · "Mobile" → 2, 6 · "Arabic / accessibility" → 7 · "Conversion / trust" → 5, 8.

## Overall ranking
Rank products by weighted total into tiers: A (8+), B (7-7.5), C (6), D (5), E (≤4). Place the user's feature among them, or the target spec if not built.

## Severity for issues
- **Critical:** blocks the task or breaks trust (dead end, data loss, wrong totals, broken on mobile, inaccessible core control), or cheap to fix with big impact.
- **High:** a top-3 need unmet, or a core sub-feature most benchmarks have.
- **Medium:** polish, copy, secondary states, nice-to-have extras.
