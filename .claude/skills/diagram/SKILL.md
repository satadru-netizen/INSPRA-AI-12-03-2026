---
name: diagram
description: Generate branded architecture diagrams, blueprints, data flows, process flows, swim lane diagrams, and system integration maps as PDF. Triggered by phrases like "draw a blueprint", "map the systems", "visualise the architecture", "diagram the integration".
---

# Skill: diagram

## Trigger
Invoke this skill when the user asks for any of:
- Diagram / blueprint / data flow / architecture diagram / system integration
- Lead flow / process flow / pipeline map / swim lane diagram
- Phrases like: "draw the flow", "map the systems", "visualise the architecture", "diagram the integration", "blueprint", "draw a blueprint"

**Do NOT** use this skill for Figma or web-based diagrams. This skill generates Python (matplotlib) diagrams saved as PDF.

---

## Overview
Four phases:
1. **Gather** — extract all needed information via conversation
2. **Generate** — write a Python script that produces the diagram (with pre-generation validation)
3. **Render → Inspect → Fix → Re-render** — mandatory visual validation loop (1-3 iterations typical). You MUST Read the temp PNG after every render and check the Visual Defect Checklist before delivering.
4. **Write-up** — generate a branded companion PDF document that explains the diagram. Both the diagram PDF and write-up PDF are standard deliverables.

---

## Phase 1 — Gather

**Input method — Fathom transcript:**
If the user pastes a Fathom (or any call recording) transcript, extract all required fields below directly from the transcript without asking. Infer:
- Client name from meeting title or introductions
- Brand (AA or Inspra) from context of who is hosting the call
- Current systems from any tools, software, or platforms mentioned
- Proposed integrations from any solutions discussed or recommended
- Phases from any "Phase 1 / Phase 2" or "short-term / long-term" language
- Open questions from any unresolved items, "we need to check", "TBD", or action items in the transcript

Only ask the user for fields that genuinely cannot be inferred. Confirm your extraction in a brief summary before proceeding to Phase 2.

Ask the user (or extract from conversation) the following. Ask only what is missing — do not re-ask confirmed details.

| Field | Default / Example |
|-------|-------------------|
| Client name | Required |
| Brand | **Inspra AI** (default) or **Automate Accelerator** |
| Diagram title | "Blueprint — [Client] × [Brand]" |
| Subtitle / version | "[Brand]  \|  [date]  \|  v1" |
| Save folder | `~/Desktop/[ClientName]/` |
| Filename prefix | `[BrandPrefix]_[Client]_Blueprint_v1_YYYYMMDD` — Inspra prefix = `Inspra`, AA prefix = `AA` |
| Phases / rows | e.g. "Current State", "Proposed Phase 1", "Phase 2 (Future)" |
| Systems per row | Described in plain English |
| Colour category per system | Auto-detect or user-specified (see palette below) |
| Connections / arrows | Described in plain English |
| Open questions | Numbered list (may be empty) |
| Footer text | "[Client] × [Brand] — Confidential" |

### Colour category auto-detection rules
- **Existing System** — pre-existing client systems, CRMs, dialers, legacy tools
- **New / Hub** — newly introduced central platform (e.g. JustCall, HubSpot replacing old system)
- **Brand AI System** — any Inspra AI or Automate Accelerator platform / agent component (uses brand colour)
- **Future / TBC** — Phase 2 items, speculative, scope TBD
- **Neutral** — endpoints, websites, agents, customers, output destinations

---

## Phase 2 — Generate Python Script

Write the script to `/tmp/blueprint_{client_snake}_{YYYYMMDD}.py` then execute it.

### Python Script Template

Use this exact structure. Replace ALL `{placeholders}` with real values from Phase 1.

