# Content-type playbooks

All types inherit `writing.md`'s non-negotiables (dashes, tells, sourcing) plus `craft.md` and
`sourcing.md`. This file is the structural/format layer per content type. Ranking/schema layer
for articles → `../seo.md`. Deliverable packaging → `../workflow.md`. Visual layer → `../design.md`.

## Articles (AEO/GEO/SEO-rich, thought-leadership, blog)

These are acceptance criteria, not preferences — a client has rejected a batch on exactly
these before.

1. One true H1, then real H2 styles (Word/HTML heading styles, NOT bold Normal) — export must
   yield real `<h1>/<h2>/<h3>`.
2. Every subheading in QUESTION format.
3. Each section ≥ 2 paragraphs / 120+ words, counted from the TRUE rendered body (Normal paras
   + heading text + table-cell words, H1 through JSON-LD) — paragraph-only counting
   under-reports by ~150-200w.
4. Target keywords used naturally everywhere — not stuffed, not absent.
5. Conclusion: single paragraph, ≤100 words.
6. FAQ = its own H2 ("Frequently Asked Questions") + one H3 per question (prefixed `Q:`),
   answers 30-50 words.
7. FAQ questions traceable to REAL Google queries — validate via GSC real queries or Semrush
   `phrase_questions`; never invent them.
8. 100% unique, human-written, plagiarism-free, no duplicate content.

**Length floor: 1800+ words of body** (excluding dev brief + JSON-LD) unless told otherwise.
Budget 11-13 question-H2 sections up front (~130-150w each) to actually clear the floor —
writing 8 sections then patching under-shoots it every time. This is a floor for a topic that
legitimately supports it, not a padding target — a genuinely narrow long-tail keyword that runs
out of real substance at 1200w gets cut short and flagged for a broader angle instead, not
stretched with rule-of-three padding or restated sections to hit the number. Budgeting sections
to a word count is exactly the mechanism that produces the filler patterns `craft.md`'s AI-tell
sweep exists to catch — use it to plan real depth, not to justify padding.

**Skeleton (client-approved gold pattern):** `Title` style = topic label → `Heading 1` = the
article H1 (often itself a question, sometimes with a parenthetical year) → `Heading 2` =
sections, all questions → `Heading 3` = sub-points / FAQ questions. Intro: ~3 Normal paragraphs
before the first H2, sources cited inline (e.g. "CBSE Affiliation Bye-Laws 2018 (cbse.gov.in)").
A comparison H2 sitting directly over a table with 0 body paragraphs is fine, that's
intentional. Dev-brief block (slug/title tag/meta/keywords/prompt targets/schema) stays under
its own `Title`/`Heading 2`.

**Commercial-intent framing:** for "best/top X" or "X with fees" terms you can't rank or price
factually, frame as "how to compare / how to choose" rather than a ranked listicle — captures
the same intent, stays truthful.

**Reuse workflow (existing approved copy, wrong structure):** don't rewrite from scratch —
extract the copy (python-docx), remap into true H1/H2/H3 with question subheads, extend past
1800w with real PAA-sourced sections, encode per-client hard rules as build-script asserts
(e.g. "no 'Best' in H1"), write to a `-v2/` directory and leave originals until sign-off. Reused
copy runs leaner per section (~120-140w), so budget 12-13 sections instead of 11.

**Batch production:** one shared builder module (styles, keyword-bold, dash assert, JSON-LD,
word-count QA) + one content-spec file per batch/article. Keeps per-client hard rules
(banned H1 words, keyword lists) as asserts in the builder, not tribal knowledge.

Deep AEO/GEO technical layer (definition blocks, schema stack, GSC/Semrush grounding, deploy
hygiene) → `../seo.md`.

## Landing pages

Generic conversion-copy frameworks (headline formulas, page-structure templates, CTA formulas)
→ the separate `copywriting` skill's `references/copy-frameworks.md` — use those as the
starting structure. The rules below are the house-specific corrections layered on top:

- **Sibling pages off one shared design system differentiate on structure, not hue.** Shifting
  just an accent colour makes two pages "read as the same page twice" — a swapped accent
  touches ~4% of the visual surface. Keep one shared base stylesheet, add a thin per-page
  identity layer that overrides *photo treatment* (grayscale vs full-colour, scrim weight) and
  adds *one signature component the sibling doesn't have*; use the accent as a saturated FILL
  on that component, not recoloured hairlines everywhere.
- **A brand-new offering with no track record never fakes proof.** No fabricated alumni,
  placements, or outcomes for something with no graduating cohort. Show the parent
  programme/product's real record as the explicit destination ("these years ARE that
  programme; these are that programme's outcomes"), drop the alumni section entirely, soften
  superlatives, and confront the "it's unproven" objection head-on rather than hiding from it.
