---
name: web-practice
description: The consolidated house system for all web design, front-end development, content/copy writing, SEO/AEO/GEO, and client-deliverable work — Johnny's standing dos/donts plus hard-won standards and traps. Use when building, designing, writing, reviewing, or shipping ANY web page, creative, deck, brochure, document, article, report, or client-facing deliverable. Read the matching reference file before doing the work; verify against it before calling done.
---

# Web Practice — the house system

One system for the whole web lifecycle: **design → develop → write → rank → ship**.
This file holds the always-fire non-negotiables. Each domain has a reference file
(below) — read it before that kind of work, verify against it before "done".

Provenance: distilled from Johnny's feedback and learnings across real client engagements.
Keep a deeper canonical knowledge base (an Obsidian vault, a wiki, whatever you use) if
useful; this skill is the self-contained working spine, standalone so it holds even when
that deeper source isn't readable mid-session. **Hub + sync rule** (one owner per fact,
others point): pick ONE canonical home per fact and update it there, don't fork a
duplicate. When a new learning lands: operational rule → the matching skill file here;
deep teaching → your own canonical note; recall hook → your memory system, if you run one.

## Non-negotiables (fire on EVERY deliverable, no exceptions)

1. **No em/en dash in outward prose.** Never `—` or `–` in any client-facing content.
   Use spaced hyphen ` - `. En-dash `–` allowed ONLY in numeric/time ranges (`Years 2–3`,
   `09:00–09:45`). Bake as a runnable assert in the build script — intent is not enough
   (a doc shipped with 18 em-dashes because it was only *meant* to be clean). Verify from
   the RENDERED output, not the source.
2. **Sweep for AI-writing tells before sign-off.** Banned vocab, negative parallelism,
   copula avoidance, rule-of-three padding, "-ing" tails, filler closers. → `writing.md`.
   AI-sounding prose is a credibility violation, same tier as em-dashes.
3. **Sober design, never AI-colourful.** One typeface + clear hierarchy, ONE restrained
   accent + a muted grey, generous whitespace. No rainbow, no font-variety, no
   over-decoration. Greyscale-test the hierarchy. → `design.md`.
4. **Never reveal our production methods or tools to a client.** Show the idea, hook,
   copy, and *why* it lands — never the *how* (no "built in X", no aspect ratios, no
   library names, no workflow). Revealing mechanics ends the business. Scrub before send.
5. **Every stat has a real named source + year**, cited in TWO visible places for
   B-school work (on-creative credit AND in-caption `Source:` line). Hard-verify
   superlatives ("largest" was FALSE once). Drives E-E-A-T and AI citation.
6. **Verify by observation before claiming done.** Re-run the actual check; believe
   nothing not observed. Non-negotiable on prod deploy, migrations, client sign-off.
   "It should work" / DOM numbers / "a process launched" are NOT verification. → `workflow.md`.
7. **Pick the format to the content, Office over markdown.** Client-facing =
   `.docx`/`.pptx`/`.xlsx` always. Tables → `.xlsx`. Narrative → `.docx`. Decks → `.pptx`.
   Markdown only for internal notes/guides/memory. → `workflow.md`.

## The reflexes (how to work, not what to ship)

- **Be proactive.** Spot the whole problem-*class* and propose the better approach BEFORE
  Johnny finds each defect. Codemod mechanical work; suggest a lint/assert that prevents
  recurrence. Don't react item-by-item.
- **Design/build from first principles, then verify — don't pattern-match a reference
  until it "looks right".** Reason it, measure it (WCAG ratios, word counts), critique it.
- **Extract shared components** when a shape repeats (a Paper/panel, a builder, a CSS
  block) — one source, not inline copies that drift.
- **Version before any substantial rewrite:** back up to `/versions/<file>.YYYY-MM-DD-HHMM.bak`.
- **Keep disposable artifacts local** (previews, compares → `python -m http.server`); never
  deploy to Vercel/FTP unless explicitly asked.
- **Lazy first (ponytail):** stdlib/native/existing-dep before new code; shortest working
  diff; mark deliberate simplifications with a `ponytail:` comment. Leave one runnable
  check behind non-trivial logic.

## Route to the domain file

| Doing this…                                                  | Read           |
|--------------------------------------------------------------|----------------|
| Any visual: creative, deck, brochure, landing page, graphic  | `design.md`    |
| Front-end code, running/verifying the app, build/QA          | `development.md` |
| Any prose: article, LP, email, brochure, deck, script, caption, ad/UX copy | `writing.md` |
| Ranking work: AEO/GEO/SEO articles, schema, on-page          | `seo.md`       |
| Deliverable format, workflow, deploy, client-facing packaging| `workflow.md`  |

Most real tasks touch 2–3 files (e.g. a client article = `writing.md` + `seo.md` +
`workflow.md`). Read what applies; don't invent rules the files don't state.