```python
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from PIL import Image
import numpy as np
import os

# ── Brand config ──────────────────────────────────────────────────────────────
# Set BRAND to "inspra" or "aa" — everything else derives from this.
BRAND = "{BRAND}"   # replace with: "inspra"  OR  "aa"

if BRAND == "aa":
    BRAND_NAME      = "Automate Accelerator"
    BRAND_COLOR     = "#F47920"          # AA orange (official: R244 G121 B32)
    BRAND_DARK      = "#412F8F"          # AA purple (official: R65 G47 B143)
    BRAND_LOGO_PATH = os.path.expanduser(
        "~/.claude/skills/brand-doc/assets/AA-logo-dark.png"
    )
    BRAND_LOGO_BG   = None               # no dark patch — logo has dark text on transparent
    BOX_BRAND       = ("#FFF0E6", "#F47920")   # Brand system box — warm orange
    ROW_B_BG        = ("#FFF3E6", "#F47920")   # Proposed row background — orange-tinted
else:  # "inspra" (default)
    BRAND_NAME      = "Inspra AI"
    BRAND_COLOR     = "#39E100"          # Inspra green
    BRAND_DARK      = "#1A3A00"
    BRAND_LOGO_PATH = os.path.expanduser(
        "~/.claude/skills/brand-doc/assets/Inspra-logo-dark.png"
    )
    BRAND_LOGO_BG   = None               # no dark bg needed — logo is dark on white
    BOX_BRAND       = ("#E8FAE0", "#39E100")   # Brand system box — green
    ROW_B_BG        = ("#EDFCE5", "#39E100")   # Proposed row background — green-tinted

# ── Colours ────────────────────────────────────────────────────────────────────
WHITE        = "#FFFFFF"
BADGE_ORANGE = "#FF6B00"

# Box fill / edge colour pairs  (fill, edge)
BOX_EXIST    = ("#E8F0FE", "#4A6FA5")   # Existing System — blue-grey
BOX_HUB      = ("#F3EEFF", "#7B2FBE")   # New / Hub — purple
# BOX_BRAND is set above in brand config    # Brand AI System — brand colour
BOX_FUTURE   = ("#FFF3E0", "#E07000")   # Future / TBC — orange
BOX_NEUTRAL  = ("#F0F0F0", "#888888")   # Neutral — light grey

# Row background colours (fill, edge)
ROW_A_BG = ("#EEF2FF", "#7090CC")
# ROW_B_BG is set above in brand config
ROW_C_BG = ("#FFF8EE", "#E07000")

TEXT_DARK   = "#1A1A1A"
TEXT_MED    = "#444444"
TEXT_LIGHT  = "#777777"
ARROW_COLOR = "#555555"
DIV_LINE    = "#DDDDDD"

# ── Figure ─────────────────────────────────────────────────────────────────────
FW, FH = 17, 11   # landscape, inches
fig = plt.figure(figsize=(FW, FH), facecolor=WHITE)
ax  = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, FW)
ax.set_ylim(0, FH)
ax.axis('off')
ax.set_facecolor(WHITE)

# ── Helpers ────────────────────────────────────────────────────────────────────
def box(cx, cy, w, h, fc, ec, lw=1.2, radius=0.18, zorder=4):
    rect = FancyBboxPatch(
        (cx - w/2, cy - h/2), w, h,
        boxstyle=f"round,pad=0,rounding_size={radius}",
        facecolor=fc, edgecolor=ec, linewidth=lw, zorder=zorder
    )
    ax.add_patch(rect)

def txt(x, y, s, fs=8, color=TEXT_DARK, bold=False,
        ha='center', va='center', zorder=5, style='normal'):
    ax.text(x, y, s, fontsize=fs, color=color,
            fontweight='bold' if bold else 'normal',
            ha=ha, va=va, zorder=zorder, style=style, clip_on=False)

def arrow_h(x0, x1, y, color=ARROW_COLOR, lw=1.2, ms=8):
    ax.annotate("", xy=(x1, y), xytext=(x0, y),
                arrowprops=dict(arrowstyle='->', color=color,
                                lw=lw, mutation_scale=ms), zorder=3)

def arrow_v(x, y0, y1, color=ARROW_COLOR, lw=1.2, ms=8):
    ax.annotate("", xy=(x, y1), xytext=(x, y0),
                arrowprops=dict(arrowstyle='->', color=color,
                                lw=lw, mutation_scale=ms), zorder=3)

def badge(x, y, n, zorder=8):
    circ = plt.Circle((x, y), 0.16, fc=BADGE_ORANGE, ec="white",
                      lw=0.8, zorder=zorder)
    ax.add_patch(circ)
    ax.text(x, y, str(n), fontsize=6.5, color="white", fontweight='bold',
            ha='center', va='center', zorder=zorder+1)

def row_bg(y_bottom, height, fc, ec, label_text, label_color):
    rect = FancyBboxPatch(
        (0.3, y_bottom), FW - 0.6, height,
        boxstyle="round,pad=0,rounding_size=0.15",
        facecolor=fc, edgecolor=ec, linewidth=1.5,
        zorder=1, alpha=0.55
    )
    ax.add_patch(rect)
    ax.text(0.62, y_bottom + height/2, label_text,
            fontsize=7.5, color=label_color, fontweight='bold',
            ha='center', va='center', rotation=90, zorder=3,
            bbox=dict(boxstyle='round,pad=0.25', fc=fc, ec=ec, lw=1.2))

def divider(y):
    ax.plot([0.3, FW - 0.3], [y, y], color=DIV_LINE, lw=0.8, zorder=2)

# ══════════════════════════════════════════════════════════════════════════════
# HEADER
# ══════════════════════════════════════════════════════════════════════════════
try:
    logo = Image.open(BRAND_LOGO_PATH).convert("RGBA")
    if BRAND_LOGO_BG:
        # Composite white logo onto dark background using PIL —
        # set_facecolor() does NOT work because imshow() composites
        # transparent pixels against the figure background, not the axes bg.
        r, g, b = int(BRAND_LOGO_BG[1:3], 16), int(BRAND_LOGO_BG[3:5], 16), int(BRAND_LOGO_BG[5:7], 16)
        bg = Image.new("RGBA", logo.size, (r, g, b, 255))
        bg.paste(logo, mask=logo.split()[3])
        logo = bg
    logo_ax = fig.add_axes([0.012, 0.915, 0.09, 0.065])
    logo_ax.imshow(np.array(logo))
    logo_ax.axis('off')
except Exception:
    ax.text(0.9, 10.55, BRAND_NAME, fontsize=14, color=BRAND_COLOR,
            fontweight='bold', ha='left', va='center')

ax.text(FW/2, 10.57, "{DIAGRAM_TITLE}",
        fontsize=14, color=TEXT_DARK, fontweight='bold',
        ha='center', va='center')
ax.text(FW/2, 10.30, "{SUBTITLE}",
        fontsize=8.5, color=TEXT_LIGHT, ha='center', va='center')

# ── Legend ────────────────────────────────────────────────────────────────────
leg_y = 10.00
leg_items = [
    (*BOX_EXIST,   "Existing System"),
    (*BOX_HUB,     "New / Central Hub"),
    (*BOX_BRAND,   BRAND_NAME + " System"),
    (*BOX_FUTURE,  "Future / TBC"),
    (*BOX_NEUTRAL, "Neutral / Endpoint"),
]
lx = 1.8
for fc, ec, label in leg_items:
    rect = FancyBboxPatch((lx, leg_y - 0.13), 0.38, 0.26,
                          boxstyle="round,pad=0,rounding_size=0.06",
                          facecolor=fc, edgecolor=ec, linewidth=1.2, zorder=5)
    ax.add_patch(rect)
    ax.text(lx + 0.52, leg_y, label, fontsize=7.2, color=TEXT_MED,
            ha='left', va='center', zorder=5)
    lx += 2.85

badge(lx + 0.18, leg_y, "Q", zorder=6)
ax.text(lx + 0.40, leg_y, "Open Question",
        fontsize=7.2, color=TEXT_MED, ha='left', va='center')

divider(9.72)

# ══════════════════════════════════════════════════════════════════════════════
# ROW A — {ROW_A_LABEL}
# ══════════════════════════════════════════════════════════════════════════════
A_Y  = 8.45
A_H  = 1.50
BW   = 1.55
BH   = 0.72
row_bg(A_Y - A_H/2 + 0.05, A_H - 0.05,
       *ROW_A_BG, "{ROW_A_LABEL}", ROW_A_BG[1])

# --- SYSTEMS FOR ROW A ---
# For each system, call box() then txt() then arrow_h() to next system.
# Example (3-system row):
# A_xs = [1.65, 5.50, 9.35]
# box(A_xs[0], A_Y, BW, BH, *BOX_NEUTRAL)
# txt(A_xs[0], A_Y+0.11, "System Name", fs=8.5, bold=True)
# txt(A_xs[0], A_Y-0.11, "Subtitle", fs=8.5)
# txt(A_xs[0], A_Y-0.32, "Description line", fs=6.8, color=TEXT_LIGHT)
# arrow_h(A_xs[0]+BW/2, A_xs[1]-BW/2, A_Y)
# ... repeat for each system

# {ROW_A_SYSTEMS_CODE}

divider({ROW_A_DIVIDER_Y})

# ══════════════════════════════════════════════════════════════════════════════
# ROW B — {ROW_B_LABEL}
# ══════════════════════════════════════════════════════════════════════════════
B_Y  = 6.22
B_H  = 1.65
row_bg(B_Y - B_H/2 + 0.05, B_H - 0.05,
       *ROW_B_BG, "{ROW_B_LABEL}", ROW_B_BG[1])

# {ROW_B_SYSTEMS_CODE}

divider({ROW_B_DIVIDER_Y})

# ══════════════════════════════════════════════════════════════════════════════
# ROW C — {ROW_C_LABEL}   [only include if Phase 2 / future row needed]
# ══════════════════════════════════════════════════════════════════════════════
C_Y  = 4.60
C_H  = 1.45
row_bg(C_Y - C_H/2 + 0.05, C_H - 0.05,
       *ROW_C_BG, "{ROW_C_LABEL}", ROW_C_BG[1])

# {ROW_C_SYSTEMS_CODE}

divider(3.88)

# ══════════════════════════════════════════════════════════════════════════════
# OPEN QUESTIONS
# ══════════════════════════════════════════════════════════════════════════════
Q_Y0 = 3.70
ax.text(0.5, Q_Y0 + 0.08, "Open Questions",
        fontsize=9, color=TEXT_DARK, fontweight='bold', va='center')

questions = [
    # (number, "Question text")
    # {QUESTIONS}
]

col1_qs = questions[:3]
col2_qs = questions[3:]
col1_x = 0.45
col2_x = 8.70

for i, (n, q) in enumerate(col1_qs):
    y = Q_Y0 - 0.38 - i * 0.44
    badge(col1_x + 0.18, y + 0.04, n)
    ax.text(col1_x + 0.45, y + 0.04, q,
            fontsize=7.5, color=TEXT_MED, ha='left', va='center')

for i, (n, q) in enumerate(col2_qs):
    y = Q_Y0 - 0.38 - i * 0.44
    badge(col2_x + 0.18, y + 0.04, n)
    ax.text(col2_x + 0.45, y + 0.04, q,
            fontsize=7.5, color=TEXT_MED, ha='left', va='center')

# ══════════════════════════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════════════════════════
divider(0.52)
ax.text(0.5,      0.30, BRAND_NAME,
        fontsize=7.5, color=TEXT_LIGHT, ha='left',   va='center')
ax.text(FW/2,     0.30, "{FOOTER_TEXT}",
        fontsize=7.5, color=TEXT_LIGHT, ha='center', va='center', style='italic')
ax.text(FW - 0.5, 0.30, "1 of 1",
        fontsize=7.5, color=TEXT_LIGHT, ha='right',  va='center')

border = FancyBboxPatch((0.05, 0.05), FW - 0.10, FH - 0.10,
                        boxstyle="round,pad=0,rounding_size=0.2",
                        facecolor="none", edgecolor=DIV_LINE, lw=1.0, zorder=0)
ax.add_patch(border)

# ── Save ───────────────────────────────────────────────────────────────────────
import pathlib
save_dir = pathlib.Path("{SAVE_PATH}").expanduser()
save_dir.mkdir(parents=True, exist_ok=True)
base = str(save_dir / "{FILENAME_PREFIX}")

fig.savefig(base + ".pdf", dpi=200, bbox_inches='tight',
            facecolor=WHITE, edgecolor='none')
# Temp PNG for visual inspection during render-validate loop (not a deliverable)
fig.savefig("/tmp/_diagram_preview.png", dpi=100, bbox_inches='tight',
            facecolor=WHITE, edgecolor='none')
plt.close()
print("SAVED_PDF:", base + ".pdf")
print("PREVIEW_PNG: /tmp/_diagram_preview.png")
```

