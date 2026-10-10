---
name: feature-benchmark
description: Benchmark one specific feature (search, onboarding, checkout, booking, filters, notifications, dashboard, chat, settings, sharing, anything) of the user's app, website or product idea against the products that do it best, starting from the user's own needs. Produces a cited feature brief, a feature benchmark report with step-by-step flow screenshots and a feature matrix, a feature spec with acceptance criteria, a component kit, a resource directory and a ready-to-paste build prompt. Use when the user names a feature and asks how others do it, wants to compare or improve a feature, plan a new feature, find best practices or patterns for a feature, or find components to build it. Triggers on "benchmark this feature", "how do the best apps do X", "compare our onboarding/checkout/search", "feature research", "feature teardown", "competitive feature analysis". For a whole-website or whole-company benchmark use website-benchmark instead.
---

# Feature Benchmark

Turn one feature plus the user's needs into research, a benchmark against the products that do that feature best, and a concrete plan to build or fix it. The **feature** is the subject, not the company. The product it lives in can be anything: a website, web app, mobile app, desktop app, internal tool, or an idea that is not built yet.

The user's needs drive everything: which products to compare, what to measure, how to weight scores and what the spec must include. Follow the phases in order. Never skip the two scope confirmations.

## Phase 0: Intake

1. Get three things, asking only for what is missing:
   - **The feature** in the user's words (e.g. "the search in my recipe app", "onboarding for new sellers").
   - **The needs**: what the feature must let people do, for whom, and what is wrong or missing today. Constraints: stack, platform, budget, deadlines, compliance, brand.
   - **The product**: URL, app store link, screenshots, screen recording, Figma file, repo, PRD, or "not built yet".
2. Ask whether the user has extras: analytics or funnel data, support tickets, reviews, user interviews, survey results, a current spec, competitor lists, design files. Read every extra before asking more questions.
3. Quick look (text only, no heavy work): where the feature sits in the product today, how people reach it, its main states. If the product is a repo, read only the files that implement the feature. If it is not built, note that and move on.
4. Load `references/feature-presets.md`: if the feature matches a preset, use its flow steps, states, needs and typical benchmark set as starting points.

## Phase 1: Questions (multiple choice)

Ask with the AskUserQuestion tool, at most 4 questions per call, in 2-3 calls. Pre-fill options from Phase 0, the presets and the extras. Use `references/questions.md` for the full bank. Core questions:

1. Feature scope (which sub-flows are in and out) · 2. Current state (live / partly built / designed / idea) · 3. Who uses it · 4. Top needs, ranked (multiSelect, pre-filled) · 5. Success signal (conversion, time to complete, fewer errors, retention, support tickets) · 6. Platforms (web desktop, web mobile, iOS, Android, desktop app) · 7. Where to look for benchmarks (direct competitors / same category / best-in-class from any industry / open-source and UI libraries) · 8. Competitors (suggest / user names / mix) · 9. Depth (Quick ~5 products / Standard ~10 / Deep 15+) · 10. Outputs · 11. Browsing permissions (including whether the user will sign in where the feature is behind a login)

Also ask where to save the outputs (a folder path).

## Phase 2: Scope confirmation, twice

- **2A. Proposal.** Show the plan: the feature and its sub-flows, the ranked needs, the flow steps and states to check on every product, the benchmark list grouped as direct / same category / best-in-class / open-source (each with URL and one-line reason it was picked), platforms, outputs, browsing permissions (which products need a login and who signs in), estimated time and number of agents. Invite edits.
- **2B. Final recap.** After edits, show a 3-4 line recap and ask **Start · Edit again · Cancel** with AskUserQuestion. Nothing heavy (research, flow captures, benchmark) runs before the user picks Start.

## Phase 3: Research

Use `references/research-playbook.md`. Run research agents in parallel (general-purpose subagents with WebSearch/WebFetch). Every finding needs a cited URL and year; label estimates.

