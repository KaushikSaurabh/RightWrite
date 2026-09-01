# Development — front-end build + run/verify traps

Lazy-first (ponytail): stdlib → native platform feature (CSS over JS, `<input type=date>`
over a picker lib, DB constraint over app code) → already-installed dep → one line → minimum
code. No speculative abstractions. Shortest working diff wins. Leave one runnable check
behind non-trivial logic.

## Modularity

When a shape repeats (a Paper/panel, a card, a builder, a CSS block), EXTRACT a shared
component — don't inline-restyle copies that drift. One source of truth. For batch content
builders: one builder module (styles, asserts, schema, QA) + one spec file per batch.

## Running & verifying the app (Windows / Next — hard-won, cost a full session)

A correct fix looked "not applied" for ~15 turns because the dev server served a STALE
bundle and "fixed" was declared from numbers, not the actual look. Avoid:

1. **Kill by PORT owner, not by name.** `Get-NetTCPConnection -LocalPort 3000` →
   `Stop-Process -Force`. Matching `next dev` misses the real `next-server` child; the
   zombie survives, holds the port, new `npm run dev` dies silently with EADDRINUSE while
   the zombie keeps serving stale.
2. **Confirm the NEW server is up:** log says `Ready in Xs` AND `/login` returns **200**.
   "A process launched" proves nothing.
3. **Verify VISUAL INTENT, not DOM numbers.** A modal can have `maxHeight` + button
   `inViewport:true` and still read broken (it centres+scrolls instead of fitting).
   Screenshot at the user's real/short viewport and LOOK. When the user says "still broken,"
   believe them over your metrics.
4. **Don't loop on screenshots.** If 2 verify cycles don't converge, ask for a hard-refresh
   (Ctrl+Shift+R — stale-cache tab is the #1 culprit) and an exact-defect description.
5. **Low-RAM OOM (this box ~7.4 GB):** `next dev`/`build` dies SILENTLY at low free RAM —
   pages capture blank white, no error trace. Check
   `(Get-CimInstance Win32_OperatingSystem).FreePhysicalMemory` FIRST; free RAM (close
   Brave, reap zombie next-servers); dev needs `--max-old-space-size=2048` (1024 is under
   Next-16's floor). If it still can't hold dev+Chromium, run the Playwright sweep in small
   BATCHES, fresh server per batch. Content-gate each shot on the route's own heading text
   (`getByText(...).waitFor`), NOT a fixed timeout.
6. **Watchpack crash on `C:\` system files (Node 24):** `next.config.ts` →
   `config.watchOptions.ignored = ['**/node_modules/**','**/.next/**','**/.git/**',
   'C:/*.sys','C:/*.tmp','C:/DumpStack.log.tmp']`.
7. **Git-Bash mangles curl URLs** (`/login` → `C:/Program Files/Git/login`). Prefix
   `export MSYS_NO_PATHCONV=1`, or verify via PowerShell `Invoke-WebRequest`.
8. **Launch dev so it SURVIVES the turn:** `Start-Process cmd /c "... npx next dev ..."
   -WindowStyle Hidden -PassThru`. A Bash `&` subshell or `run_in_background` gets reaped
   mid-compile.
9. Preview/e2e on socket-holding pages use `domcontentloaded`, NOT `networkidle` (never
   idles → timeout). Reap leftover preview browser node procs.

## WordPress body-HTML embed (wpautop trap)

Pasting self-contained HTML into a WP post: wpautop `<p>`-wraps loose nodes (scripts,
comments) and breaks it. Wrap EVERYTHING in one `<div>`, use a Custom HTML block, drop
title/canonical/breadcrumb (the theme owns `<head>`), namespace your classes vs theme
collisions, break out full-width via `100vw`. TEST LIVE, not in a harness (harness skips
wpautop). Watch for theme-polluted schema nodes (staging phone/name) — flag pre-crawl.

## Definition of done (dev)

Plan → strategize → execute → test/verify with FRESH evidence before claiming done.
Run a judge pass on any "fixed/deployed/works" claim — mine, a tool's, or another agent's.