### Pre-generation validation

Before writing the script, mentally walk through these tests (adapted from the Excalidraw diagram skill):

1. **Structure test**: If you removed all text from the diagram, would the swim lanes + arrows + box layout alone communicate the flow? If not, the layout needs restructuring — not more text.
2. **Text overflow pre-check**: For every box label, check: does the longest line fit within `BW` at the given `fs`? Rule of thumb: at `fs=8.5`, approximately 14-16 characters fit in `BW=1.55`. If a label exceeds this, either widen the box, split the text, or reduce font size.
3. **Box count check**: More than 5 boxes in a single row requires tighter spacing (see dynamic box width table below). More than 8 boxes means you need sub-rows.
4. **Arrow sanity**: Sketch the arrow routing mentally. If two arrows would cross, consider rearranging box order to eliminate the crossing.

### Filling the template — rules

**Spacing / layout:**
- Figure coordinate system: x ∈ [0, FW], y ∈ [0, FH]. Origin bottom-left.
- Standard box: BW=1.55, BH=0.72. Wider central-hub boxes: ~1.70–1.80.
- Leave ~0.10–0.15 gap between boxes for arrows.
- Spread systems evenly across x ∈ [1.3, FW-0.5].
- Row A centre Y ≈ 8.45, Row B centre Y ≈ 6.22, Row C centre Y ≈ 4.60.
- Dividers sit ~0.80 below each row's bottom edge.
- Open questions block: Y from ~3.70 down to ~0.60.

