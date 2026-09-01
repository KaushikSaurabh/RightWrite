# Design — foundations + critique discipline

**ALWAYS-FIRE on any visual work** (creatives, decks, brochures, landing pages, graphics):
design by REASONING from first principles, then VERIFY. Do not pattern-match a reference
until it "looks right." Keep a deeper canonical design-standards doc if useful; this file
is the self-contained working summary.

## Load-bearing principles (Williams / Gestalt / Müller-Brockmann / Lupton / Butterick / Albers / WCAG)

- **CRAP** — Contrast (commit, don't nudge), Repetition, Alignment (NOTHING floats — every
  element shares an axis with another), Proximity (space groups; the gap IS the signal).
- **Figure-ground** — the focal element must advance off the background or it's ignored.
- **Hierarchy** = size + weight + VALUE + position + contrast + spacing. MAX 3 levels.
  Differences must be substantial (≥1.5×). **Greyscale test:** if the hierarchy dies in
  greyscale, it was hue, not hierarchy.
- **Real grid**, not eyeballed pixels — order = credibility. Margins set the register.
- **Type** — body-first; measure 45–90 chars; leading 120–145%; max 1–2 faces with real
  contrast; ALL-CAPS only when short + tracked; no faux bold; modular scale.
- **Colour** — VALUE contrast beats hue; VERIFY WCAG ratio (4.5:1 body, 3:1 large text) —
  measure, don't assume, don't round up; 60-30-10; one accent by scarcity; near-black /
  near-white, not pure black/white.
- **White space is ACTIVE** (it's the ground). Crowding destroys hierarchy. Resist the urge
  to "fill the space."

## Sober house style (client-facing)

One typeface with clear hierarchy, ONE restrained accent + a muted grey, generous
whitespace, thin rules not heavy fills. No rainbow, no font-variety, no over-decoration —
that combination reads machine-generated and cheapens the work.
- docx verify: `set(re.findall(r'w:ascii="([^"]+)"', document_xml))` → one font;
  distinct `w:color` values ≤ 2–3.
- Brand accent per client (check the project) — e.g. one client's system might be a specific
  purple, never the agency's own default; match the brand, don't default.

## Critique discipline (the real ask, run on EVERY creative)

Audit and name each violation, then fix by principle:
- One clear focal point?
- No floaters (every element shares an axis)?
- ≤ 3 hierarchy levels?
- Survives the greyscale test?
- Contrast VERIFIED by measurement (not vibes)?
- One accent / 60-30-10 respected?
- Whitespace working as active ground, not leftover?

**Verify the critique itself with measurement.** Once I *assumed* a chart background hurt
legibility; measured 11.5:1 (passes) — the real faults were a floating "01" number (no
shared axis), no true grid (absolute-pixel positioning), and hierarchy leaning on size
alone. Principle + measurement, never one or the other.

## Rendering / export (headless Chrome — MCP-free, exact pixels)

- **Exact-pixel PNG export:** `chrome --headless=new --force-device-scale-factor=1
  --window-size=W,H --screenshot` + `:target` hash isolation per artboard. (chrome-devtools
  MCP `resize_page` ignores px and DPR-scales — don't use it for pixel-critical work.)
- **A4 multi-page PDF:** `--print-to-pdf` FORCES US Letter (612×792) and splits your pages.
  Use CDP `Page.printToPDF { paperWidth:8.27, paperHeight:11.69 }` via Node instead
  (unique `--user-data-dir`, poll `/json/version`, `setEmulatedMedia:print`).
- Google Fonts may not load in headless — self-host if pixel-critical.
- QA screenshots via Playwright Chromium (Brave headless has been broken here).
