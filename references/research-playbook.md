# Research playbook

Every finding: one sentence, a cited URL, the year of the data, and "estimate" where it is one. Prefer primary sources. Run modules as parallel subagents (general-purpose, WebSearch + WebFetch); give each the feature, the ranked needs, the platforms and the output format below. Keep every module tied to the feature: drop findings that do not change how the feature should work.

## Output format for every finding
`- <finding> — <what it means for this feature> [source: <URL>, <year>] (estimate?)`

## Module A: Feature best practices
| Area | Questions | Good source types |
|---|---|---|
| Usability research | What do studies say makes this feature work or fail? | Baymard Institute, Nielsen Norman Group, GOV.UK Design System, academic HCI papers |
| Platform guidance | What do the platforms recommend for this pattern? | Apple Human Interface Guidelines, Material Design, Microsoft Fluent, web.dev |
| Patterns | Named patterns and when to use each (e.g. faceted search vs simple filters, stepper vs single page checkout) | Pattern libraries, design system docs (Shopify Polaris, Atlassian, Carbon, GOV.UK) |
| Anti-patterns | Known mistakes and dark patterns to avoid | NN/g, Baymard, deceptive.design |
| Numbers | Typical completion or abandonment rates, recommended field or step counts, performance budgets | Baymard benchmarks, industry studies; label estimates and year |

## Module B: User expectations
- The user's extras first: tickets, reviews, analytics funnels, interviews. Quote counts, not personal data.
- Public reviews of benchmark products (app stores, G2, Reddit, Trustpilot) filtered to this feature: recurring praise and complaints.
- Output: a ranked list of expectations, each with its evidence.

## Module C: Standards and rules (only those touching this feature)
- Accessibility: the WCAG 2.2 AA criteria this feature must meet (e.g. 3.3.1 error identification for forms, 2.5.8 target size, 4.1.3 status messages for search results). Verify criteria numbers on w3.org.
- Privacy and consent: data collected by the feature, consent needs (e.g. location for a store finder), retention.
- Payments, age, identity or industry rules where they apply (e.g. Strong Customer Authentication for checkout).
- Performance: Core Web Vitals thresholds if the feature is on the web (verify current values on web.dev).

## Module D: Market context (only if the user named markets or languages)
Languages and RTL, local payment or identity methods, local platforms and expectations that change this feature. Reuse `../website-benchmark/references/markets/` if installed, always re-verified.

## Module E: Benchmark discovery
Three buckets: direct competitors, same category in other markets, best-in-class for this feature from any industry. Optionally open-source projects that implement it well. Return name, URL, platform, bucket, one-line reason tied to a need, and whether the feature needs a login or payment to see. New candidates go back to the user for approval.

## Turning research into decisions
1. **Rubric weights:** raise the dimensions linked to the top needs (see `rubric.md`).
2. **Needs checklist:** one yes/no line per need or finding, e.g. "Shows result count before applying filters?", "Guest checkout available?", "Error message says how to fix?", "Works with Arabic input and Latin transliteration?". The same checklist is used on every product.
3. **Spec requirements:** states, copy rules, accessibility criteria, rules and numbers the spec must hit.
