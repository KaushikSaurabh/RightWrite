# web-practice

A Claude Code skill for the whole web-agency lifecycle: **design → develop → write → rank → ship**.

Nine reference files covering hard-won, battle-tested standards for front-end build/verify
traps, visual design critique, AEO/GEO/SEO article structure, writing craft and AI-tell
detection, source verification, and client-deliverable packaging — the kind of standards
that usually stay locked in one agency's private notes. Distilled from real client work,
with the client-identifying specifics scrubbed out; the rules and the reasoning behind them
are what's kept.

## What's in here

| File | Covers |
|---|---|
| `SKILL.md` | The always-fire non-negotiables + routing table to the rest |
| `design.md` | Visual design principles (CRAP, hierarchy, WCAG contrast) + critique discipline |
| `development.md` | Front-end build/run/verify traps (Windows/Next-specific gotchas included) |
| `writing.md` | Writing non-negotiables + routing to the content-type playbooks |
| `writing/craft.md` | The 7 convergent craft rules, dash enforcement, AI-tell sweep, detector honest-limits |
| `writing/sourcing.md` | Source tiering by client vertical, citation discipline, competitive-claim handling |
| `writing/formats.md` | Per-content-type playbooks: articles, LPs, email, brochures, scripts, ad copy, RFPs, and more |
| `seo.md` | AEO/GEO/SEO ranking + schema + meta mechanics |
| `workflow.md` | Verify-before-done discipline, deliverable format rules, safety/reversibility |

## Install

Copy this repo's contents into `~/.claude/skills/web-practice/` (or clone straight into
that path). Claude Code picks up the skill automatically once `SKILL.md`'s frontmatter is
in place.

```
git clone https://github.com/KaushikSaurabh/RightWrite.git ~/.claude/skills/web-practice
```

## Toolkit scripts

`writing/craft.md` references two small stdlib Python scripts meant to live in a `tools/`
directory alongside this skill:

- `tools/ai_tell_lint.py` — bundled. Stdlib-only (falls back to `xml.etree` if
  `defusedxml` isn't installed), works standalone against a `.md` or `.docx` file, no
  network. Ported from a real project's vendored copy after a real crash fix (a
  zero-sentence input, e.g. a one-word reply, threw `StatisticsError` on
  `statistics.mean([])` - now falls back to `0` for that field instead).
- `tools/similarity_check.py` — not yet built. The rules are written so the skill still
  works without it (see craft.md's "if ai_tell_lint.py isn't reachable" fallback), but a
  real similarity pass needs the actual script. Open an issue or a PR if you build one.

## Why this exists

Most of what's here came from real mistakes that shipped once and got turned into a rule:
a hard-coded reading-level ceiling that would have flattened legitimately dense legal
prose, a sourcing rule that read as "government-only" when it meant "primary," an AI-tell
threshold that doesn't distinguish marketing copy from legal drafting. The rules are kept
specific enough to be checkable (regex asserts, character counts, review flags with real
thresholds) rather than vague "write good copy" advice — and each one carries the failure
it exists to prevent, so it's harder to misapply.

## License

MIT — see `LICENSE`.
