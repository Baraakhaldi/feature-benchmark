# feature-benchmark

A [Claude Code](https://claude.com/claude-code) skill that benchmarks **one feature** of your app, website or product idea (search, onboarding, checkout, booking, filters, notifications, dashboard, chat, settings, sharing, anything) against the products that do it best, starting from **your needs**.

It is the feature-level sibling of [website-benchmark](https://github.com/Baraakhaldi/website-benchmark): instead of auditing a whole company website, you say which feature and what it must do, and everything (which products to compare, what to measure, how to score) follows from that.

## What you get

1. **Feature brief:** ranked needs, best practices, anti-patterns, pattern choices, what users say, the standards and rules that apply, and a needs checklist. Every point cited.
2. **Feature benchmark report:** your feature scored against 5–15+ products on 8 feature dimensions, a feature matrix (✓ ◐ ✗ ?), the same flow step side by side across products with screenshots, issues as *Problem → Screenshot → Who does it better → Research reason → Fix*, the 10 best patterns and a roadmap.
3. **Feature spec:** user stories, target flow, every state with its copy, acceptance criteria, edge cases, accessibility, analytics events.
4. **Component kit** and **resource directory:** verified components, libraries and services to build it, with licences.
5. **Build prompt:** a ready-to-paste prompt for another Claude session to build or fix the feature.

## How it works

1. **Intake:** the feature, your needs, and the product in any form (URL, app, screenshots, Figma, repo, or "not built yet"), plus extras like analytics, tickets or reviews.
2. **Questions:** multiple choice, pre-filled from feature presets: scope, status, users, ranked needs, success signal, platforms, where to look, depth, outputs, permissions.
3. **Scope check, twice:** a proposal you can edit, then *Start · Edit again · Cancel*.
4. **Research:** feature best practices, user expectations, relevant standards, and benchmark discovery across direct competitors and best-in-class products from any industry.
5. **Audit:** your feature walked step by step on each platform, every state captured and measured.
6. **Benchmark:** parallel agents walk the same steps and states on every product.
7. **Score and outputs.**

Browsing is careful by design: you sign in yourself where needed, flows stop before any submit, pay, book, send or delete, only dummy data is typed, CAPTCHAs are left to you, and gaps are reported, never guessed.

## Install

```bash
git clone https://github.com/Baraakhaldi/feature-benchmark.git ~/.claude/skills/feature-benchmark
```

```bash
pip install playwright pillow
```

```bash
python -m playwright install chromium
```

## Use

> Benchmark the checkout in my store https://example.com — it needs guest checkout, Apple Pay and fewer steps

or invoke `/feature-benchmark`.

## Contents

| Path | What it is |
|---|---|
| `SKILL.md` | Workflow and rules |
| `scripts/flow_capture.py` | Walks a flow from a JSON step list, screenshots each step on desktop and mobile, stops before submit-like actions |
| `scripts/screenshots.py` | Page and component captures, crops, contact sheets |
| `scripts/check_sources.py` | Re-verifies resource sites, repos, skills and MCP hints |
| `scripts/export_standalone.py` | Embeds images into HTML for standalone files |
| `references/feature-presets.md` | Flow steps, states, needs and benchmark ideas for 15 common features |
| `references/questions.md` | Question bank |
| `references/research-playbook.md` | Research modules and how findings become weights and checks |
| `references/rubric.md` | 8 feature dimensions with anchors, and issue severity |
| `references/agent-template.md` | Prompts for benchmark, component and library subagents |
| `references/ui-sources.json` | Vetted UI and CSS resources |
| `templates/` | Feature brief, feature report, feature spec, component kit, resource directory |

## License

MIT
