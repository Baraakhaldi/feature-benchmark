# {{FEATURE}} spec · {{PRODUCT_NAME}}

<!-- TEMPLATE: replace every {{PLACEHOLDER}}. Every requirement traces to a need (N#), a research finding [source] or a benchmark pattern (P#). Describe competitor patterns; never copy their text or assets. Mark open decisions in "Open questions", not inline guesses. -->

Version {{VERSION}} · {{DATE}} · Status: draft for review
Built from: feature brief, feature benchmark report ({{N}} products), the user's extras ({{LIST}}).

## 1. Problem
{{2-4 sentences: what users try to do, what goes wrong today (with the measured numbers), why it matters to the business}}

## 2. Needs (ranked)
| # | Need | Evidence | Success measure |
|---|---|---|---|
| N1 | {{NEED}} | {{SOURCE}} | {{e.g. completion rate from X% to Y%, steps from 7 to 4}} |

## 3. Users and context
- **Who:** {{USER_GROUPS}}
- **Platforms:** {{PLATFORMS}} · **Languages:** {{LANGUAGES, incl. RTL}}
- **Entry points:** {{WHERE_PEOPLE_START_THE_FEATURE}}

## 4. User stories
- As a {{USER}}, I want to {{ACTION}} so that {{OUTCOME}}. (N#)

## 5. Target flow
| Step | Screen / component | What the user does | What the system does | Pattern source |
|---|---|---|---|---|
| 1 | {{SCREEN}} | {{ACTION}} | {{RESPONSE}} | {{P# / finding}} |

## 6. States and copy
Write final-direction copy in plain words; flag lines needing native review for other languages.

| State | When it shows | What it shows | Copy (EN) | Copy ({{LANG}}) |
|---|---|---|---|---|
| Empty | {{TRIGGER}} | {{CONTENT}} | {{COPY}} | {{COPY or "needs native writer"}} |
| Loading | | | | |
| Success | | | | |
| Error: {{TYPE}} | | | {{what happened + how to fix}} | |
| No results / no availability | | | | |
| Offline / slow | | | | |
| Permission denied | | | | |

## 7. Acceptance criteria
- **AC1** (N1) Given {{CONTEXT}}, when {{ACTION}}, then {{RESULT}}.

## 8. Edge cases
- {{EDGE_CASE}} → {{EXPECTED_BEHAVIOUR}}

## 9. Accessibility and localisation
- WCAG 2.2 AA criteria for this feature: {{LIST with how each is met}}
- Keyboard and screen-reader behaviour: {{FOCUS ORDER, ANNOUNCEMENTS}}
- RTL and mixed-direction text, number and date formats: {{RULES}}

## 10. Data, APIs and analytics
- Data needed: {{FIELDS, SOURCES}} · Data stored: {{WHAT, RETENTION, CONSENT}}
- APIs / services: {{FROM RESOURCE DIRECTORY, with licence and tier}}
- Analytics events: `{{event_name}}` ({{properties}}) — measures {{N#}}

## 11. Performance
{{BUDGETS, e.g. results in under 300 ms after typing stops; INP ≤ 200 ms}}

## 12. Out of scope
- {{ITEM}}

## 13. Open questions
- {{QUESTION}} — owner: {{WHO}}

## 14. References
- Benchmark patterns: P1 {{PRODUCT, STEP}} …
- Research: [{{SOURCE}}]({{URL}}) ({{YEAR}})