**Dynamic box width (by box count per row):**

| Boxes per row | BW   | FW  | Description font fs | Notes |
|---------------|------|-----|---------------------|-------|
| 1–5           | 1.55 | 17  | 6.8                 | Standard layout |
| 6             | 1.45 | 17  | 6.8                 | Slightly narrower boxes |
| 7             | 1.35 | 18  | 6.0                 | Narrower boxes, wider figure |
| 8             | 1.25 | 19  | 6.0                 | Compact boxes, wide figure |

For even distribution across n boxes: `margin = 1.3; xs = [margin + i * (FW - 2*margin) / (n-1) for i in range(n)]`

**Colour assignment per system:**
- Map each system the user described to one of: BOX_EXIST, BOX_HUB, BOX_INSPRA, BOX_FUTURE, BOX_NEUTRAL
- Unpack colour pairs with `*BOX_XXX` → `fc, ec`

**Text inside boxes (3-line standard):**
```python
txt(cx, cy+0.11, "Primary Name",    fs=8.5, bold=True)
txt(cx, cy-0.11, "Secondary label", fs=8.5)
txt(cx, cy-0.32, "Description",     fs=6.8, color=TEXT_LIGHT)
```

**Arrows between systems:**
- Horizontal: `arrow_h(x_left_edge_of_next - gap, x_right_edge_of_prev + gap, row_Y)`
- Vertical (rare): `arrow_v(x, y0, y1)`
- Fan-out (one system → multiple outcomes): use annotate per outcome from a common xytext
- Diagonal / dependency (cross-row cascade within the SAME swim lane): use `ax.annotate()` directly with `linestyle='dashed'`:
```python
ax.annotate("", xy=(target_x, target_y),
            xytext=(source_x, source_y),
            arrowprops=dict(arrowstyle='->', color='#7B2FBE',
                            lw=1.0, mutation_scale=8, linestyle='dashed'), zorder=3)
```
  Use dashed lines to show dependencies between boxes in different sub-rows (e.g. "L1+L2 cascade → L6"). Add a small `txt()` label near the arrow origin to explain the relationship.
