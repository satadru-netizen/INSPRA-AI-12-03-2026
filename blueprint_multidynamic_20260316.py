import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from PIL import Image
import numpy as np
import os
import pathlib
import tempfile

# ── Brand config ──────────────────────────────────────────────────────────────
BRAND = "inspra"

BRAND_NAME      = "Inspra AI"
BRAND_COLOR     = "#39E100"
BRAND_DARK      = "#1A3A00"
BRAND_LOGO_PATH = os.path.expanduser(
    "~/.claude/skills/diagram/assets/Inspra-logo-dark.png"
)
BRAND_LOGO_BG   = None
BOX_BRAND       = ("#E8FAE0", "#39E100")
ROW_B_BG        = ("#EDFCE5", "#39E100")

# ── Colours ────────────────────────────────────────────────────────────────────
WHITE        = "#FFFFFF"
BADGE_ORANGE = "#FF6B00"

BOX_EXIST    = ("#E8F0FE", "#4A6FA5")
BOX_HUB      = ("#F3EEFF", "#7B2FBE")
BOX_FUTURE   = ("#FFF3E0", "#E07000")
BOX_NEUTRAL  = ("#F0F0F0", "#888888")

ROW_A_BG = ("#EEF2FF", "#7090CC")
ROW_C_BG = ("#FFF8EE", "#E07000")

TEXT_DARK   = "#1A1A1A"
TEXT_MED    = "#444444"
TEXT_LIGHT  = "#777777"
ARROW_COLOR = "#555555"
DIV_LINE    = "#DDDDDD"

# ── Figure ─────────────────────────────────────────────────────────────────────
FW, FH = 17, 11
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
    logo_ax = fig.add_axes([0.012, 0.915, 0.09, 0.065])
    logo_ax.imshow(np.array(logo))
    logo_ax.axis('off')
except Exception:
    ax.text(0.9, 10.55, BRAND_NAME, fontsize=14, color=BRAND_COLOR,
            fontweight='bold', ha='left', va='center')

ax.text(FW/2, 10.57, "Blueprint — Multi Dynamic × Inspra AI",
        fontsize=14, color=TEXT_DARK, fontweight='bold',
        ha='center', va='center')
ax.text(FW/2, 10.30, "Inspra AI  |  16 March 2026  |  v1",
        fontsize=8.5, color=TEXT_LIGHT, ha='center', va='center')

