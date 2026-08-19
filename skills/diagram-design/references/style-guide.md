# Style Guide

**The single source of truth for colors, typography, and tokens.** Every diagram draws from this — not from hex values inlined in other reference files. If you want to change the visual skin of Diagram Design, change this file.

Active skin is the **Public Voyani visual system** — warm green field paper, dark ink, Voyani coral accent, grey/brown muted. Swap these values (or run [`onboarding.md`](onboarding.md)) and every new diagram inherits the new skin without touching any type-specific logic. The pristine shipped skin is recoverable at `~/.diagram-design/profiles/default.md`.

To generate your own from a website URL, see [`onboarding.md`](onboarding.md).

---

## Tokens

### Semantic roles

Every token is referred to by **semantic role**, not by its hex value. Type references (`type-*.md`) and SKILL.md say `accent`, not `#f7591f`.

| Role | Purpose | Default (light) | Default (dark) |
|---|---|---|---|
| `paper` | Page background, default node fill | `#EBF5DF` (warm green field) | `#2B2C2C` (dark ink) |
| `paper-2` | Diagram container bg, secondary fill | `#FFFDF7` (paper card) | `#3E3A37` |
| `ink` | Primary text, primary stroke | `#2B2C2C` (dark ink) | `#FFFFFF` |
| `muted` | Secondary text, default arrow stroke | `#5C5E5E` (grey.dark) | `#B0B8A7` (green.dark) |
| `soft` | Sublabels, boundary labels | `#847D76` (brown.dark) | `#847D76` |
| `rule` | Hairline borders | `rgba(43,44,44,0.12)` | `rgba(255,255,255,0.12)` |
| `rule-solid` | Stronger borders, baselines | `#B0A79D` (brown.normal) | `#5C5E5E` |
| `accent` | Focal / 1–2 max per diagram | `#EF6340` (Voyani coral) | `#EF6340` (Voyani coral) |
| `accent-tint` | Fill for accent-bordered boxes | `rgba(239,99,64,0.08)` | `rgba(239,99,64,0.12)` |
| `accent-thin` | Thin accent strokes, accent-colored text | `#B34A30` (tomato.dark) | `#EF6340` |
| `link` | HTTP/API calls, external arrows | `#4D7FAA` (signal blue) | `#7FA9CC` |

> **Brand palette source:** Public Voyani visual system, extracted from the governed brand pack (`~/.claude/skills/voyani/reference/approved-pack.json`, canonical `Mojo-Solo/standard-brand` → `brand.voyani.yaml`). Palette families: `tomato #EF6340`, `brown #B0A79D`, `grey #7A7D7D`, `yellow #F7F391`, `blue #DFF5F3`, `green #EBF5DF`. `muted`, `soft`, `rule-solid` and `accent-thin` are drawn from those families' `dark`/`normal` steps rather than invented, so every token here is a Voyani color. `link` uses Voyani's semantic signal blue.

> **Contrast notes (light):** `ink` 12.44:1, `muted` 5.80:1, `accent-thin` 4.74:1 — all AA. `accent #EF6340` is 2.86:1 on `paper`, marginally under the 3.0:1 graphic threshold; it is kept because Voyani coral is load-bearing brand heat. Use `accent-thin #B34A30` for hairline accent strokes and accent-colored text; reserve `accent` for fills and large marks. Dark mode: `ink` 14.01:1, `muted` 6.84:1, `accent` 4.35:1 — all pass.

> **Note:** The pre-baked example HTML files in `assets/` were built under an earlier skin. Regenerating them against the current `style-guide.md` is a v5.1 task. New diagrams the skill produces will use the tokens above.

### Inversion rule (light → dark)

Voyani ships a **real dark palette**, so the dark column above is Voyani's own dark set — not a mechanical inversion. Do not derive dark values by flipping light ones. For any token not listed, `rgba(43,44,44, X)` in light becomes `rgba(255,255,255, X)` in dark at the same opacity. The accent does **not** hue-shift: `#EF6340` is the accent in both modes and already clears AA on dark paper (4.35:1).

### Series palette (multi-series chart types only)

A small set of desaturated, editorial-tone colors for chart types that genuinely need to distinguish multiple overlapping entities (currently: **radar**). The "1-focal" rule still holds — `accent` is reserved for the focal series; the palette below covers the rest.

| Token | Light | Dark | Notes |
|---|---|---|---|
| `series-1` | `#7c8f6f` (sage) | `#9caf8f` | Non-focal series |
| `series-2` | `#5e7a9b` (dusty-blue) | `#82a0c0` | Non-focal series |
| `series-3` | `#b8915a` (mustard) | `#d3ad7a` | Non-focal series |
| `series-4` | `#9c6b50` (rust-brown) | `#b88670` | Non-focal series |
| `series-5` | `#6e6479` (slate) | `#8d8298` | Non-focal series |

Fills sit at `0.18` opacity light, `0.22` dark; strokes use the full color. **Don't backfill these tokens to non-chart types** — architecture, swimlane, etc. continue to use muted-ink variants. The series palette is opt-in for diagrams where overlapping shapes demand distinguishable color, not a license to add color elsewhere.

### Terminal skin (opt-in alternate)

A self-contained palette for the terminal-window primitive (see [primitive-terminal.md](primitive-terminal.md)) — a CLI-chrome register for dev-tool posts and technical social cards. It does not replace the default skin above and isn't affected by onboarding; it's a second, fixed skin you opt into per-diagram.