- **Cross-row arrows (BETWEEN swim lanes) — MUST be vertical, never diagonal:**
  When connecting Row B → Row C (or any row to the row below), use clean vertical `arrow_v()` calls
  aligned to the **target box's x-centre**, NOT the source box's x-position. Diagonal cross-row arrows
  look messy and misaligned. Pattern:
```python
# Drop vertical arrows from divider to each target box
divider_y = B_BOT - BH/2 - 0.45   # the divider between rows
for cx in C_xs:                     # C_xs = target box centres
    arrow_v(cx, divider_y - 0.05, C_Y + BH/2 + 0.05, color='#2D8A2D', lw=1.0)
```
  **Never** use `ax.annotate()` with mismatched source/target x-coordinates for cross-row arrows —
  this creates diagonals that look broken.

**Open questions (badge-question parity rule — MANDATORY):**
- Only include if the user actually has open questions.
- Number them 1, 2, 3... matching badge numbers on the diagram.
- **Badge numbers must follow left-to-right reading order.** The leftmost box with a question gets badge 1, the next one to the right gets badge 2, etc. The `questions` list at the bottom must match this same order. The customer reads the diagram left to right, so the numbering must be consistent with that flow.
- **Every question in the `questions` list MUST have a corresponding `badge()` call on a box in the diagram.** If Q1 is about Webtrack GPS and Q2 is about ServiceM8, then both the Webtrack GPS box and the ServiceM8 box must have `badge(x, y, 1)` and `badge(x, y, 2)` respectively. A question without a visible badge on a box is a defect.
- **Exception:** If the question refers to a system that is not shown as a box in this diagram (e.g. a lever diagram that does not show data source boxes), the badge is omitted and the question stands alone. This is acceptable only when the relevant box genuinely does not exist in the diagram.
- If no open questions, set `questions = []` and omit the block entirely (or render a simple "No open questions at this time." line).

**Row label format:**
- Short, fits vertically: 2–3 lines max. Use `\n` to break.
- Example: `"CURRENT STATE\n(pre-Inspra AI)"`

**Adapting row count:**
- 2 rows: use Row A (y≈8.45) and Row B (y≈6.22). Skip Row C. Move open questions up.
- 3 rows: A, B, C as above. Standard layout.
- 4+ rows: compress row heights and adjust Y centres proportionally.

**Sub-rows within a single swim lane:**
When a row needs two lines of boxes (e.g. 7 items split 4+3), increase the row height to ~2.50 and create two centre-Y values:
- `B_TOP = 7.85` (upper sub-row), `B_BOT = 6.65` (lower sub-row)
- Increase figure height to `FH = 12.5` to accommodate the extra space
- Add sub-row category labels above each group using `txt()` with `bold=True` and category colour
- Use diagonal dependency arrows (see above) to show cross-sub-row relationships

