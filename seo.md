# SEO / AEO / GEO — ranking + answer-engine + generative-engine

Three distinct pillars, keep them straight:
- **SEO** — classic search ranking (Google blue links).
- **AEO** — Answer Engine Optimization (featured snippets, PAA, direct answers).
- **GEO** — Generative Engine Optimization (getting cited inside AI answers:
  ChatGPT / Claude / AI Overviews). NOT "Geographic."

## Approved-list first

For client SEO, read and conform to the client's approved keyword/prompt `.xlsx` BEFORE
building from Semrush/GSC. Tool data validates and prioritizes; it does not CHOOSE the
keywords. The client's approved list wins.

## Grounding tools (live data)

- **GSC MCP** (`google-suite` / gsc) — real clicks/impressions/CTR/position + real queries
  for FAQ sourcing. Use exact property URL from `list_properties`.
- **Semrush MCP** — keyword gap, phrase_questions, position tracking, competitor sets.
- **SearchApi.io** — real People-Also-Ask + AI-Overview verification when Semrush units are
  out or the client isn't in GSC yet. Save raw JSON to the project's `serp-verify/`.
- `/seo-suite` composite skill chains these with the installed SEO skills.

## On-page + AEO/GEO build

- True heading hierarchy (one H1 → question H2s → H3 FAQ) so the answer engines can parse
  Q→A pairs. (Full structure rules in `writing.md`.)
- **Definition block** near the top (crisp "X is …" for snippet capture).
- **Tables** for comparisons — machine-readable, snippet-friendly.
- **Schema stack (JSON-LD):** appropriate `@graph` — Organization/School, WebPage,
  BreadcrumbList, FAQPage, Article as fits. Append the JSON-LD in the same deliverable doc
  (per the deliverables rule, not a standalone `.json`). Verify with Rich Results.
- FAQ questions traceable to GSC/Semrush real queries, never invented.
- Sourcing cited inline (e.g. "CBSE Affiliation Bye-Laws 2018 (cbse.gov.in)") — feeds both
  E-E-A-T and AI citation.

## AI-visibility measurement (GEO scoring)

- One engine-aware scorer shared by capture + rescore (don't fork scoring logic — it drifts
  and produces false counts). A reconciliation guard should ABORT the build on drift between
  the scorer's verdicts and the deck/xlsx.
- Verify AI presence by TEXT-checking the actual engine output per prompt, not by assuming.
  Track presence per engine (Claude / ChatGPT / AI Overview) separately.

## Meta/title mechanics (every article ships this block — make it checkable)

- **Title tag:** ~50-60 characters (Google truncates past ~600px). Primary keyword near the
  front, active/specific, not a restated H1.
- **Meta description:** ~150-160 characters. States the value/answer + has a reason to click;
  never truncated mid-word if avoidable. Not filler ("Learn more about X on our site").
- **Alt text:** descriptive, no "image of" / "picture of" prefix — describe what matters for
  someone who can't see it. ~125 characters is a soft target for a simple photo/icon, NOT a
  hard cap — WCAG asks for enough description to convey the same information, not a length
  limit, and truncating a data chart or infographic to fit 125 chars strips the information
  that made the image worth including. For a complex visual, write the full description
  needed and use a long-description pattern (adjacent caption, `aria-describedby`) rather than
  cutting it short.
- Bake these as length asserts in the build script, same discipline as the dash check — a
  title/description that's the right idea but wrong length is exactly the kind of thing that
  ships unnoticed without a runnable check.

## Deploy hygiene for rank

`robots.txt` (RFC-clean) + `sitemap.xml` + `llms.txt` + `.well-known/ai-faq.json` where the
project uses them; canonical/OG/geo meta; submit sitemap in GSC post-live; run Rich Results.

Packaging (docx + JSON-LD in one doc) → `workflow.md`. Prose rules → `writing.md`.
