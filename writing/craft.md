# Craft — the 7 rules, AI-tell sweep, dash enforcement, detector mechanics

Keep a deeper canonical authoring guide if useful (this file is the self-contained working
summary). Toolkit scripts (`ai_tell_lint.py`, `similarity_check.py`) belong in a `tools/`
directory alongside this skill — see the Toolkit section below. Read before writing, run
`ai_tell_lint.py` before sign-off.
Applies to EVERY authored deliverable — articles, LPs, brochures, ad/banner/carousel copy,
captions, scripts, even internal docs and CVs. Scope-narrowing this to "marketing copy only"
has shipped bad drafts twice; there is no exempt category.

## Core thesis

Pre-AI style authorities (Strunk, Gopen & Swan, Williams, Zinsser, Orwell, Le Guin) and modern
AI-detectors describe the same quality from opposite ends. Detectors crudely measure the
ABSENCE of good writing. The durable move is classic craft, not anti-detector tricks.

## The 7 convergent rules

1. Action in the verb — kill nominalizations (-tion/-ment/-ance as the main noun).
2. Strong word at the END of the sentence (stress position).
3. Old info first, new info last (cohesion chain).
4. Subject and verb close together.
5. Cut every word that doesn't work, then cut again.
6. Simplest concrete word (help not assistance; because not due-to-the-fact).
7. Nouns + verbs carry, adjectives + adverbs decorate.

Plus: real VOICE (Zinsser's "transaction" — lived detail, stated opinion, the one thing no
model fakes) and VARIED RHYTHM (Le Guin — never 4+ same-length sentences running; read aloud).

