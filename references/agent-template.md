# Benchmark subagent prompt template

Fill the placeholders and launch one general-purpose subagent per group of 3-5 products, in parallel, in the background.

---
You are benchmarking ONE feature, {FEATURE}, across products, to compare with {USER_PRODUCT} (status: {STATUS}). Focus only on this feature and how people reach it; ignore the rest of each product. Load WebFetch and WebSearch via ToolSearch ("select:WebFetch,WebSearch"). If browser tools (mcp__Claude_Browser__*) are available, use them to walk the flow and take screenshots; save them to {IMG_DIR} named `<product>_<step>_<d|m>.jpg`.

The user's ranked needs:
{NEEDS}

Walk these flow steps on every product, in this order, on {PLATFORMS}:
{FLOW_STEPS}

Capture these states where you can reach them: {STATES}

Products:
{PRODUCT_LIST}

Rules: do not log in, create accounts (including free trials) or submit anything: stop at the last step before submit, pay, book, send, post or delete, and capture it. Type only dummy data (e.g. "test", "Jane Test", "test@example.com" only into fields that will not be submitted). Decline non-essential cookies; if only "Accept" exists, leave the banner. Never click CAPTCHAs or human checks: report the product as blocked. If the feature is behind a login or paywall, say so and use public docs, help pages or official videos instead, marking every point "from docs, not tested". Never guess.

For EACH product report concisely:
- Entry point: where and how the feature is reached, labels used
- Flow: each step in one line (what the screen asks, inputs, defaults), plus counts: steps, screens, clicks/taps, required fields
- States: how each listed state looks and what it says
- Needs checklist: ✓ / ◐ / ✗ / ? for each need, with a short note
- Standout sub-features and microcopy worth learning from (describe, do not copy text verbatim beyond a few words)
- Weaknesses and friction
- Accessibility and language notes you can observe (labels, focus, contrast, RTL)
- Scores 0-10 on the 8 rubric dimensions (Discoverability, Flow efficiency, Completeness, States and errors, Clarity and copy, Interaction and visual, Accessibility, Trust and control), each with one-line justification; mark "(inferred)" where not walked
- Screenshot file names per step

Finish with a ranking for this feature and the 10 best concrete patterns you saw (which product, which step, how it works, which need it serves). Report only what you observed. About 1200-2000 words.
---

## Component search subagent (for the component kit)
Give each agent one group of sources (Tailwind kits / React-animated / CSS galleries / native UI kits when the product is a mobile app) from `ui-sources.json` and the list of needs (one per issue or new sub-feature). For each need: best component plus runner-up, EXACT URL, WHERE on the page (menu path and example position), why it fits and what to adapt, free or paid and licence, pure CSS vs JS, accessibility and RTL notes. Every link must be opened and verified. Flag components to avoid (gimmicky, inaccessible).

## Library and service search subagent (for the resource directory)
Find libraries, SDKs and services that implement the hard parts of {FEATURE} (e.g. search engines, date pickers, payment SDKs, form validation, notification services). For each: URL, what it covers, licence and pricing tier, stack, self-hosted or SaaS, accessibility and RTL notes, GitHub repo and stars, install command copied from its own docs. Open and verify every link.
