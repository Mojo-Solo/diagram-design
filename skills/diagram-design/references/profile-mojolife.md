<!-- diagram-design-profile
name: MojoLife CoThinker Hub (Ian Nov 6)
slug: mojolife
source-url: https://mojosolo.com
created: 2026-11-06
updated: 2026-11-06
notes: Warm paper (#faf7f2), navy ink (#16273b), Mojo blue (#006da4 / #00a9e0), REC red (#c7261c), on-track green (#2e7d4f)
-->
# Style Guide

**The single source of truth for MojoLife CoThinker Hub diagrams.** Matches Ian's Nov 6 MojoLife tokens (`--paper: #faf7f2`, `--card: #ffffff`, `--surface: #f1ece4`, `--ink: #16273b`, `--soft: #5c6672`, `--rule: #e2dcd2`, `--act: #006da4`, `--live: #00a9e0`, `--rec: #c7261c`, `--ok: #2e7d4f`).

---

## Tokens

### Semantic roles

| Role | Purpose | Default (light) | Default (dark) |
|---|---|---|---|
| `paper` | Page background, default node fill | `#faf7f2` | `#0f1922` |
| `paper-2` | Diagram container bg, secondary surface | `#f1ece4` | `#172532` |
| `ink` | Primary text, primary stroke | `#16273b` | `#f3eee4` |
| `muted` | Secondary text, default arrow stroke | `#5c6672` | `#b6b0a4` |
| `soft` | Sublabels, boundary labels | `#8d97a2` | `#6f7d8a` |
| `rule` | Hairline borders | `#e2dcd2` `rgba(22,39,59,0.12)` | `#263440` `rgba(243,238,228,0.12)` |
| `rule-solid` | Stronger borders, baselines, manila | `#d9ccb6` `#e7dcca` `#f3ebde` | `#1d2d3b` |
| `accent` | Focal / Mojo action blue | `#006da4` | `#00a9e0` |
| `accent-tint` | Fill for accent-bordered boxes | `#e3eef5` `rgba(0,109,164,0.08)` `rgba(46,125,79,0.18)` `rgba(46,125,79,0.45)` | `rgba(0,169,224,0.14)` |
| `link` | Live Jev / API calls / status / avatar | `#00a9e0` `#2fa9de` `#ffc21a` `#2e7d4f` `#9be6b8` `#c7261c` `#f8e4e1` `#b7791f` | `#5fcbec` `#ff3b30` `#141413` |

## Typography

| Role | Family | Size | Weight | Usage |
|---|---|---|---|---|
| `title` | Instrument Serif | 1.75rem | 400 | Page H1 |
| `node-name` | Plus Jakarta Sans | 12px | 600 | Human-readable labels |
| `sublabel` | Geist Mono | 9px | 400 | Port, protocol, URL, field type |
| `eyebrow` | Geist Mono | 8px | 500 | Type tags, axis labels |
| `arrow-label` | Geist Mono | 8px | 400 | Arrow annotations |
| `callout` | Instrument Serif | 14px | 400 | Editorial asides |