**Discipline-lens for bylined pieces:** never open with a formulaic credential-drop ("I spent
N years..."), it makes every author sound identical. Write from inside how the author's FIELD
thinks — a systems/IS mind sees feedback loops and debugging, a marketer sees positioning,
finance sees risk-return. Swap-test: if another expert's byline fits the opening, rewrite it.
When no profile is given, infer the mindset from field + role; don't stall to ask for a CV.

## Dashes (hard rule, assert it — don't just intend it)

- **No em-dash `—` anywhere** in outward prose → `assert '—' not in alltext`. Use ` - `.
- **En-dash `–` only in numeric/time ranges** (`digit–digit`, `09:00–09:45`) →
  `assert not re.findall(r'[A-Za-z]\s*–\s*[A-Za-z]', alltext)`.
- Codemod existing: `re.sub(r'\s*—\s*', ' - ', src)` then the prose-en variant
  `re.sub(r'(?<=[A-Za-z])\s*–\s*(?=[A-Za-z])', ' - ', src)`. CAUTION: a blind codemod also
  rewrites dashes inside your own assert strings — re-check the guard line after running it.
- Bake the check as a runnable assert in the build script's self-test, not a final eyeball
  grep — a doc shipped with 18 em-dashes once because the rule was only *meant*, not enforced.
  Verify from the RENDERED output (docx/html), not the source markdown.
- Some clients are stricter still: no `—` or `–` at all, ever, always ` - ` — confirm per
  client style guide.
- This applies to CVs, internal notes, build-script comments in client-visible output —
  anything that reads as a sentence, not only recognized "content" pipelines.

## AI-writing tells to sweep (no single tell is fatal; a cluster is)

- **Banned vocab:** delve, tapestry, testament to, underscore, pivotal, boasts, nestled,
  vibrant, foster, showcasing, highlighting, leverage, crucial, seamless, robust,
  game-changer; `moreover`/`furthermore`/`additionally` as sentence openers.
- **Negative parallelism** ("not just X, but Y" / "not A, it's B") — the #1 GPT signature,
  the single worst habit found in practice. Keep to 0-1 for deliberate effect; rewrite the
  rest into positive, active statements. Watch for it especially in short copy (an 8-word
  banner line has nowhere to hide one).
- **Copula avoidance** — dodging "is/are" for "serves as / stands as."
- **Rule-of-three padding**, superficial "-ing" tails ("…highlighting its importance"),
  weasel attribution ("experts argue"), elegant variation (swapping synonyms to avoid
  repeating a term — note this is sometimes WRONG to chase, see limits below), promo/
  travel-guide gloss, "Challenges and Legacy" / "Future Outlook" filler closers, chat
  residue ("let's dive in").
- **Copula-opener monotony** ("It is / That is / There are" to start sentences) — keep ≤3
  per piece; start with a noun, verb, or clause instead.
- **Article-opener monotony** (The/A/An starting >~33% of sentences) — vary with names,
  dates, subordinate clauses, verbs.
- Write clean from the start: specific, sourced, plain verbs. Then sweep the OUTPUT with the
  wordlist, same as the em-dash check — don't rely on writing clean by intention alone.

## House style basics (decide once, apply everywhere — prevents drift piece-to-piece)

- Oxford comma: yes.
- Numerals: spell out one-nine, digits for 10+ (except stats/ranges/currency, always digits).
- Quotation marks: curly `“ ”` in rendered output (Word/HTML auto-curl), straight `"` only in
  code/data.
- Acronyms: expand on first use per document ("Answer Engine Optimization (AEO)"), acronym
  alone after.
- These are defaults, not client overrides — a client style guide always wins where one exists.

## Reading level (target by client vertical, not instinct)

No stated target left "readable" to feel, with clients spanning legal/B-school (denser,
formal register expected) to D2C/consumer (should scan easy). Treat Flesch-Kincaid grade level
as a FLAG to review, not a cap to force-fit — **~8-10 for D2C/consumer/social**, **~12-16 for
legal/B2B/academic thought-leadership** are the expected bands; dense legal/academic prose
naturally runs 16-18 and forcing it under a hard ceiling would flatten a bylined expert's voice
the same way chasing a detector score does (this file's Honest Limits section below warns
against exactly this — don't repeat the mistake here). If a piece lands outside its band,
read it and ask why — simplify a D2C piece that's genuinely hard to follow; leave a legal
piece that's dense because the subject is dense. A legal client reading *easier* than its own
register looks under-expert; a D2C ad reading *harder* than its register loses the scroll.

## Formality dial (translate a voice answer into concrete choices, not vibes)

When intake gives "casual" / "professional-friendly" / "formal" (see `copywriting` skill's
intake), apply it as mechanics, not a feeling:

| Register              | Contractions | Person         | Sentence length      | Example client        |
|------------------------|--------------|----------------|-----------------------|------------------------|
| Formal (legal/B-school) | none         | third person   | complete, no fragments | law firm, business school |
| Professional-friendly   | sparing      | second person  | mixed, some fragments  | SaaS, B2B services    |
| Casual (D2C/social)      | freely       | second person  | short, fragments fine  | D2C, consumer social  |

UX/product microcopy (`writing/formats.md`) is exempt from the "no fragments" cell above
regardless of client register — "Save changes" beats "Save your changes" even for a law-firm
or B-school product UI. Fragment-native is correct there, not informal.

## Proofread pass (separate from the AI-tell lint — different failure class)

The lint catches AI-sounding PATTERNS; it does not catch a plain typo, a subject-verb mismatch,
or a product/brand name spelled two different ways in the same piece. Run a real proofread pass
BEFORE the AI-tell lint, not folded into it: spellcheck, and a terminology-consistency grep
against a per-client glossary (product names, capitalization, spelling of the client's own
name). A piece can clear 0 AI-tell flags and still ship a typo — the lint was never checking
for one.

## Toolkit (free, stdlib, self-tested — keep your working copy in `tools/` alongside this skill)

- `ai_tell_lint.py <file.md|docx>` — hedging density (≤12/1000w), lexical diversity TTR
  (≥0.40), nominalization density (≤25/1000w), negation-tic count, copula-opener count,
  burstiness, banned vocab, dashes, per-sentence "hotspot" pass (mirrors how Turnitin scores
  overlapping windows rather than whole-doc averages).
- `similarity_check.py <target> <corpus...>` — cosine + 8-word verbatim-run overlap against a
  corpus you supply (own pieces + cited sources). Not a web database. Cosine of 75-86% between
  two same-genre articles is NORMAL (shared common + topic words); the only real plagiarism
  signal is a **shared 8-word verbatim run**.
- Workflow: write → lint → hand-rewrite flagged rhythm (vary, don't mangle) → re-lint until 0
  high-severity → similarity-check vs own pieces + cited sources.

## Honest limits (don't chase ghosts)

- Detectors disagree wildly on identical text (one real article: ZeroGPT 17% "human" vs
  Grammarly 66-90% AI vs Originality-Turbo near 98%). There is no true score — never present
  one tool's number as validated.
- Grammarly/Turnitin over-flag polished, dense, formal, cited, ESL-academic prose even when
  genuinely human (Stanford HAI: 61% of TOEFL essays flagged). That is exactly the
  thought-leadership profile this house writes in.
- Length raises detector confidence; a real ~1000w cited essay has roughly a 35% Grammarly
  FLOOR no rewrite clears without going short and thin. A short ~200w probe can hit 0% purely
  from low sample confidence — not a real signal.
- The only way to drop a black-box classifier score further is to degrade the writing
  (choppier, simpler) — defeats the purpose of a bylined piece. Never flatten a bylined
  expert's voice to chase a number; that reads junior (the "register trap").
- Burstiness has a natural floor in short ad/display copy — 10-word lines will always look
  more uniform than prose. Vary what can be varied (mix a 4-word fragment with a 20-word
  support line) and stop; don't force artificial variance.
- Low lexical diversity (TTR) is sometimes CORRECT — an ad set repeats product vocabulary on
  purpose, and the elegant-variation ban above says not to synonym-swap just to raise TTR.
  These two rules can point opposite directions on the same line; know why before "fixing."
  Same logic extends past ad copy to legal/patent drafting, which reuses the exact same
  defined term ("the Company," "the Agreement") on every reference on purpose — correct
  precision, not a TTR problem to fix.
- **Nominalization density (≤25/1000w) and hedging density (≤12/1000w) are review flags for
  legal/financial/compliance register, not hard caps** — same treatment as the reading-level
  rule above, for the same reason. Legal/contract prose is built FROM nominalizations that are
  the technical vocabulary itself (termination, indemnification, jurisdiction, consideration),
  and compliance writing needs hedges ("may," "subject to," "as applicable") to avoid
  overclaiming — stripping them to pass a lint number can turn an accurate qualified statement
  into an inaccurate unqualified one, a worse outcome than a lint flag. If a legal/compliance
  piece trips these, read why before rewriting; don't force it under the number.
- **If `ai_tell_lint.py` isn't reachable in this session** (it lives in one working
  toolkit directory, not every machine/session), don't stall sign-off waiting for it and
  don't claim it ran when it didn't. Fall back to the manual checklist: the
  banned-vocab list, negative-parallelism/copula-opener/article-opener sweeps, and the dash
  assert above, eyeballed or grepped directly against the wordlists in this file.
- Never use GitHub "humanizer" bypass tools (synonym-swap, zero-width-char injection) — quality
  and reputational risk on a named byline, and the effect doesn't survive Turnitin's windowed
  scoring anyway.
- The real question is not "beat the detector" but "who runs this text through which detector,
  and does it matter?" Confirm the actual gate (a specific platform's submission checker, a
  client's own tool) before optimizing blind for a hypothetical one.