**Custom colour categories:**
The five standard categories (EXIST, HUB, BRAND, FUTURE, NEUTRAL) cover most cases. For diagrams that need additional semantic categories, define custom `(fill, edge)` tuples:
```python
BOX_OUTCOME  = ("#E8FAE8", "#2D8A2D")   # Positive outcome — green
```
Update the legend `leg_items` list to match. Keep total legend items ≤ 6 to fit on one line.

**Lever / tag labels below boxes:**
For diagrams that map levers or categories to processing modules, add a small tag line below the box:
```python
txt(cx, cy - 0.48, "L1  L3  L5  L6", fs=6, color=BRAND_DARK, bold=True)
```

---

## Phase 3 — Render → Inspect → Fix → Re-render (mandatory loop)

This phase uses a **mandatory visual validation loop**. Do NOT deliver the diagram after a single render. Always inspect and iterate.

### Step 1: First render
1. Write the complete Python script to `/tmp/blueprint_{client}_{date}.py`
2. Run: `python3 /tmp/blueprint_{client}_{date}.py`
3. If it fails, read the error, fix the script, and re-run (max 3 attempts for runtime errors)

### Step 2: Visual inspection (MANDATORY)
4. **Read the temp PNG (`/tmp/_diagram_preview.png`) using the Read tool** — this is non-negotiable. You MUST visually inspect every render.
5. Run through the **Visual Defect Checklist** below. For each item, determine pass/fail.

### Step 3: Fix and re-render (if any defect found)
6. If ANY visual defect is found:
   - Identify the root cause in the script (coordinates, font sizes, spacing, etc.)
   - Edit the script file to fix the issue
   - Re-run the script to regenerate PDF + temp PNG
   - **Go back to Step 2** — re-read the temp PNG and re-inspect
7. Repeat until all checklist items pass. Typical: 1-3 iterations.

### Step 4: Deliver
8. Confirm `.pdf` was saved (parse `SAVED_PDF:` from stdout)
9. Report the PDF save path to the user
10. Show the final preview inline (Read the temp PNG via Read tool)

---

## Phase 4 — Companion Write-up (PDF)

After the diagram is finalised, generate a branded companion document that explains it. This is a **standard deliverable** — always produce it alongside the diagram PDF.

### Write-up structure

The write-up is a branded `.docx` converted to PDF, using the `/brand-doc` skill patterns. Follow the AA or Inspra brand formatting (logo, colours, fonts, footer) matching the diagram's brand.

| Section | Content |
|---------|---------|
| **Title** | Same as diagram title |
| **Subtitle** | "Companion Guide to the [Diagram Type] Diagram" |
| **Overview** | 2-3 paragraphs: what the business does, the problem, and the headline outcome |
| **How to Read the Diagram** | 3-5 bullets explaining rows, colour categories, and arrow meanings |
| **Detail per item** | For each major box/system/lever in the diagram: a heading, impact line (bold), and 2-3 sentence explanation |
| **Summary table** | Lever/system name, category, and impact — branded table with orange/green header |
| **Phased rollout** | If the diagram includes phases: timeline, cost, and deliverable per phase |
| **Investment summary** | Total cost, expected return, payback period |
| **Next steps** | 3-5 actionable bullets for the client |

### Write-up rules

- **Australian English** — organisation, colour, recognise, optimise
- **No contractions** — "do not" not "don't", "it is" not "it's"
- **No dashes as punctuation** — use commas instead. Hyphens only in compound words.
- Content should be **client-facing** — professional, concise, no internal jargon
- Derive all facts from the diagram and conversation context. Do not invent numbers.
- **Footer text format (both brands):** Use wider spacing around the separator and include `https://`:
  - AA: `Automate Accelerator   |   https://automateaccelerator.com.au`
  - Inspra: `Inspra AI   |   https://inspra.ai`
  - Right side: `Page {n}  |  {DD Month YYYY}`
- Generate as PDF directly using ReportLab (not docx-to-PDF conversion). Use the `/brand-doc` brand config (colours, logo path, footer) but render via ReportLab's `SimpleDocTemplate` with `canvas.drawImage` for the logo header and `canvas.line` for the orange rule. This avoids the LibreOffice/docx2pdf dependency.
- ReportLab logo pattern (calculate height from aspect ratio, then draw rule BELOW logo — never before):
  ```python
  from reportlab.lib.utils import ImageReader
  img = ImageReader(LOGO_PATH)
  iw, ih = img.getSize()
  logo_w = 34*mm
  logo_h = logo_w * ih / iw
  LOGO_TOP = H - 5*mm                      # logo top edge, 5mm from page top
  logo_bottom = LOGO_TOP - logo_h
  canvas.drawImage(LOGO_PATH, 20*mm, logo_bottom, width=logo_w, height=logo_h, mask='auto')
  # Orange rule sits 2mm below the logo — measure first, draw second
  rule_y = logo_bottom - 2*mm
  canvas.setStrokeColor(BRAND_COLOR_RL)    # ReportLab color object for brand colour
  canvas.setLineWidth(1.5)
  canvas.line(20*mm, rule_y, W - 20*mm, rule_y)
  ```
  **Critical:** always draw the logo first, calculate `logo_bottom`, then position the rule at `logo_bottom - 2*mm`. Never set a fixed Y for the rule before knowing the logo height — this is what causes the rule to slice through the logo.

