# Sourcing & verification — every claim, every project

**No made-up stats, no made-up facts, no guessed URLs.** Naming a plausible-sounding source is
NOT verification — the source has to actually exist, actually say the thing, and the URL has
to actually resolve. This is a hard rule Johnny has restated more than once; treat every number
as unshippable until it clears the checks below.

## Tier the sources to the client

The real line is PRIMARY vs AGGREGATOR-SUMMARIZED, not "government vs not." Reading the old
rule as "must be a .gov domain" would reject sources that ARE primary and aren't government —
a peer-reviewed journal, a company's own audited filing, a rating agency's own rating. Use the
vertical-specific definition of primary instead:

- **Legal** — the instrument itself: statute text (gazette/indiacode), the court's own
  judgment (NJDG/eCourts, or an official law-report series if the court doesn't self-host), the
  regulator's own circular/notification. A case-law aggregator (Indian Kanoon, SCC Online,
  Manupatra) is fine for FINDING a citation, not for quoting AS the primary text — pull the
  actual judgment/statute language it points to.
- **Medical** — a peer-reviewed, indexed journal article (PubMed etc.), a regulatory body
  (FDA/CDSCO/WHO), or a registered clinical-trial record. Primary and authoritative without
  being government-hosted — don't reject a journal citation for failing a literal government
  test.
- **Financial** — a regulatory filing (SEBI/SEC/RBI), the company's own audited annual
  report/financial statement, exchange data (NSE/BSE), or a rating agency's own published
  rating (CRISIL/ICRA/Moody's/S&P). All primary, none of them the government.
- **Education / admissions / B-school** — the institution's own accreditation body (AACSB/
  NAAC/NIRF/UGC), the official ranking body, or the university's own registrar/admissions
  page — never a paywalled aggregator or a competitor's marketing page taken at face value.
  This tier exists because a false/unverifiable claim (an unverified university-affiliation
  claim, a numeric threshold claim not actually present on the live page) shipped once already.
- **What's actually banned across all four, and the enforceable line** — paywalled
  market-research/review aggregators that summarize someone else's primary data without being
  a primary source themselves: no Grand View, Mordor, Statista, IBEF, G2, Capterra as primary
  for these clients. This is the failure mode the rule exists to stop (a wrong GST SAC code, a
  misattributed HBR stat, a DPDP enforceability date off by a year, dead indiacode `/handle`
  URLs cited as primary) — not "anything without a .gov domain."
- **Gartner (and equivalent named-analyst research) is NOT in that banned list** — a Gartner
  Magic Quadrant placement is the analyst's own named, dated assessment, structurally the same
  as a rating agency's own rating (allowed under Financial above), not an aggregation of
  someone else's numbers. Cite it attributed and dated like any primary source. The test is
  "whose own assessment is this," not "does the brand sound like a data vendor."
- **Commercial / marketing clients** — real named industry reports are fine (FICCI-EY, Redseer,
  NASSCOM, Kantar, GroupM, Bain) with publisher + year; these clients tolerate aggregator-tier
  sourcing the four verticals above don't.
- If a figure cannot be tied to a real, checkable publisher, **cut it** or make the point
  qualitatively. Silence beats a shaky citation.

## Research and lock BEFORE writing

1. Research the open internet for the BEST available primary source — never settle for what's
   already to hand. Go find the statute PDF, the gazette notification, the regulator's own
   page, and **fetch each one live** before citing it. A URL that 403s, redirects to a
   homepage, or doesn't actually contain the claim is rejected. Record a verbatim quote plus
   the access date, never a paraphrase.
2. Lock a source table BEFORE writing, not after: one file listing each approved claim, its
   exact primary URL (checked live), the exact subsection, mandatory framing, and an explicit
   DEAD/DO-NOT-USE list. Writers cite from that table and nothing else.
3. **Verify by machine, not by trust** — especially across subagent fan-out, where every writer
   will assure you it complied. Run a deterministic checker over the drafts that re-tests every
   URL against the approved set, flags dead/aggregator/competitor domains, enforces mandatory
   framings, and prints every numeric claim for eyeball review.

## Every statistic = number + named source + year, visible

