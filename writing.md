# Writing — golden standard for all outward prose

Every client-facing word respects these, across every content type: articles, LPs, brochures,
decks, reports, scripts, captions, ad/banner copy, emails. Keep a deeper canonical authoring
guide if useful (this file is the self-contained working summary). Bake checks into the build script's
self-test so a violation fails the build — intent alone once shipped 18 em-dashes. Run
`ai_tell_lint.py` before sign-off. Verify from the RENDERED doc, not the source.

## Non-negotiables (fire on every deliverable)

1. **No em-dash `—` anywhere; en-dash `–` only in numeric/time ranges.** Assert it, don't just
   intend it — full mechanics + codemods → `writing/craft.md`.
2. **Sweep for AI-writing tells** — banned vocab, negative parallelism, copula avoidance,
   rule-of-three padding, filler closers. Applies to display/ad copy as much as articles; an
   8-word banner has nowhere to hide one tell. Full list + toolkit → `writing/craft.md`.
3. **Every stat has a real named source + year, verified live before it ships.** No made-up
   figures, no guessed URLs, no citing yourself. Register + tiering + competitive-claim
   handling → `writing/sourcing.md`.
4. **Never reveal production methods or tools in client-facing copy.** Show the idea and why
   it works, not the how — EXCEPT an RFP/proposal response explicitly asking a vendor-
   questionnaire item ("describe your technical approach/tools/QA process"); answer it, a
   non-compliant narrative scores worse than a plain compliant one. → `writing/formats.md`
   (brochures/decks and RFP/proposal sections).
5. **Client-approved keyword/prompt lists win over tool data.** Semrush/GSC validate and
   prioritize; they don't choose outside the approved list.

## Route to the content-type playbook

| Writing this…                                              | Read                                  |
|--------------------------------------------------------------|--------------------------------------|
| Article / blog / AEO-GEO-SEO-rich content                    | `writing/formats.md` + `seo.md`      |
| Landing page copy                                             | `writing/formats.md` (+ `copywriting` skill for generic frameworks) |
| Email / newsletter                                             | `writing/formats.md`                 |
| Case study / testimonial                                       | `writing/formats.md` + `writing/sourcing.md` |
| Brochure, deck, client report/proposal                        | `writing/formats.md` + `workflow.md` |
| Video/presenter/webinar/chatbot script                         | `writing/formats.md`                 |
| Social caption, ad/banner/carousel copy                       | `writing/formats.md`                 |
| UX/product copy (buttons, errors, empty states)                | `writing/formats.md`                 |
| Press release, white paper, RFP/proposal response               | `writing/formats.md`                 |
| The craft rules, dash mechanics, AI-tell sweep, detector tools | `writing/craft.md`                   |
| Sourcing, citation tiering, competitive claims                | `writing/sourcing.md`                |

Most real tasks touch 2-3 files. Read what applies; don't invent rules the files don't state.
Deeper AEO/GEO/schema layer → `seo.md`. Format/packaging → `workflow.md`.
