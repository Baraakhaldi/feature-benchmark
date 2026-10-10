# Question bank

Ask with AskUserQuestion: up to 4 questions per call, 2-4 options each (the tool adds "Other"). Put the recommended option first and add "(Recommended)". Include a "Skip / you decide" style option where it makes sense. Pre-fill options from the quick look (Phase 0), `feature-presets.md` and the user's extras.

## Call 1: the feature and the needs
1. **Which parts of the feature are in scope?** (header: Scope, multiSelect) Sub-flows from the preset or the quick look, e.g. for search: Search box and suggestions · Results page · Filters and sort · No-results state.
2. **Where is the feature today?** (Status) Live and in use · Partly built · Designed, not built · Just an idea.
3. **Who uses it?** (Users, multiSelect) e.g. New visitors · Returning customers · Admins / staff · Research it for me.
4. **What matters most?** (Needs, multiSelect) Pre-filled with the preset's top needs plus anything the user said, e.g. Find results fast · Works well on mobile · Handles typos · Works in Arabic.

## Call 2: success, platforms, where to look
5. **How will you know it got better?** (Success) Higher conversion / completion · Faster to finish · Fewer errors or support tickets · More repeat use.
6. **Platforms to check** (Platforms, multiSelect) Web desktop · Web mobile · iOS app · Android app.
7. **Where should benchmarks come from?** (Sources, multiSelect) Direct competitors · Same category, other markets · Best-in-class from any industry (Recommended) · Open-source projects and UI libraries.
8. **Competitors** (Products) Suggest them for me (Recommended) · I'll name some · Mix of both.

## Call 3: depth, outputs, permissions
9. **Benchmark depth** (Depth) Standard ~10 products (Recommended) · Quick ~5 · Deep 15+.
10. **Outputs** (Outputs, multiSelect) Feature benchmark report · Feature brief (research) · Feature spec · Component kit. Then ask in a follow-up about the Resource directory and Build prompt, or include them by default when the status is "Designed" or "Just an idea".
11. **Browsing permissions** (Permissions, multiSelect) Public pages only · I'll sign in where the feature needs a login · Walk flows up to (not including) submit · Ask me each time.
12. **Market or language focus** (Markets) None / global · Specific countries (ask which) · Specific languages incl. RTL. Ask only if the needs or the product hint at it.

Also ask (free text or follow-up): output folder path; any extras not yet shared (analytics, tickets, reviews, designs).

## Mapping answers to the work
- **Status = Just an idea / Designed:** skip the Phase 4 audit; the spec and build prompt become the main outputs; the report compares benchmarks with each other and with the target needs.
- **Needs** set rubric weights: the top 3 needs raise their linked dimensions (see `rubric.md`).
- **Success signal** decides which numbers to measure first (e.g. "faster" → steps, clicks, time; "fewer errors" → validation and error states).
- **Login needed** on competitor products: list them in the 2A proposal; the user decides whether to sign in or accept "from docs, not tested".