- **A. Feature best practices:** usability research for this feature (Baymard, Nielsen Norman Group, platform guidelines such as Apple HIG and Material Design, web.dev), known patterns and anti-patterns, benchmark numbers (e.g. typical completion rates, recommended step counts) where reliable.
- **B. User expectations:** what users of this kind of product expect from the feature, ranked. Use the user's extras first (tickets, reviews, analytics), then public reviews and forums for the benchmark products (what people praise or complain about in this feature).
- **C. Standards and rules that touch this feature only:** accessibility (WCAG 2.2 AA items relevant to it), privacy and consent, payments, age, regional rules. Skip what does not apply.
- **D. Market context only if the user named markets:** languages and RTL, local payment or identity methods, local platforms. Reuse the website-benchmark market files if installed (`../website-benchmark/references/markets/`) but re-verify.
- **E. Benchmark discovery:** products that do this feature best, including outside the user's industry (e.g. Airbnb's date picker for a clinic booking flow). New candidates go back to the user for approval.

Turn the research into: (1) rubric weights, (2) a needs checklist (one yes/no line per need, used on every product), (3) the requirements for the spec and build prompt.

## Phase 4: Audit the user's feature

Skip to Phase 5 if the feature is not built yet; the needs checklist becomes the baseline instead.

1. **Walk the flow** step by step on each chosen platform. For public web flows write a flow file and run `scripts/flow_capture.py` (desktop 1440px and mobile 390px). For logged-in flows, ask the user to sign in in the browser first, then continue with the browser tools. For native apps, use the user's screenshots or recordings, or computer use if the user allows it.
2. **Capture every state:** entry point, empty, loading, filled, error, validation, success, edge cases (no results, long text, slow network, offline, permission denied, second language).
3. **Measure:** steps and screens to complete, taps or clicks, fields, required vs optional inputs, time to complete where measurable, reading level of key copy. Mark anything not measured as "not measured".
4. **Review visually:** read every screenshot (split tall captures). Look for unclear copy, missing feedback, dead ends, inconsistent states, contrast, touch targets, broken RTL.
5. Check the feature against the needs checklist and the user's extras.

## Phase 5: Benchmark

Launch subagents in parallel, one per group of 3-5 products, each with the template in `references/agent-template.md`. Every agent walks the **same flow steps and states** so results line up, captures screenshots per step where possible, and fills the needs checklist per product. Blocked, login-only, paywalled, offline or bot-protected flows are reported as such, never guessed. Mark anything seen only in marketing pages, help docs or videos as "from docs, not tested".

Build the **feature matrix**: rows are needs and sub-features, columns are products, cells are ✓ full / ◐ partial / ✗ missing / ? not seen, each with a one-line note.

## Phase 6: Score

Use `references/rubric.md` (8 feature dimensions with anchors), weighted by the user's ranked needs and the research. State the weights. Mark anything judged from docs or text only as "inferred".

## Phase 7: Outputs (only the ones chosen)

Build each HTML output as a page (load the `artifact-design` skill first if publishing artifacts), publish as a private artifact, and also write a standalone copy to the user's folder with `scripts/export_standalone.py`.

