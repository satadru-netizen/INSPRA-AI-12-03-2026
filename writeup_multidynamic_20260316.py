import os
import pathlib
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether
)
from reportlab.lib.utils import ImageReader

# ── Brand config ──────────────────────────────────────────────────────────────
BRAND_NAME = "Inspra AI"
BRAND_COLOR_HEX = "#39E100"
BRAND_DARK_HEX = "#1A3A00"
BRAND_COLOR_RL = HexColor(BRAND_COLOR_HEX)
BRAND_DARK_RL = HexColor(BRAND_DARK_HEX)
LOGO_PATH = os.path.expanduser("~/.claude/skills/diagram/assets/Inspra-logo-dark.png")

TEXT_DARK = HexColor("#1A1A1A")
TEXT_MED = HexColor("#444444")
TEXT_LIGHT = HexColor("#777777")
WHITE = HexColor("#FFFFFF")
ROW_HEADER_BG = BRAND_COLOR_RL

W, H = A4

# ── Styles ────────────────────────────────────────────────────────────────────
s_title = ParagraphStyle("title", fontSize=18, textColor=TEXT_DARK,
                         fontName="Helvetica-Bold", leading=24, spaceAfter=4*mm)
s_subtitle = ParagraphStyle("subtitle", fontSize=11, textColor=TEXT_LIGHT,
                            fontName="Helvetica", leading=15, spaceAfter=8*mm)
s_h1 = ParagraphStyle("h1", fontSize=13, textColor=BRAND_DARK_RL,
                       fontName="Helvetica-Bold", leading=18, spaceBefore=6*mm,
                       spaceAfter=2*mm)
s_h2 = ParagraphStyle("h2", fontSize=11, textColor=TEXT_DARK,
                       fontName="Helvetica-Bold", leading=15, spaceBefore=4*mm,
                       spaceAfter=2*mm)
s_body = ParagraphStyle("body", fontSize=9.5, textColor=TEXT_DARK,
                        fontName="Helvetica", leading=14, spaceAfter=3*mm)
s_body_bold = ParagraphStyle("body_bold", fontSize=9.5, textColor=TEXT_DARK,
                             fontName="Helvetica-Bold", leading=14, spaceAfter=3*mm)
s_bullet = ParagraphStyle("bullet", fontSize=9.5, textColor=TEXT_DARK,
                          fontName="Helvetica", leading=14, spaceAfter=2*mm,
                          leftIndent=12, bulletIndent=0, bulletFontSize=9.5)
s_cell_hdr = ParagraphStyle("cell_hdr", fontSize=9, textColor=white,
                            fontName="Helvetica-Bold", leading=13)
s_cell_body = ParagraphStyle("cell_body", fontSize=8.5, textColor=TEXT_DARK,
                             fontName="Helvetica", leading=13)

# ── Header / Footer ──────────────────────────────────────────────────────────
def header_footer(canvas, doc):
    canvas.saveState()
    # Logo
    try:
        img = ImageReader(LOGO_PATH)
        iw, ih = img.getSize()
        logo_w = 34*mm
        logo_h = logo_w * ih / iw
        LOGO_TOP = H - 5*mm
        logo_bottom = LOGO_TOP - logo_h
        canvas.drawImage(LOGO_PATH, 20*mm, logo_bottom,
                         width=logo_w, height=logo_h, mask='auto')
        rule_y = logo_bottom - 2*mm
    except Exception:
        canvas.setFont("Helvetica-Bold", 14)
        canvas.setFillColor(BRAND_COLOR_RL)
        canvas.drawString(20*mm, H - 15*mm, BRAND_NAME)
        rule_y = H - 18*mm

    canvas.setStrokeColor(BRAND_COLOR_RL)
    canvas.setLineWidth(1.5)
    canvas.line(20*mm, rule_y, W - 20*mm, rule_y)

    # Footer
    canvas.setStrokeColor(HexColor("#DDDDDD"))
    canvas.setLineWidth(0.5)
    canvas.line(20*mm, 12*mm, W - 20*mm, 12*mm)

    canvas.setFont("Helvetica", 7)
    canvas.setFillColor(TEXT_LIGHT)
    canvas.drawString(20*mm, 7*mm, "Inspra AI   |   https://inspra.ai")
    canvas.drawRightString(W - 20*mm, 7*mm,
                           f"Page {doc.page}  |  16 March 2026")
    canvas.restoreState()