### ReportLab table cell wrapping rule (MANDATORY)

**Never put plain strings directly into Table cell data.** ReportLab silently truncates plain strings that overflow a cell — no error is raised, content is simply lost. Always wrap every body cell in a `Paragraph` object so text word-wraps and the row height expands automatically.

```python
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle

s_cell_hdr  = ParagraphStyle("cell_hdr",  fontSize=9,   textColor=WHITE,     fontName="Helvetica-Bold", leading=13)
s_cell_body = ParagraphStyle("cell_body", fontSize=8.5, textColor=TEXT_DARK, fontName="Helvetica",      leading=13)

def make_table(data, col_widths):
    wrapped = []
    for r_idx, row in enumerate(data):
        new_row = []
        for cell in row:
            style = s_cell_hdr if r_idx == 0 else s_cell_body
            new_row.append(Paragraph(str(cell), style) if isinstance(cell, str) else cell)
        wrapped.append(new_row)
    t = Table(wrapped, colWidths=col_widths, repeatRows=1, hAlign="LEFT")
    # ... apply TableStyle as normal
    return t
```

**Also set `VALIGN: TOP` in the TableStyle** when cells contain Paragraph objects — `MIDDLE` alignment can misalign multi-line cells.

### Write-up page-break rules (MANDATORY)

These prevent sections from splitting awkwardly across pages:

1. **Plan page layout upfront** — before writing the story list, decide which sections go on which page. Use explicit `PageBreak()` between page groups.
2. **Short sections (≤8 items): wrap entire section in `KeepTogether`** — use `section_block()`:
   ```python
   def section_block(title, items):
       return KeepTogether([
           Paragraph(title, s_h1),
           Spacer(1, 2*mm),
           *items,
       ])
   ```
3. **Phase/week sections: always `KeepTogether`** — a phase (objective + 4 weeks + levers) is ~7 items and must never split mid-week.
4. **Long sections (>8 items or multi-paragraph prose): use `section_flow()`** — keeps heading + first 2 items together, lets rest flow.
   ```python
   def section_flow(title, items):
       heading = Paragraph(title, s_h1)
       sp = Spacer(1, 2*mm)
       if len(items) >= 2:
           return [KeepTogether([heading, sp, items[0], items[1]])] + items[2:]
       elif items:
           return [KeepTogether([heading, sp, items[0]])] + items[1:]
       return [heading, sp]
   ```
5. **Consistent inter-section spacing** — use `Spacer(1, 4*mm)` between sections on the same page.
6. **Never let a bullet list split** — if you have ≤6 bullets, wrap them all in `KeepTogether`.
7. **Tables with heading: wrap together** — `KeepTogether([heading, spacer, table])` for tables ≤4 data rows.

### Filename convention

`{BrandPrefix}_{Client}_{DiagramType}_Writeup_{YYYYMMDD}.pdf`

Example: `AA_BinBath_Lever_Map_Writeup_2026-03-15.pdf`

Save to the same folder as the diagram PDF.

### Delivery

Report both file paths to the user:
1. Diagram PDF: `{SAVE_PATH}/{FILENAME_PREFIX}.pdf`
2. Write-up PDF: `{SAVE_PATH}/{BrandPrefix}_{Client}_{Type}_Writeup_{date}.pdf`

---

## Pre-render Checklist (before first run)

- [ ] `BRAND` set to `"inspra"` or `"aa"` (not left as `"{BRAND}"`)
- [ ] All other placeholder strings `{...}` replaced with real values
- [ ] No syntax errors (check indentation, unclosed brackets)
- [ ] At least one system per row
- [ ] `arrow_h` x-coordinates don't overlap box bodies
- [ ] `questions` list is valid Python (trailing comma on last item)
- [ ] `SAVE_PATH` and `FILENAME_PREFIX` are correctly set
- [ ] Logo path uses `os.path.expanduser` or `pathlib.Path.expanduser()`
- [ ] PDF save call and temp PNG preview save are both present

---

## Visual Defect Checklist (after each render)

Run through this checklist every time you Read the PNG. Fix any failures before delivering.