- **Feature brief** (`templates/feature-brief.html`): the feature and its needs, ranked user expectations, best practices and anti-patterns, relevant standards and rules, benchmark numbers. Every point cited.
- **Feature benchmark report** (`templates/feature-report.html`): verdict and score, key numbers (steps, clicks, fields vs the best), scorecard, feature matrix, side-by-side flow comparison (same step, every product), issues by severity in the format Problem → Screenshot → Who does it better → Research reason → Fix, the 10 best patterns seen, what the user's feature already does well, roadmap (quick fixes / next version / later), method and limits.
- **Feature spec** (`templates/feature-spec.md`, markdown): problem, needs, user stories, the target flow step by step, every state with its copy, acceptance criteria (Given/When/Then), edge cases, analytics events, accessibility and localisation requirements, out of scope, open questions.
- **Component kit** (`templates/component-kit.html`): for each issue or new sub-feature, a before screenshot, a real-world reference and verified components for HTML, React and CSS stacks (or native components when the product is a mobile app). Each component: exact URL, where on the page, screenshot captured with `scripts/screenshots.py components`, licence, pure CSS vs JS. Start from `references/ui-sources.json`.
- **Resource directory** (`templates/resource-directory.html`): vetted libraries, SDKs and services for building this feature (e.g. a search engine service for search, a payments SDK for checkout), with licence, pricing tier, stack, RTL support, GitHub stars and Copy buttons for verified hooks. Run `scripts/check_sources.py` first. List dropped options with the reason.
- **Build prompt** (markdown): tells another Claude session to read the outputs and build or fix the feature in the user's stack. Include the spec, hard requirements, states and copy, the fix list, components and licences, data and API needs, and test cases from the acceptance criteria.

Finish with a short summary in chat: links, files saved, the top 3 findings, the single biggest gap, and anything unverified.

## Rules

**Scope and input**
1. The feature is the subject. Look at the rest of a product only where it affects the feature (e.g. how people reach it). Flag anything wider before going deeper, and suggest website-benchmark for whole-site work.
2. The user's needs come first. Every benchmark product, check and score must trace back to a stated need or a cited finding.
3. Input is a feature plus any form of product (URL, app, screenshots, repo, idea). Read extras first and use them throughout.

**Asking before acting**
4. Questions are multiple choice, pre-filled, with Skip and Other.
5. Confirm scope twice (proposal, then Start · Edit again · Cancel).
6. Nothing heavy runs before Start.
7. Stop at the spec and build prompt. Never build, change code or publish anything unless the user asks separately.

**Evidence and honesty**
8. Every claim has evidence (screenshot, measured number, observed text) or a cited source.
9. Label inferences, estimates and "from docs, not tested".
10. Report gaps (blocked, login-only, paywalled); never fill them with guesses.
11. Compare like with like: same flow steps, same states, same platform.

**Browsing: ask first**
12. Logins: ask; the user signs in themselves in the browser, then continue. Never type passwords or create accounts, including trial accounts on competitor products.
13. Forms: never submit a form, place an order, send a message, book, pay or delete without an explicit yes for that action. Stop the flow at the last step before submission and capture it.
14. Cookies: ask which choice to make; without an answer, decline non-essential cookies.
15. CAPTCHAs and human checks: ask the user to complete them; never solve them.
16. Downloads and app installs: ask first, stating name, source and size.
17. Use only test or dummy data in inputs (e.g. "test search", placeholder names); never the user's personal data.

**Content and licences**
18. Copy commands come only from a resource's own repo or docs, never from memory.
19. Show every component's and library's licence; mark paid tiers.
20. Never copy competitors' branding, copy text or images into the spec; describe the pattern instead.
21. Never translate Arabic or other languages literally; flag uncertain wording for native review.

**Tools, data and outputs**
22. Use paid analytics or research tools only if connected; otherwise public data plus the user's extras.
23. Collect no personal data from any product; keep the user's extras local.
24. Outputs are private, saved to the user's folder, and never sent or shared without an explicit yes.

## Files

- `scripts/flow_capture.py`: walks a feature flow from a JSON step list and screenshots each step on desktop and mobile; stops before submit-like actions unless confirmed.
- `scripts/screenshots.py`: page captures, component captures at an anchor, crops and contact sheets.
- `scripts/check_sources.py`: verifies UI resource sites, llms.txt, GitHub repos, skills and MCP hints.
- `scripts/export_standalone.py`: embeds images into HTML for standalone files.
- `references/questions.md`, `feature-presets.md`, `research-playbook.md`, `rubric.md`, `agent-template.md`, `ui-sources.json`.
- `templates/`: feature brief, feature report, feature spec, component kit, resource directory.