# ── Legend ────────────────────────────────────────────────────────────────────
leg_y = 10.00
leg_items = [
    (*BOX_EXIST,   "Existing System"),
    (*BOX_HUB,     "New / Central Hub"),
    (*BOX_BRAND,   "Inspra AI System"),
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
# ROW A — CURRENT STATE
# ══════════════════════════════════════════════════════════════════════════════
A_Y  = 8.45
A_H  = 1.50
BW   = 1.55
BH   = 0.72
row_bg(A_Y - A_H/2 + 0.05, A_H - 0.05,
       *ROW_A_BG, "CURRENT STATE\n(pre-Inspra AI)", ROW_A_BG[1])

# 5 systems: RP Data, ID for Me, Mobile Contacts, Vault-RE, Google Calendar
A_xs = [2.00, 4.80, 7.60, 10.70, 13.80]

# RP Data
box(A_xs[0], A_Y, BW, BH, *BOX_EXIST)
txt(A_xs[0], A_Y+0.11, "RP Data", fs=8.5, bold=True)
txt(A_xs[0], A_Y-0.11, "Property Data", fs=8.5)
txt(A_xs[0], A_Y-0.32, "~12-13K records", fs=6.8, color=TEXT_LIGHT)

# ID for Me
box(A_xs[1], A_Y, BW, BH, *BOX_EXIST)
txt(A_xs[1], A_Y+0.11, "ID for Me", fs=8.5, bold=True)
txt(A_xs[1], A_Y-0.11, "Data Source", fs=8.5)
txt(A_xs[1], A_Y-0.32, "~12-13K records", fs=6.8, color=TEXT_LIGHT)

# Mobile Contacts
box(A_xs[2], A_Y, BW, BH, *BOX_EXIST)
txt(A_xs[2], A_Y+0.11, "Mobile Contacts", fs=8, bold=True)
txt(A_xs[2], A_Y-0.11, "Megha + Tirtha", fs=8.5)
txt(A_xs[2], A_Y-0.32, "~12K+ contacts", fs=6.8, color=TEXT_LIGHT)
badge(A_xs[2] + BW/2 - 0.10, A_Y + BH/2 - 0.10, 1)

# Vault-RE (CRM)
box(A_xs[3], A_Y, 1.70, BH, *BOX_HUB)
txt(A_xs[3], A_Y+0.11, "Vault-RE", fs=8.5, bold=True)
txt(A_xs[3], A_Y-0.11, "CRM (Central)", fs=8.5)
txt(A_xs[3], A_Y-0.32, "~3K contacts, 7 offices", fs=6.5, color=TEXT_LIGHT)
badge(A_xs[3] + 1.70/2 - 0.10, A_Y + BH/2 - 0.10, 2)

# Google Calendar
box(A_xs[4], A_Y, BW, BH, *BOX_EXIST)
txt(A_xs[4], A_Y+0.11, "Google", fs=8.5, bold=True)
txt(A_xs[4], A_Y-0.11, "Calendar", fs=8.5)
txt(A_xs[4], A_Y-0.32, "Synced with Vault-RE", fs=6.5, color=TEXT_LIGHT)
badge(A_xs[4] + BW/2 - 0.10, A_Y + BH/2 - 0.10, 3)

# Arrows Row A: data sources → Vault-RE
arrow_h(A_xs[0] + BW/2 + 0.05, A_xs[1] - BW/2 - 0.05, A_Y)
arrow_h(A_xs[1] + BW/2 + 0.05, A_xs[2] - BW/2 - 0.05, A_Y)
arrow_h(A_xs[2] + BW/2 + 0.05, A_xs[3] - 1.70/2 - 0.05, A_Y)
arrow_h(A_xs[3] + 1.70/2 + 0.05, A_xs[4] - BW/2 - 0.05, A_Y)

divider(7.50)

# ══════════════════════════════════════════════════════════════════════════════
# ROW B — PROPOSED PHASE 1 (Inspra AI)
# ══════════════════════════════════════════════════════════════════════════════
B_Y  = 6.22
B_H  = 1.65
row_bg(B_Y - B_H/2 + 0.05, B_H - 0.05,
       *ROW_B_BG, "PROPOSED\nPHASE 1", ROW_B_BG[1])

# 6 systems
B_xs = [1.80, 4.30, 6.80, 9.50, 12.20, 14.90]
B_BW = 1.55

# Data Import & Dedup
box(B_xs[0], B_Y, B_BW, BH, *BOX_BRAND)
txt(B_xs[0], B_Y+0.11, "Data Import", fs=8.5, bold=True)
txt(B_xs[0], B_Y-0.11, "& Dedup", fs=8.5)
txt(B_xs[0], B_Y-0.32, "~32K → ~8-10K clean", fs=6.5, color=TEXT_LIGHT)

# AI Outbound Agent
box(B_xs[1], B_Y, B_BW, BH, *BOX_BRAND)
txt(B_xs[1], B_Y+0.11, "AI Outbound", fs=8.5, bold=True)
txt(B_xs[1], B_Y-0.11, "Agent", fs=8.5)
txt(B_xs[1], B_Y-0.32, "Calls, verifies, qualifies", fs=6.5, color=TEXT_LIGHT)

# Disposition Tagging
box(B_xs[2], B_Y, B_BW, BH, *BOX_BRAND)
txt(B_xs[2], B_Y+0.11, "Disposition", fs=8.5, bold=True)
txt(B_xs[2], B_Y-0.11, "Tagging", fs=8.5)
txt(B_xs[2], B_Y-0.32, "Hot/Warm/Cold/Invalid", fs=6.5, color=TEXT_LIGHT)

# Vault-RE (CRM) — receives data
box(B_xs[3], B_Y, 1.70, BH, *BOX_HUB)
txt(B_xs[3], B_Y+0.11, "Vault-RE", fs=8.5, bold=True)
txt(B_xs[3], B_Y-0.11, "CRM (Updated)", fs=8.5)
txt(B_xs[3], B_Y-0.32, "Transcripts + tags", fs=6.5, color=TEXT_LIGHT)

# Appointment Booking
box(B_xs[4], B_Y, B_BW, BH, *BOX_BRAND)
txt(B_xs[4], B_Y+0.11, "Appointment", fs=8.5, bold=True)
txt(B_xs[4], B_Y-0.11, "Booking", fs=8.5)
txt(B_xs[4], B_Y-0.32, "Calendar sync", fs=6.5, color=TEXT_LIGHT)

# Email / SMS Notifications
box(B_xs[5], B_Y, B_BW, BH, *BOX_NEUTRAL)
txt(B_xs[5], B_Y+0.11, "Email / SMS", fs=8.5, bold=True)
txt(B_xs[5], B_Y-0.11, "Notifications", fs=8.5)
txt(B_xs[5], B_Y-0.32, "Callbacks + follow-ups", fs=6.5, color=TEXT_LIGHT)

# Arrows Row B
arrow_h(B_xs[0] + B_BW/2 + 0.05, B_xs[1] - B_BW/2 - 0.05, B_Y)
arrow_h(B_xs[1] + B_BW/2 + 0.05, B_xs[2] - B_BW/2 - 0.05, B_Y)
arrow_h(B_xs[2] + B_BW/2 + 0.05, B_xs[3] - 1.70/2 - 0.05, B_Y)
arrow_h(B_xs[3] + 1.70/2 + 0.05, B_xs[4] - B_BW/2 - 0.05, B_Y)
arrow_h(B_xs[4] + B_BW/2 + 0.05, B_xs[5] - B_BW/2 - 0.05, B_Y)

# Cross-row vertical arrows: Current State → Phase 1
# Data sources feed into Data Import
for src_x in [A_xs[0], A_xs[1], A_xs[2]]:
    arrow_v(src_x, A_Y - BH/2 - 0.05, 7.50 - 0.02, color='#39E100', lw=1.0)

arrow_v(B_xs[0], 7.50 + 0.02, B_Y + BH/2 + 0.05, color='#39E100', lw=1.0)

# Vault-RE current → Vault-RE updated
arrow_v(A_xs[3], A_Y - BH/2 - 0.05, 7.50 - 0.02, color='#7B2FBE', lw=1.0)
arrow_v(B_xs[3], 7.50 + 0.02, B_Y + BH/2 + 0.05, color='#7B2FBE', lw=1.0)

# Calendar current → Appointment Booking
arrow_v(A_xs[4], A_Y - BH/2 - 0.05, 7.50 - 0.02, color='#4A6FA5', lw=1.0)
arrow_v(B_xs[4], 7.50 + 0.02, B_Y + BH/2 + 0.05, color='#4A6FA5', lw=1.0)

divider(5.15)

# ══════════════════════════════════════════════════════════════════════════════
# ROW C — FUTURE (Phase 2+)
# ══════════════════════════════════════════════════════════════════════════════
C_Y  = 4.20
C_H  = 1.45
row_bg(C_Y - C_H/2 + 0.05, C_H - 0.05,
       *ROW_C_BG, "FUTURE\n(Phase 2+)", ROW_C_BG[1])

C_xs = [3.50, 8.50, 13.50]

# AI Inbound Agent
box(C_xs[0], C_Y, 1.70, BH, *BOX_FUTURE)
txt(C_xs[0], C_Y+0.11, "AI Inbound", fs=8.5, bold=True)
txt(C_xs[0], C_Y-0.11, "Agent", fs=8.5)
txt(C_xs[0], C_Y-0.32, "Handle incoming calls", fs=6.8, color=TEXT_LIGHT)

# Website Lead Capture
box(C_xs[1], C_Y, 1.70, BH, *BOX_FUTURE)
txt(C_xs[1], C_Y+0.11, "Website Lead", fs=8.5, bold=True)
txt(C_xs[1], C_Y-0.11, "Capture", fs=8.5)
txt(C_xs[1], C_Y-0.32, "Inquiry → pipeline", fs=6.8, color=TEXT_LIGHT)
badge(C_xs[1] + 1.70/2 - 0.10, C_Y + BH/2 - 0.10, 4)

# Multi-Office Rollout
box(C_xs[2], C_Y, 1.70, BH, *BOX_FUTURE)
txt(C_xs[2], C_Y+0.11, "Multi-Office", fs=8.5, bold=True)
txt(C_xs[2], C_Y-0.11, "Rollout", fs=8.5)
txt(C_xs[2], C_Y-0.32, "6 remaining franchises", fs=6.8, color=TEXT_LIGHT)

# Cross-row arrows: Phase 1 → Future
for cx in C_xs:
    arrow_v(cx, 5.15 - 0.05, C_Y + BH/2 + 0.05, color='#E07000', lw=1.0)

divider(3.28)

# ══════════════════════════════════════════════════════════════════════════════
# OPEN QUESTIONS
# ══════════════════════════════════════════════════════════════════════════════
Q_Y0 = 3.10
ax.text(0.5, Q_Y0 + 0.08, "Open Questions",
        fontsize=9, color=TEXT_DARK, fontweight='bold', va='center')

questions = [
    (1, "Mobile contacts import method (CSV export → Vault-RE bulk upload?)"),
    (2, "Vault-RE API capabilities and limitations — IT session needed"),
    (3, "Google Calendar ↔ Vault-RE sync — ensure no overlapping appointments"),
    (4, "Website inquiry integration — scope and timeline TBD"),
    (5, "Objection handling document — Megha to provide"),
    (6, "Agent assignment routing — Megha vs Tirtha vs assistants by suburb"),
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
ax.text(FW/2,     0.30, "Multi Dynamic × Inspra AI — Confidential",
        fontsize=7.5, color=TEXT_LIGHT, ha='center', va='center', style='italic')
ax.text(FW - 0.5, 0.30, "1 of 1",
        fontsize=7.5, color=TEXT_LIGHT, ha='right',  va='center')

border = FancyBboxPatch((0.05, 0.05), FW - 0.10, FH - 0.10,
                        boxstyle="round,pad=0,rounding_size=0.2",
                        facecolor="none", edgecolor=DIV_LINE, lw=1.0, zorder=0)
ax.add_patch(border)

# ── Save ───────────────────────────────────────────────────────────────────────
save_dir = pathlib.Path(os.path.expanduser("~/Desktop/MultiDynamic"))
save_dir.mkdir(parents=True, exist_ok=True)
base = str(save_dir / "Inspra_MultiDynamic_Blueprint_v1_20260316")

fig.savefig(base + ".pdf", dpi=200, bbox_inches='tight',
            facecolor=WHITE, edgecolor='none')

# Temp PNG for visual inspection
temp_dir = pathlib.Path(os.path.expanduser("~/Desktop/MultiDynamic"))
preview_path = str(temp_dir / "_diagram_preview.png")
fig.savefig(preview_path, dpi=100, bbox_inches='tight',
            facecolor=WHITE, edgecolor='none')
plt.close()
print("SAVED_PDF:", base + ".pdf")
print("PREVIEW_PNG:", preview_path)