- Real content is visible by plain CSS default, always — never gate a section's visibility on
  JS executing at the right moment (`opacity:0` + IntersectionObserver/ScrollTrigger waiting to
  flip it). Motion is an additive enhancement only. See `design_foundations` memory for the
  full mechanism and why it broke twice on the same build.

## Email / newsletter

- **Subject line ~40-60 characters** (mobile clients truncate further); preheader text is a
  second, separate line of copy, never a restatement of the subject.
- **One primary CTA per email.** Secondary links are fine below the fold; don't compete two
  CTAs for the same click.
- **Footer compliance:** physical/registered sender identity + a working unsubscribe link on
  every marketing send, non-negotiable regardless of platform (CAN-SPAM/general anti-spam
  practice) — check before every send, not just the template.
- Same craft/dash/tell rules as any other prose; same sourcing rules if the email cites a stat.
- Nurture sequences: one idea per email, not a compressed brochure — if it needs three CTAs
  and five proof points, that's three emails.

## Case studies / testimonials

- Structure: problem → what was done → the result, in that order, with the result being a real
  verifiable number or an actual customer quote, not a vague "significant improvement."
- **Customer quotes are verbatim, not paraphrased** — same discipline as a competitive claim
  (`sourcing.md`). Get permission to publish before use; never invent or composite a "typical
  customer" quote.
- If a metric appears in the quote, verify it's the client's own number, not one you supplied
  to them for approval.

## Brochures / decks / client-facing reports

- **Never reveal production methods or tools.** No "built in X", no aspect ratios, no library
  names, no workflow exposition. Show the idea, hook, copy, and WHY it lands for their
  audience — never the HOW. Scrub any sentence explaining how a thing was made rather than what
  it is or why it works, before send. This is how the agency stays indispensable.
- **Sober design, not AI-colourful.** One typeface with clear hierarchy, ONE restrained accent
  + a muted grey, generous whitespace. No rainbow, no font-variety, no over-decoration — that
  combination reads as machine-generated and cheapens real work.
- **For a PROSPECT: sell the diagnosis and urgency, never hand over the plan.** Show findings,
  withhold remedies. Name what's deliberately withheld on its own slide ("what is deliberately
  not in this document") — a declared gap converts to a meeting, a hidden gap just reads as a
  short deck. Give them what only measurement produces (their invisible position, a
  competitor's long-running campaign); hold what only judgement produces (which categories,
  which price band, which message). Pair every claim with a screenshot they can re-verify
  themselves — proof a client can check lands harder than proof they must trust.
- **Be honest about limits in the same document.** What we don't know, what we can't promise,
  what a competitor does better. Conceding the weak points is what makes the strong ones
  credible.
- **Scrub the boring cells too, not just the marketing copy.** Internal file paths, staff first
  names, and agency-internal phrasing land in "documentation-feeling" cells — source citations,
  changelog notes, audit-trail rationale — that a copy-focused scrub misses because they don't
  read like marketing. Before shipping, run a leak scan across every file part (for Office
  formats: `zipfile.ZipFile(f).namelist()`, substring-match each XML part against a banned-term
  list) plus a malicious-content sweep (script-injection patterns, secrets patterns, macro
  content types, embedded executables — note `ppt/printerSettings/*.bin` is a benign PowerPoint
  artifact, not a hit).
