# Workflow — plan, verify, package, ship

## The loop (all non-trivial dev/content work)

**Classify → define done → gather evidence → decide → act surgically → verify by
observation → report outcome-first.** Plan robustly, strategize, execute the shortest
working change, then TEST/verify with FRESH evidence before claiming done. Pragmatic
ceremony — skip it on one-file / <10-line / clean-attended tasks and just report in two
sentences.

## Verify before "done" (non-negotiable on prod / migrations / client sign-off)

Re-run the ACTUAL check; believe nothing not observed. Applies to my claims, a tool's
output, and another agent's "done." "It should work", DOM numbers, and "a process launched"
are not verification. For prod: prod can drift from migration files — check the live state,
not the intended state. Run a judge pass on any "fixed / deployed / works complete" claim
before presenting it.

## Deliverable format (pick format to content)

- Client-facing = **always `.docx`** (python-docx): content plans, roadmaps, dev fix-lists,
  reports, articles.
- Table-heavy → **`.xlsx`** (openpyxl via uv).
- Decks → **`.pptx`**.
- Narrative articles → `.docx`; JSON-LD schema appended in the SAME doc (no standalone
  `.md`/`.json`).
- **Markdown only for internal** notes/guides/backlog/memory.
- Prefer Office formats over markdown for anything a human other than me opens.

## Rolling / recurring reports

A recurring report is ONE incrementing workbook — append a column/period via a `MONTHS`
list + a KPI-trend sheet — NOT a new file each month. The numeric spine comes from ONE live
date-clean source (e.g. fresh GSC pull), never mixed-date cached exports (mixed dates get
caught in review, every time). Keep one central, reusable generator module for this report
type, invoked the same way every period. Report generators are author-fresh per client
(reuse helpers, not a config-driven monolith).

## Client-facing packaging (two hard rules)

1. **Never reveal production methods/tools.** No "built in X", no aspect ratios, no library
   names, no workflow exposition. Show the idea, hook, copy, and why it lands. Scrub any
   sentence explaining *how a thing is made* rather than *what it is / why it works* before
   send. This keeps the agency indispensable.
2. **Sober design** (see `design.md`): one font, one accent + grey, whitespace, thin rules.

## Safety / reversibility

- **Version before any substantial rewrite:** `/versions/<file>.YYYY-MM-DD-HHMM.bak`.
- **Keep disposable artifacts local** (previews, compares → `python -m http.server`); never
  deploy to Vercel/FTP unless explicitly asked.
- Confirm outward/irreversible actions (deploy, send, delete, publish) before doing them,
  unless durably authorized. Approval in one context doesn't carry to the next.
- Deploy to the client's real target (know FTP vs Vercel vs WP per project — check the
  project's own record of it; one client might deploy via FTP to a specific subpath,
  another via a platform like Vercel — look it up per project, never assume).

## Be proactive (standing expectation)

Spot the whole problem-CLASS and propose the better approach BEFORE Johnny finds each
defect. Codemod mechanical fixes across all instances at once; suggest the lint/assert that
prevents the class from recurring. Don't react item-by-item.

## GateGuard (this machine)

A fact-forcing hook gates first-Bash / destructive-Bash / first-Edit-Write. It doesn't
block — it demands facts FIRST, in the SAME message, before the call, so it passes on the
first try (every denial is a wasted re-run). First Edit/Write: state (1) who imports it,
(2) public fns/classes affected, (3) data files + fields, (4) the instruction verbatim.
Destructive Bash: add exact files touched + one-line rollback + instruction verbatim.
Don't disable it — oblige it.