For B-school / academic / any credibility-sensitive brand, show the source in TWO visible
places: a short credit line ON the creative (small, bottom of image) AND a `Source:` line IN
the caption/body — never a designer-only note the audience never sees. Definitional/opinion
posts assert no statistic — label them as such, no false-precision source credit.

**Hard-verify every superlative.** "Largest", "first", "only" have shipped false at least
twice (a "largest in its category" claim that a competitor had already overtaken; a
threshold-number claim that was never actually on the live page). A superlative is a claim
like any other — check it live.

## The source register (ship alongside every research-backed deliverable)

Inline citations are not enough. Ship a separate, durable register with, per claim:
- the exact claim as used in the deliverable
- the verbatim quote from the source (not a paraphrase)
- the URL + date accessed
- confidence tier: Verified (read at primary/official source) / Secondary (reputable third
  party) / Not published
- where the claim is used, so a challenged claim is traceable both ways

Also persist the RAW capture (scraped HTML/text, API JSON, screenshots) into a dated folder,
e.g. `research/<source>-YYYY-MM-DD/`. Pages 404 fast — three sources rotted the same day on one
real sweep. Build the register in the SAME pass as the research, never afterward. XLSX when
it's a table of claims. Mark unverified figures as unverified in the register AND in the
deliverable rather than quietly dropping them; re-verify before any relaunch or reuse.

## Competitive claims — a special case

- **Never cite yourself** as the source for a competitive comparison ("Source: our own
  analysis at ourdomain.com") — circular, defeats the point of a source. Cite the primary by
  name: institution, exact programme/product title, date read.
- **Verbatim beats paraphrase.** Their own sentence is unarguable; your summary of it isn't.
  Reproducing a competitor's own labels/text in full is stronger than describing them.
- **Trap:** a summarizing fetch returns quotes that are not necessarily verbatim page text.
  Before putting a competitor's words on a creative, re-fetch with a prompt that demands
  verbatim strings only and marks anything unfound as NOT FOUND — several "quotes" have failed
  this check on a fresh re-pull.
- State the fee/number as printed alongside any competitive claim — a claim about a priced
  programme is weak without the price in it.
- Two claim types need different handling: a *page/ad claim* must carry the verbatim string;
  an *absence claim* ("they publish no fee") or *your own measurement* ("48% of 178 ads
  checked") can't be quoted from anyone's page — label it plainly as your own count/check.
  Build this as a runnable audit over the copy data, not an eyeball pass.
- The trade, stated once: naming a competitor is the strongest legal position (verbatim,
  dated, true; truthful comparative advertising is generally permitted) and the highest
  commercial risk (platform complaints, their brand inside your ad). Get written client
  sign-off before naming an institution.

## Product-capability claims — verify boundaries, not just statistics

Before writing anything that describes what a client's OWN product/service does (features,
automation, integrations), check the claim against a client-supplied capability/truth table the
same way a statistic gets checked against a source — a plausible-sounding capability claim is
not verification any more than a plausible-sounding statistic is. This has shipped wrong before:
a product got described as auto-computing a tax field and auto-exporting to an ERP it actually
has no integration with, both manual steps framed as automatic. If no truth table exists for a
new client, ask for one (what it does, and explicitly what it does NOT do / still requires
manual steps for) before writing capability claims, same discipline as locking a source table
before writing per the section above. Applies to LP feature lists, product pages, technical/
developer-audience articles, and sales-facing case studies alike.

## Customer quotes / testimonials — same verbatim discipline as competitive claims

A testimonial is a claim about the client, from a named person, same as a competitive claim is
a claim about a competitor: quote their actual words, don't summarize them into marketing
copy — the summary is arguable, their own sentence isn't. Get explicit permission to publish
before use, and never invent or composite a quote from "typical" feedback. If a metric is in
the quote ("cut our reporting time in half"), verify it's the client's own number, not one you
supplied to them.

## Compliance is separate from sourcing

A claim being true and sourced does not make it usable — check the client's own BLOCKED-claims
list even when the live source states it. "It's on their site" and "cleared for paid spend"
are not the same bar. Client-approved keyword/prompt lists win over what a tool surfaces:
conform to the approved list first, then use Semrush/GSC/etc. to validate and prioritize
within it, not to choose outside it.