### Layout & Spacing
- [ ] **Box overlap**: No boxes overlap or touch each other
- [ ] **Even spacing**: Boxes within the same row are evenly spaced (visually consistent gaps)
- [ ] **Row alignment**: All boxes in a row sit at the same vertical centre
- [ ] **Swim lane sizing**: Row backgrounds fully contain all their boxes with visible padding
- [ ] **Margin safety**: No content touches or extends beyond the outer border

### Text
- [ ] **Text clipping**: No text visually overflows its containing box (check long labels)
- [ ] **Text readability**: All text is legible at the rendered resolution (minimum fs=6.5)
- [ ] **Label hierarchy**: Bold titles are visually distinct from subtitles and descriptions
- [ ] **Row labels**: Vertical swim lane labels are fully readable (not cropped or overlapping content)

### Arrows & Connections
- [ ] **Arrow routing**: Arrows connect between boxes, not through them
- [ ] **Arrow direction**: All arrows point in the correct direction (flow goes top-to-bottom or left-to-right)
- [ ] **Dependency arrows**: Dashed diagonal arrows (if any) are visually distinct from flow arrows
- [ ] **No orphan arrows**: Every arrow has a clear source and target box

### Branding & Structure
- [ ] **Logo visible**: Brand logo renders correctly in the top-left corner (or fallback text appears)
- [ ] **Legend accuracy**: Legend items match the colour categories actually used in the diagram
- [ ] **Correct brand colours**: AA uses orange (#F47920) + purple (#412F8F), Inspra uses green (#39E100)
- [ ] **Footer present**: Footer line with brand name, confidentiality text, and page number is visible
- [ ] **Badge placement**: Question badges sit on box corners, not floating in empty space
- [ ] **Badge-question parity**: Count the `badge()` calls on boxes and compare to the `questions` list. Every question number must have a matching badge on a box (unless the relevant system is not shown as a box in this diagram)

### Composition (overall impression)
- [ ] **Visual balance**: The diagram does not feel lopsided or cramped in one area
- [ ] **Whitespace**: Adequate breathing room between sections (rows, questions, footer)
- [ ] **Professional quality**: Would you send this PDF to a client without hesitation?

### Common fixes for defects found during inspection

| Defect | Fix |
|--------|-----|
| Text overflows box | Widen the box (`BW += 0.30`), shorten text, or reduce `fs` by 0.5-1pt |
| Boxes too close together | Increase x-spacing between items in the `xs` array by 0.3-0.5 |
| Row label cropped by content | Move the first box rightward (increase minimum x to 1.8+) |
| Arrow passes through a box | Add waypoints using multiple annotate calls, or adjust Y offset |
| Swim lane too short | Increase `_H` value by 0.2-0.4 and shift lower rows down |
| Legend overflows right edge | Reduce `lx` spacing from 2.85 to 2.5, or reduce legend items |
| Open questions text cropped | Move `col2_x` left, or reduce `fontsize` to 7.0 |
| Uneven vertical spacing | Recalculate all `_Y` centres to maintain equal gaps between rows |
| Missing badge on box | Count `questions` list items vs `badge()` calls on boxes — add missing `badge(x + BW/2 - 0.10, y + BH/2 - 0.10, N)` |

---

## Common Errors & Fixes

| Error | Fix |
|-------|-----|
| `ModuleNotFoundError: PIL` | Run `pip3 install Pillow` first |
| `ModuleNotFoundError: matplotlib` | Run `pip3 install matplotlib` first |
| Logo not found | Script has try/except fallback — logo silently skipped |
| Boxes overlap | Increase spacing in x-coordinate list |
| Text clipped | Reduce font size or shorten label text |
| Arrows miss boxes | Recalculate `x ± BW/2` edge positions |

---

## Reference Implementation
The SkyMesh v3/v4 diagrams (`/tmp/skymesh_arch_v3.py`, `/tmp/skymesh_arch_v4.py`) are the canonical reference. Study them for complex fan-out arrows, "NEW" badge chips on boxes, and side-by-side agent pool layouts. Do NOT modify those files.

**BinBath references** (added 2026-03-15):
- `/tmp/blueprint_binbath_lever_map_20260315.py` — demonstrates sub-rows within a single swim lane (7 items split 4+3), diagonal dependency arrows (dashed), custom `BOX_OUTCOME` colour, and `FH=12.5` for taller layouts.
- `/tmp/blueprint_binbath_dataarch_20260315.py` — standard 3-row data architecture (5 sources → 4 engine modules → 3 outputs), lever tag labels below boxes, verdict text between rows.

---

## Team Distribution
This skill lives at `~/.claude/skills/diagram/SKILL.md`.
To share: copy the `diagram/` folder into any team member's `~/.claude/skills/` directory.