# ── Helpers ───────────────────────────────────────────────────────────────────
def bullet(text):
    return Paragraph(f"\u2022  {text}", s_bullet)

def section_block(title, items):
    return KeepTogether([
        Paragraph(title, s_h1),
        Spacer(1, 2*mm),
        *items,
    ])

def section_flow(title, items):
    heading = Paragraph(title, s_h1)
    sp = Spacer(1, 2*mm)
    if len(items) >= 2:
        return [KeepTogether([heading, sp, items[0], items[1]])] + items[2:]
    elif items:
        return [KeepTogether([heading, sp, items[0]])] + items[1:]
    return [heading, sp]

def make_table(data, col_widths):
    wrapped = []
    for r_idx, row in enumerate(data):
        new_row = []
        for cell in row:
            style = s_cell_hdr if r_idx == 0 else s_cell_body
            new_row.append(Paragraph(str(cell), style) if isinstance(cell, str) else cell)
        wrapped.append(new_row)
    t = Table(wrapped, colWidths=col_widths, repeatRows=1, hAlign="LEFT")
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), BRAND_COLOR_RL),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BACKGROUND', (0, 1), (-1, -1), HexColor("#F8F8F8")),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor("#DDDDDD")),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [HexColor("#FFFFFF"), HexColor("#F5FFF0")]),
    ]))
    return t

# ── Build Document ────────────────────────────────────────────────────────────
save_dir = pathlib.Path(os.path.expanduser("~/Desktop/MultiDynamic"))
save_dir.mkdir(parents=True, exist_ok=True)
out_path = str(save_dir / "Inspra_MultiDynamic_Blueprint_Writeup_20260316.pdf")

doc = SimpleDocTemplate(
    out_path, pagesize=A4,
    topMargin=32*mm, bottomMargin=18*mm,
    leftMargin=20*mm, rightMargin=20*mm
)

story = []

# ── Title page content ───────────────────────────────────────────────────────
story.append(Spacer(1, 8*mm))
story.append(Paragraph("Blueprint \u2014 Multi Dynamic \u00d7 Inspra AI", s_title))
story.append(Paragraph("Companion Guide to the System Integration Blueprint", s_subtitle))

# Overview
story.append(Paragraph("Overview", s_h1))
story.append(Paragraph(
    "Multi Dynamic is a franchise real estate business operating seven offices across "
    "New South Wales, with its head office coordinating operations centrally. The Oran Park "
    "office, established approximately five months ago, is the pilot location for integrating "
    "Inspra AI's outbound calling solution.",
    s_body))
story.append(Paragraph(
    "The core challenge is lead generation and data hygiene. Multi Dynamic holds approximately "
    "32,000 contacts across multiple sources (RP Data, ID for Me, mobile contacts, and Vault-RE CRM), "
    "but a significant portion of this data is outdated, duplicated, or unverified. Manual cold calling "
    "is time-consuming, demoralising for junior agents, and produces inconsistent results.",
    s_body))
story.append(Paragraph(
    "Inspra AI will deploy an outbound AI agent to systematically call, verify, and qualify all "
    "contacts, clean the database down to approximately 8,000 to 10,000 valid records, categorise leads by "
    "urgency (Hot, Warm, Cold, Unassessed), and book appraisal appointments directly into the calendar. "
    "This frees experienced agents like Megha and Tirtha to focus on high-value, dollar-productive "
    "activities: presenting to qualified prospects and closing listings.",
    s_body))

story.append(Spacer(1, 4*mm))

# How to Read the Diagram
story.append(section_block("How to Read the Diagram", [
    bullet("<b>Row A (Current State)</b> shows Multi Dynamic's existing systems before Inspra AI integration: "
           "data sources (RP Data, ID for Me, mobile contacts), the Vault-RE CRM, and Google Calendar."),
    bullet("<b>Row B (Proposed Phase 1)</b> shows the Inspra AI integration layer: data import and deduplication, "
           "AI outbound calling agent, disposition tagging, CRM updates, appointment booking, and notifications."),
    bullet("<b>Row C (Future / Phase 2+)</b> shows planned future capabilities: inbound AI agent, "
           "website lead capture, and rollout to remaining franchise offices."),
    bullet("<b>Colour coding:</b> Blue = existing systems, Purple = central hub (Vault-RE), "
           "Green = Inspra AI systems, Orange = future/TBC, Grey = neutral endpoints."),
    bullet("<b>Orange badges (numbered)</b> indicate open questions that need resolution. "
           "Each badge number corresponds to the numbered list at the bottom of the diagram."),
]))