- Format: `.docx` for narrative, `.pptx` for anything pitched or long/exhaustive (a 20-page
  docx doesn't get read; the same content paced one idea per slide does), `.xlsx` for anything
  tabular. Full rules → `../workflow.md`.

## Scripts (video, reels, presenter)

- Write STRAIGHT scripts — full sentences of what gets said, NOT time-cued shot lists
  (no "[0:00-0:03] Hook shot"). Time-cues and shot directions are production mechanics, which
  the client-facing rule above says stays internal/undisclosed anyway.
- Same craft + dash + tell rules as any other prose — a script is spoken content, not exempt.
- Discipline-lens applies here too: a presenter script should sound like the actual person's
  field of thinking, not a generic narrator voice.
- Not every spoken format is the same shape — a short reel/presenter script is one continuous
  read; a webinar/podcast script additionally needs a cold open and explicit segment breaks; a
  chatbot/IVR script is branching (fallback line for every unmatched input), not linear at
  all — confirm which shape before writing, don't default the reel pattern onto a branching one.

## UX / product microcopy (buttons, errors, empty states, form labels)

Component copy, not persuasive prose — different register and a hard length budget:
- **Button labels:** 1-3 words, verb-first ("Save changes", not "Submit").
- **Error messages:** say what happened + what to do about it, plainly — never blame the user,
  never a vague "Something went wrong" when the real cause is knowable ("That email's already
  in use — try signing in instead.").
- **Empty states:** one line on what belongs here + one action to fill it, not filler copy.
- **Tooltips/form labels:** as short as still-clear; a tooltip that needs two sentences is a
  sign the UI itself needs a label, not more copy.
- Same dash/tell rules apply, but craft rules like "stress position" and "varied rhythm" mostly
  don't — a 3-word button label doesn't have rhythm to vary.

## Press release

- **Dateline first line:** `CITY, Month Day, Year — Company Name`.
- **Inverted pyramid, not narrative build:** the single most newsworthy fact goes in the first
  sentence, not the third paragraph. A journalist reads one sentence and decides; don't make
  them dig for the news.
- **At least one real, attributed quote** from a named spokesperson — same sourcing discipline
  as anywhere else, never invented, never generic ("we're thrilled...").
- **Boilerplate paragraph at the end:** the standard "About [Company]" description, reused
  verbatim release to release, not rewritten each time.
- **Media contact block** (name, email, phone) at the bottom — a press release's whole point is
  public distribution with a reachable contact, so this is the one deliverable type where a
  real staff name in the copy is correct, not a leak.
- **Embargo, if any:** `EMBARGOED UNTIL [date/time]` at the very top, never buried.
- No sales tone. A release that reads like an ad gets spiked by the journalist reading it —
  state the facts, let the quote carry the color.

## White paper / gated long-form guide

- **Executive summary up front**, standalone-readable — the whole argument in roughly one
  page, because a white paper's reader may stop after the summary. This differs from an
  article's intro, which is a hook, not a synopsis.
- **Argument-driven headings, not search-intent headings.** Don't force the article playbook's
  question-subhead AEO structure onto this — headings organize the argument's logic for an
  expert reader, not a snippet.
- Same sourcing rigor as an article, but citations can run denser (footnotes/endnotes are
  fine) since the audience is already expert, not scanning for a quick answer.
- **Gating check:** if it's lead-gen gated, the exec summary alone must justify the email/form
  ask — don't gate something too thin to be worth a real address.

## RFP / proposal response

- **Point-by-point compliance format, not narrative prose.** Mirror the RFP's own
  numbering/section structure exactly so an evaluator can tick off each requirement — a
  well-written narrative that doesn't map 1:1 to their ask scores worse than a plain,
  compliant answer that does.
- Restate the requirement briefly, then answer it directly — don't make the evaluator hunt for
  where 4.3 got addressed.
- Still governed by the client-facing packaging rule above: sell capability and fit, never
  reveal internal production methods, tooling, or margin structure beyond what's explicitly
  asked for.
- A compliance matrix (requirement / how we meet it / evidence) is often a required attachment
  in its own right — build it as a real table (xlsx), not a paragraph pretending to be one.

## Social captions & ad/display/banner copy

**Display copy IS content.** Headlines, support lines, carousel cards, ad primary text, CTAs
all go through the same gate as an article: `craft.md`'s tell-sweep and the 7 craft rules, then
`ai_tell_lint.py` before sign-off. This matters MORE in short copy, not less — an 8-20 word
banner has nowhere to hide one tell; a negation-tic line ("Not a certificate. Not a mentor.")
IS the whole ad.

**Before drafting copy for approved creative — check the format first.** A numbered image
sequence (`1.png`...`4.png`) with a matching design system (shared wordmark position, one
narrative arc across cards) is often ONE carousel, not N standalone ads. The copy structure is
entirely different: one shared intro text + short per-card headlines, versus N full standalone
posts. Confirm before drafting.

**Captions complement the creative, they don't restate it.** If the banner image already bakes
in the price, a name, a list — don't put that same fact back into the caption. Read the image's
own baked text first, then pull complementary, true, on-brand facts from adjacent assets
already built for the account (the landing page, the brief) — eligibility criteria, dates,
deadlines, curriculum structure, a CTA the card itself doesn't carry.

**Caption standard (client social, IG-first unless told otherwise):** long, complementary
captions (100+ words) with paragraph breaks (3-4 paragraphs), hashtags on their own line at the
end. Every caption ships with CTA + UTM link + hashtags; stack CTAs (Save / Follow / prompt)
where the format fits.

**Two honest limits on ad-copy linting** (don't over-correct against the format): burstiness
has a natural floor in short display lines — vary what you can and stop. Low lexical diversity
is sometimes correct on purpose (repeating product vocabulary across an ad set) and directly
conflicts with the elegant-variation ban — know which rule actually applies before "fixing."

Compliance carries over regardless of source format — a client's BLOCKED-claims list applies
even to copy for a channel where the live site itself states the claim.