| Token | Hex | Purpose |
|---|---|---|
| `terminal-page` | `#0a0a0a` | Page background behind the window |
| `terminal-paper` | `#141414` | Window body, node fill |
| `terminal-bar` | `#1b1b1b` | Titlebar strip |
| `terminal-border` | `#2b2b2b` | Window border, hairlines |
| `terminal-ink` | `#f5f5f5` | Primary text, primary stroke (same white-smoke as default `ink`) |
| `terminal-muted` | `#9a9a9a` | Secondary text, sublabels, ring stroke |
| `terminal-soft` | `#5c5c5c` | Tertiary — inactive dots, spokes |
| `terminal-accent` | `#ff5a36` | The one accent — focal station, prompt sign, active dot |
| `terminal-accent-tint` | `rgba(255,90,54,0.12)` | Fill for accent-bordered boxes |

**1-accent rule still holds.** Everything that isn't `terminal-ink` or `terminal-muted`/`terminal-soft` should be `terminal-accent` — never introduce a second hue.

---

## Typography

| Role | Family | Size | Weight | Usage |
|---|---|---|---|---|
| `title` | Libre Baskerville | 1.75rem | 400 | Page H1 |
| `node-name` | Instrument Sans | 12px | 500 | Human-readable labels |
| `sublabel` | Geist Mono | 9px | 400 | Port, protocol, URL, field type |
| `eyebrow` | Geist Mono | 7–8px | 500, tracked 0.18em, uppercase | Type tags, axis labels |
| `arrow-label` | Geist Mono | 8px | 400, tracked 0.06em | Arrow annotations |
| `callout` | Libre Baskerville *italic* | 14px | 400 | Editorial asides only |

### Font stack

```html
<link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Instrument+Sans:wght@400;500&family=Geist+Mono:wght@400;500&display=swap" rel="stylesheet">
```

**Voyani weight cap:** never exceed weight 500 on quiet surfaces. `node-name` is 500, not 600. Libre Baskerville 700 is available but reserved for a page H1 that genuinely needs it.

**Load-bearing rule:** Mono is for *technical* content (ports, commands, URLs, field types). Names go in Instrument Sans. Page title is Libre Baskerville. Italic Libre Baskerville is reserved for annotation callouts (see [primitive-annotation.md](primitive-annotation.md)). **Never JetBrains Mono** as a blanket "dev" font.

---

## Stroke, radius, spacing

| Token | Value | Use |
|---|---|---|
| `stroke-thin` | `0.8` | Tag-box outlines, leaf nodes |
| `stroke-default` | `1` | Most strokes |
| `stroke-strong` | `1.2` | Emphasis strokes |
| `radius-sm` | `4` | Small tags |
| `radius-md` | `6` | Node boxes |
| `radius-lg` | `8` | Containers, rings |
| `grid` | `4` | Every coord, size, and gap is divisible by 4 (hard rule) |

---

## Node type → treatment

Semantic role combinations — reference these by name in type specs.

| Type | Fill | Stroke |
|---|---|---|
| `focal` (1–2 max) | `accent-tint` | `accent` |
| `backend` | `#ffffff` (white) | `ink` |
| `store` | `ink @ 0.05` | `muted` |
| `external` | `ink @ 0.03` | `ink @ 0.30` |
| `input` | `muted @ 0.10` | `soft` |
| `optional` | `ink @ 0.02` | `ink @ 0.20` dashed `4,3` |
| `security` | `accent @ 0.05` | `accent @ 0.50` dashed `4,4` |

---

## Customizing the skin

Four options:

1. **Run onboarding** — see [`onboarding.md`](onboarding.md). Drop a URL; the skill extracts the palette + fonts and rewrites this file.
2. **Edit by hand** — change the hex values in the tables above. Run the pre-output taste gate afterward to verify the accent still reads as "focal" against the new paper color.
3. **Brand handoff** — paste your existing design-token JSON into a new section here and map its tokens to the semantic roles above.
4. **Client profiles** — save and switch named skins, or bind one to a project, using [`profiles.md`](profiles.md).

### Constraints (don't break these)

- **Contrast**: `ink` must hit WCAG AA on `paper`. `muted` must hit AA on `paper` for 11px+ text.
- **One accent**: pick one color for `accent`. Two accents erases the focal signal.
- **No rainbow palette**: if your brand ships 8 colors, pick 3 (paper, ink, accent). The rest become `muted` variants.
- **Serif + sans + mono**: three families, not more. Voyani supplies all three (Libre Baskerville / Instrument Sans / Geist Mono), so no substitution is needed — the serif/sans contrast is load-bearing and already brand-true.
- **Paper is warm-neutral, not pure white**: pure white turns the design sterile. Pick a cream, bone, or light grey with a hint of warmth.
- **Dot pattern is optional, not default**: the 22×22 dot pattern is an opt-in "dotted paper" variant (good for long-form editorial hero diagrams). The default background is a clean `paper` fill, no pattern. When the pattern is enabled, it should sit at ~10% opacity of `ink` on `paper` — visible but quiet.
- **Container is clean by default**: the diagram sits directly on the page paper, no secondary container background or border. A framed variant (`paper-2` bg + `rule` border + 8px radius + padding) is available as an opt-in for card-heavy layouts, but don't reach for it by default — the extra chrome fights the figure.