story.append(Spacer(1, 4*mm))

# Detail per system — Phase 1
story += section_flow("Phase 1 Systems in Detail", [
    Paragraph("<b>Data Import and Deduplication</b>", s_h2),
    Paragraph(
        "<b>Impact: Reduces ~32,000 contacts to ~8,000\u201310,000 clean, verified records.</b>",
        s_body_bold),
    Paragraph(
        "All data sources (RP Data with ~12,000\u201313,000 property records for six core suburbs, "
        "ID for Me with a similar volume at ~30\u201340% overlap, mobile contacts from Megha and Tirtha "
        "totalling ~12,000+, and existing Vault-RE records of ~3,000) are consolidated. Duplicates are "
        "removed and records are standardised with minimum fields: full name, address, mobile, and email.",
        s_body),

    Paragraph("<b>AI Outbound Agent</b>", s_h2),
    Paragraph(
        "<b>Impact: Eliminates manual cold calling burden from junior agents.</b>",
        s_body_bold),
    Paragraph(
        "The AI agent systematically calls every contact in the cleaned database. It verifies whether "
        "the number is valid and connected, qualifies the contact's intent (buying or selling within "
        "12 months), and handles common objections naturally. If the contact is not interested, the agent "
        "asks for referrals to family or friends. Calling hours are 8:30 AM to 7:30 PM. No live transfers "
        "are performed; instead, a callback is scheduled and the team is notified.",
        s_body),

    Paragraph("<b>Disposition Tagging</b>", s_h2),
    Paragraph(
        "<b>Impact: Every contact is categorised for appropriate follow-up cadence.</b>",
        s_body_bold),
    Paragraph(
        "Post-call, each contact is automatically tagged: Hot (planning to act within 3 months, follow up "
        "immediately), Warm (6\u201312 months, follow up fortnightly), Cold (beyond 12 months, follow up "
        "every second month), or Unassessed (no decision yet). Invalid, disconnected, or deceased records "
        "are flagged for removal. This ensures no wasted effort on dead data.",
        s_body),

    Paragraph("<b>Vault-RE CRM (Updated)</b>", s_h2),
    Paragraph(
        "<b>Impact: CRM becomes the single source of truth with enriched contact records.</b>",
        s_body_bold),
    Paragraph(
        "Call transcripts, summaries, disposition tags, and lead categories are pushed back into Vault-RE "
        "automatically. Agents can review conversation history before callbacks. The system serves all "
        "seven offices centrally, with the Oran Park office as the pilot.",
        s_body),

    Paragraph("<b>Appointment Booking</b>", s_h2),
    Paragraph(
        "<b>Impact: Qualified appointments booked directly into agent calendars.</b>",
        s_body_bold),
    Paragraph(
        "When a contact expresses interest, the AI agent offers two time options at each step (this week "
        "or next week, then specific days, then morning or afternoon) and books the appointment. The booking "
        "syncs with Google Calendar and Vault-RE to prevent double-booking. Both the lead agent (Megha or "
        "Tirtha) and the relevant assistant agent are notified based on suburb coverage.",
        s_body),

    Paragraph("<b>Email and SMS Notifications</b>", s_h2),
    Paragraph(
        "<b>Impact: Ensures no qualified lead falls through the cracks.</b>",
        s_body_bold),
    Paragraph(
        "Callback requests trigger email notifications to the assigned agent. Unreachable but valid numbers "
        "receive SMS follow-ups. Post-appointment booking, the contact receives a confirmation message with "
        "meeting details and any preparation documents.",
        s_body),
])

story.append(PageBreak())

# Summary table
story.append(Paragraph("System Summary", s_h1))
story.append(Spacer(1, 2*mm))

table_data = [
    ["System", "Category", "Phase", "Impact"],
    ["Data Import & Dedup", "Inspra AI", "Phase 1",
     "Consolidate ~32K contacts to ~8\u201310K clean records"],
    ["AI Outbound Agent", "Inspra AI", "Phase 1",
     "Automated calling, verification, and qualification"],
    ["Disposition Tagging", "Inspra AI", "Phase 1",
     "Categorise leads: Hot / Warm / Cold / Unassessed"],
    ["Vault-RE CRM", "Central Hub", "Existing + Phase 1",
     "Single source of truth, enriched with AI call data"],
    ["Appointment Booking", "Inspra AI", "Phase 1",
     "Direct calendar booking with dual-agent notification"],
    ["Email / SMS", "Neutral", "Phase 1",
     "Callback alerts and follow-up messaging"],
    ["AI Inbound Agent", "Future", "Phase 2+",
     "Handle incoming calls automatically"],
    ["Website Lead Capture", "Future", "Phase 2+",
     "Funnel web inquiries into the pipeline"],
    ["Multi-Office Rollout", "Future", "Phase 2+",
     "Replicate to remaining 6 franchise offices"],
]

col_widths = [90, 65, 70, 200]
story.append(KeepTogether([make_table(table_data, col_widths)]))

story.append(Spacer(1, 6*mm))

# Phased rollout
story.append(Paragraph("Phased Rollout", s_h1))
story.append(Spacer(1, 2*mm))

phase_data = [
    ["Phase", "Timeline", "Deliverables"],
    ["Phase 1a: Setup",
     "Weeks 1\u20132",
     "IT session with Vault-RE team to confirm API capabilities. "
     "Data import, deduplication, and cleaning. Calendar sync validation."],
    ["Phase 1b: Prototype",
     "Weeks 2\u20133",
     "AI agent demo with call flow, objection handling, and appointment booking. "
     "Test phone number provided for internal testing."],
    ["Phase 1c: Soft Launch",
     "Weeks 3\u20134",
     "AI agent begins calling Oran Park leads. Weekly review meetings to "
     "listen to recordings and refine the agent."],
    ["Phase 1d: Full Launch",
     "Weeks 5\u20138",
     "Full-scale outbound calling across all cleaned data. "
     "Dashboard access for call monitoring and reporting."],
    ["Phase 2+: Expansion",
     "TBD",
     "Inbound AI agent, website lead capture, rollout to remaining offices. "
     "Scope and timeline to be determined after Phase 1 results."],
]

phase_widths = [90, 70, 265]
story.append(KeepTogether([make_table(phase_data, phase_widths)]))

story.append(Spacer(1, 6*mm))

# Open Questions
story.append(section_block("Open Questions", [
    bullet("<b>Q1:</b> Mobile contacts import method. Megha and Tirtha need to export contacts "
           "from their mobile phones as CSV and bulk-upload into Vault-RE."),
    bullet("<b>Q2:</b> Vault-RE API capabilities and limitations. A dedicated IT session with "
           "the Vault-RE team is required to confirm integration feasibility."),
    bullet("<b>Q3:</b> Google Calendar and Vault-RE calendar sync. Must ensure no overlapping "
           "appointments when the AI agent books meetings."),
    bullet("<b>Q4:</b> Website inquiry integration. Scope and timeline to be defined in Phase 2."),
    bullet("<b>Q5:</b> Objection handling document. Megha to provide common objections and "
           "preferred responses for the AI agent script."),
    bullet("<b>Q6:</b> Agent assignment routing. Appointments must route to the correct agent "
           "(Megha, Tirtha, or their assistants) based on suburb coverage area."),
]))

story.append(Spacer(1, 6*mm))

# Next Steps
story.append(section_block("Next Steps", [
    bullet("Schedule IT session with Vault-RE team to confirm API capabilities (early next week)."),
    bullet("Megha to export mobile contacts to CSV and provide objection handling document."),
    bullet("Inspra AI to deliver the blueprint diagram (this document) and system flowchart for review."),
    bullet("Inspra AI to build a prototype AI agent demo for Multi Dynamic Oran Park testing."),
    bullet("Confirm recurring weekly meeting slot for ongoing review and optimisation."),
]))

# ── Build ─────────────────────────────────────────────────────────────────────
doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
print("SAVED_WRITEUP:", out_path)
