import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    KeepTogether, HRFlowable
)
from reportlab.lib.utils import ImageReader
from datetime import date

# ── Brand config ───────────────────────────────────────────────────────────────
AA_ORANGE    = colors.HexColor("#F47920")
AA_PURPLE    = colors.HexColor("#412F8F")
TEXT_DARK    = colors.HexColor("#1A1A1A")
TEXT_MED     = colors.HexColor("#444444")
TEXT_LIGHT   = colors.HexColor("#888888")
WHITE        = colors.white
BG_LIGHT     = colors.HexColor("#FFF8F3")
BG_PURPLE    = colors.HexColor("#F4F2FB")

LOGO_PATH    = os.path.expanduser("~/.claude/skills/brand-doc/assets/AA-logo-dark.png")
SAVE_PATH    = os.path.expanduser("~/Desktop/Diagram-Skill-Package/AA_DiagramSkill_TeamGuide.pdf")
W, H         = A4
TODAY        = date.today().strftime("%d %B %Y")

# ── Styles ─────────────────────────────────────────────────────────────────────
_ss = getSampleStyleSheet()

def sty(name, **kw):
    return ParagraphStyle(name, parent=_ss["Normal"], **kw)

s_title  = sty("s_title",  fontSize=22, textColor=TEXT_DARK,  fontName="Helvetica-Bold",
                leading=28, spaceAfter=2*mm)
s_sub    = sty("s_sub",    fontSize=11, textColor=AA_ORANGE,  fontName="Helvetica",
                leading=16, spaceAfter=6*mm)
s_h1     = sty("s_h1",     fontSize=13, textColor=AA_PURPLE,  fontName="Helvetica-Bold",
                leading=18, spaceBefore=2*mm, spaceAfter=1.5*mm)
s_h2     = sty("s_h2",     fontSize=10, textColor=AA_ORANGE,  fontName="Helvetica-Bold",
                leading=14, spaceBefore=1*mm, spaceAfter=1*mm)
s_body   = sty("s_body",   fontSize=9.5, textColor=TEXT_DARK, fontName="Helvetica",
                leading=14, spaceAfter=1.5*mm)
s_med    = sty("s_med",    fontSize=9.5, textColor=TEXT_MED,  fontName="Helvetica",
                leading=14, spaceAfter=1*mm)
s_bullet = sty("s_bullet", fontSize=9.5, textColor=TEXT_DARK, fontName="Helvetica",
                leading=15, leftIndent=10*mm, bulletIndent=3*mm, spaceAfter=1*mm)
s_code   = sty("s_code",   fontSize=9,   textColor=AA_PURPLE, fontName="Courier-Bold",
                leading=14, spaceAfter=1*mm, backColor=BG_PURPLE,
                leftIndent=4*mm, rightIndent=4*mm, borderPad=3*mm)
s_note   = sty("s_note",   fontSize=8.5, textColor=TEXT_MED,  fontName="Helvetica-Oblique",
                leading=13, leftIndent=6*mm, spaceAfter=2*mm)
s_footer = sty("s_footer", fontSize=7.5, textColor=TEXT_LIGHT, fontName="Helvetica",
                leading=10, alignment=TA_CENTER)

# ── Helpers ────────────────────────────────────────────────────────────────────
def sp(h=3):
    return Spacer(1, h * mm)

def rule():
    return HRFlowable(width="100%", thickness=0.5,
                      color=colors.HexColor("#DDDDDD"),
                      spaceAfter=2*mm, spaceBefore=1*mm)

def b(text):
    return Paragraph(f"• {text}", s_bullet)

s_cell_hdr  = sty("s_cell_hdr",  fontSize=9,   textColor=WHITE,     fontName="Helvetica-Bold", leading=13)
s_cell_body = sty("s_cell_body", fontSize=8.5, textColor=TEXT_DARK, fontName="Helvetica",      leading=13)

def tbl(data, widths=None):
    """Wraps every cell in a Paragraph so text word-wraps correctly."""
    wrapped = []
    for r_idx, row in enumerate(data):
        new_row = []
        for c_idx, cell in enumerate(row):
            if isinstance(cell, str):
                style = s_cell_hdr if r_idx == 0 else s_cell_body
                new_row.append(Paragraph(cell, style))
            else:
                new_row.append(cell)
        wrapped.append(new_row)

    t = Table(wrapped, colWidths=widths or [80*mm, 90*mm], repeatRows=1, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND",     (0,0), (-1,0),  AA_ORANGE),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE, BG_LIGHT]),
        ("GRID",           (0,0), (-1,-1), 0.4, colors.HexColor("#DDDDDD")),
        ("TOPPADDING",     (0,0), (-1,-1), 5),
        ("BOTTOMPADDING",  (0,0), (-1,-1), 5),
        ("LEFTPADDING",    (0,0), (-1,-1), 5),
        ("RIGHTPADDING",   (0,0), (-1,-1), 5),
        ("VALIGN",         (0,0), (-1,-1), "TOP"),
    ]))
    return t

def section(heading, *items, h1=True):
    """Keeps heading with first content block. Remaining items flow freely."""
    style = s_h1 if h1 else s_h2
    head  = Paragraph(heading, style)
    items = list(items)
    if not items:
        return [head]
    # Anchor: heading + first item always stay together
    anchor = KeepTogether([head, sp(1), items[0]])
    return [anchor] + items[1:]

def subsection(heading, *items):
    """s_h2 heading kept with its first item."""
    return section(heading, *items, h1=False)

# ── Header / Footer ────────────────────────────────────────────────────────────
def on_page(c, doc):
    c.saveState()

    # Logo — measure height first
    LOGO_TOP = H - 5*mm
    try:
        img  = ImageReader(LOGO_PATH)
        iw, ih = img.getSize()
        lw   = 34*mm
        lh   = lw * ih / iw
        logo_bottom = LOGO_TOP - lh
        c.drawImage(LOGO_PATH, 20*mm, logo_bottom, width=lw, height=lh, mask="auto")
    except Exception:
        lh = 8*mm
        logo_bottom = LOGO_TOP - lh
        c.setFont("Helvetica-Bold", 9)
        c.setFillColor(AA_ORANGE)
        c.drawString(20*mm, logo_bottom + 1*mm, "Automate Accelerator")

    # Orange rule sits 2mm below logo — never overlapping
    rule_y = logo_bottom - 2*mm
    c.setStrokeColor(AA_ORANGE)
    c.setLineWidth(1.5)
    c.line(20*mm, rule_y, W - 20*mm, rule_y)

    # Footer rule
    c.setStrokeColor(AA_ORANGE)
    c.setLineWidth(1)
    c.line(20*mm, 14*mm, W - 20*mm, 14*mm)
    c.setFont("Helvetica", 7)
    c.setFillColor(TEXT_LIGHT)
    c.drawString(20*mm, 9*mm, "Automate Accelerator   |   https://automateaccelerator.com.au")
    c.drawRightString(W - 20*mm, 9*mm, f"Page {doc.page}  |  {TODAY}")
    c.restoreState()

# ══════════════════════════════════════════════════════════════════════════════
# STORY
# ══════════════════════════════════════════════════════════════════════════════
story = []

# ── Cover ──────────────────────────────────────────────────────────────────────
story += [
    sp(10),
    Paragraph("Diagram Skill", s_title),
    Paragraph("Team Setup and Usage Guide", s_sub),
    Paragraph(
        "This skill generates branded PDF deliverables from any meeting — client calls, "
        "internal sessions, integration scoping, campaign planning, or cross-department reviews. "
        "It adapts to any workflow, any team, and any type of work.",
        s_body),
    Paragraph(
        "<b>No technical background required. Anyone on the team can use this</b> — "
        "whether you are in sales, delivery, integration, content, or operations. "
        "It works on both Claude Code (desktop CLI) and Claude Cowork (the team workspace at claude.ai). "
        "Choose the platform you already have access to.",
        s_body),
    Paragraph(
        "Both Automate Accelerator and Inspra AI brands are built in. The skill detects "
        "which brand to apply based on the context you provide.",
        s_med),
    sp(4), rule(),
]

# ── What it produces ───────────────────────────────────────────────────────────
story += section(
    "What the Skill Produces",
    Paragraph(
        "Every time you invoke the skill, it generates two branded PDF files automatically. "
        "You always deliver both.",
        s_body),
    tbl([
        ["Output",             "Description"],
        ["Diagram PDF",
         "Landscape swim lane chart. Maps systems, integrations, data flows, or process "
         "steps across phases. Branded header, colour-coded legend, arrows, and open "
         "question badges."],
        ["Companion write-up PDF",
         "Portrait document. Written explanation of each system or step, phased rollout "
         "plan, investment summary, and next steps. Professional language ready to send "
         "directly to a client or stakeholder."],
    ], widths=[48*mm, 110*mm]),
    Paragraph("Files are named consistently and saved to the folder you specify:", s_med),
    Paragraph("AA_ClientName_Blueprint_v1_YYYYMMDD.pdf", s_code),
    Paragraph("AA_ClientName_Blueprint_Writeup_YYYYMMDD.pdf", s_code),
    Paragraph("(Replace AA_ with Inspra_ for Inspra AI projects.)", s_note),
    sp(2), rule(),
)

# ── One-time setup ─────────────────────────────────────────────────────────────
story += section(
    "One-Time Setup — Choose Your Platform",
    Paragraph(
        "This skill works on two platforms. Use whichever you already have access to. "
        "Setup is done once per person.",
        s_body),
)
story += subsection(
    "Platform A — Claude Cowork (recommended for most team members)",
    Paragraph(
        "No installation needed. Works in any browser. "
        "Claude Cowork is the team workspace inside claude.ai — log in and look for the Cowork tab.",
        s_body),
    b("Log in at claude.ai and navigate to the Cowork tab"),
    b("Go to Projects and open or create the shared Diagram Skill project"),
    b("If setting up for the first time: open Project Instructions and paste the full contents of SKILL.md"),
    b("Save — every team member with access to the project now has the skill active"),
    b("To use: start a new chat inside the project and type /diagram or any trigger phrase listed below"),
    Paragraph(
        "Claude Cowork Projects are shared across your team — one person sets it up, "
        "everyone uses it. Ask your admin to add the SKILL.md to the shared project instructions.",
        s_note),
    sp(1),
)
story += subsection(
    "Platform B — Claude Code (desktop CLI, for technical team members)",
    Paragraph(
        "Claude Code is a desktop application. Download it from your Anthropic account.",
        s_body),
    b("Install Claude Code from your Anthropic account"),
    b("Copy SKILL.md to: ~/.claude/skills/diagram/SKILL.md"),
    b("Copy the four logo files from assets/ to: ~/.claude/skills/brand-doc/assets/"),
    b("Type /diagram in Claude Code to invoke the skill"),
    Paragraph(
        "Required logo files: AA-logo-dark.png, AA-logo-white.png, "
        "Inspra-logo-dark.png, Inspra-logo-light.png.",
        s_note),
    sp(2), rule(),
)

# ── How to invoke ──────────────────────────────────────────────────────────────
story += section(
    "How to Invoke the Skill",
    Paragraph("Type any of the following in Claude Cowork or Claude Code. All phrases trigger the same skill.", s_body),
)
story += subsection(
    "Recommended — slash command",
    Paragraph("/diagram", s_code),
)
story += subsection(
    "Natural language phrases",
    tbl([
        ["Phrase",                      "When to use"],
        ["blueprint",                   "General system or integration map"],
        ["draw a blueprint",            "Same as above"],
        ["data flow",                   "How data moves between systems or platforms"],
        ["architecture diagram",        "Technical system overview"],
        ["system integration",          "How tools connect to each other"],
        ["lead flow",                   "Lead gen or outreach pipeline"],
        ["process flow",                "Any step-by-step business or team process"],
        ["pipeline map",                "Sales, marketing, or delivery pipeline"],
        ["swim lane diagram",           "Multi-phase or multi-team layout"],
        ["map the systems",             "Quick trigger phrase"],
        ["visualise the architecture",  "Technical or operational overview"],
        ["draw the flow",               "Any process or data flow"],
        ["diagram the integration",     "Connecting two or more platforms"],
    ], widths=[70*mm, 96*mm]),
    sp(2), rule(),
)

# ── Two ways to use ────────────────────────────────────────────────────────────
story += section("Two Ways to Use It",
    Paragraph("Choose based on what you have available after the meeting.", s_body),
)
story += subsection(
    "Option A — From your notes",
    Paragraph("Open Claude Cowork or Claude Code, type /diagram, and answer the questions:", s_body),
    b("Client or project name"),
    b("Which brand — Automate Accelerator or Inspra AI"),
    b("Current state: existing systems, tools, or steps"),
    b("Proposed: what you are building, integrating, or recommending"),
    b("Phases or future items (if applicable)"),
    b("Where to save the output files"),
    Paragraph("Claude generates both PDFs and reports the file paths.", s_med),
    sp(2),
)
story += subsection(
    "Option B — Paste a Fathom transcript (faster)",
    Paragraph(
        "In Claude Cowork or Claude Code, type /diagram then paste the full Fathom transcript into the same message. "
        "Claude reads the transcript and automatically extracts:",
        s_body),
    b("Client name and brand from context"),
    b("Current systems from tools and platforms mentioned"),
    b("Proposed integrations from solutions discussed"),
    b("Phases from any Phase 1 / Phase 2 or short-term / long-term language"),
    b("Open questions from unresolved items or action points"),
    Paragraph(
        "Claude confirms what it extracted and asks only for anything it could not determine. "
        "Both PDFs are then generated automatically.",
        s_med),
    Paragraph("Tip: the more detail in the transcript, the less Claude needs to ask.", s_note),
    sp(2), rule(),
)

# ── Use cases ──────────────────────────────────────────────────────────────────
story += section(
    "Use Cases — Any Team, Any Meeting",
    Paragraph(
        "This skill is not built for one department or one type of call. It is designed "
        "to adapt to any workflow, any team structure, and any type of work. If you have "
        "left a meeting and someone would benefit from seeing how things connect, "
        "this skill is the right tool.",
        s_body),
    Paragraph(
        "Below are illustrations across common scenarios. This is not an exhaustive list — "
        "if your situation involves systems, steps, people, or data moving between places, "
        "the skill can map it.",
        s_med),
    sp(1),
)
story += subsection(
    "Client-Facing",
    tbl([
        ["Situation",            "What to map"],
        ["Onboarding call",      "Client's current systems and what you are building for them"],
        ["Proposal or pre-sign", "The proposed solution so the client can see it before committing"],
        ["Strategy session",     "Recommended integrations, phased rollout, and expected outcomes"],
        ["Quarterly review",     "Progress to date and what is coming in the next phase"],
        ["Upsell conversation",  "Phase 2 additions or new integrations you are recommending"],
        ["Handover to delivery", "Full system map so nothing is lost between sales and delivery"],
    ], widths=[55*mm, 111*mm]),
    sp(2),
)
story += subsection(
    "System Integration",
    tbl([
        ["Situation",                    "What to map"],
        ["New integration scoping",      "Source systems, destination platforms, data flow between them"],
        ["API or webhook mapping",       "How data moves from one tool to another (e.g. CRM to dialler to reporting)"],
        ["Troubleshooting a broken flow","Current architecture to identify where the failure sits"],
        ["Documenting a completed build","Final state of the integration for client records and internal reference"],
        ["Before vs after comparison",   "Current state row vs proposed row to show exactly what changes"],
    ], widths=[55*mm, 111*mm]),
    sp(2),
)
story += subsection(
    "Content and Marketing",
    tbl([
        ["Situation",           "What to map"],
        ["Content pipeline",    "From brief creation through to publishing and distribution"],
        ["Lead gen workflow",   "Outreach sequence, platform touchpoints, and handoff to sales"],
        ["Campaign flow",       "Ad platform to landing page to CRM to follow-up sequence"],
        ["Multi-channel strategy","How different channels connect and feed each other"],
        ["Reporting structure", "Where data comes from and how it reaches the client dashboard"],
    ], widths=[55*mm, 111*mm]),
    sp(2),
)
story += subsection(
    "Voice AI (Inspra AI)",
    tbl([
        ["Situation",                  "What to map"],
        ["Voice agent architecture",   "Telephony platform, AI agent, CRM, and escalation path"],
        ["Call routing logic",         "How inbound calls are triaged and routed to the right outcome"],
        ["Client stack integration",   "How the voice agent connects to the client's existing tools"],
        ["Post-call data flow",        "What happens to call data, transcripts, and outcomes after the call"],
    ], widths=[55*mm, 111*mm]),
    sp(2),
)
story += subsection(
    "Internal and Cross-Department",
    tbl([
        ["Situation",                    "What to map"],
        ["Internal process design",      "Any recurring workflow that needs to be documented across teams"],
        ["New team member onboarding",   "How the business operates, which tools do what, who owns what"],
        ["SOP visualisation",            "Standard operating procedures shown as a clear flow"],
        ["New service planning",         "Map the delivery process before the service is launched"],
        ["Retrospective or post-mortem", "What the process looked like and where it broke down"],
        ["Cross-department alignment",   "How two or more teams interact around a shared process or client"],
    ], widths=[55*mm, 111*mm]),
    sp(1),
    Paragraph(
        "The skill is multi-departmental and multi-dynamic by design. It does not assume "
        "a fixed structure — it builds the diagram from whatever context you provide. "
        "The more specific your input, the more precise the output.",
        s_body),
    Paragraph(
        "Send client-facing PDFs within 24 hours of the call. "
        "For internal use, save to the relevant team or project folder.",
        s_note),
    sp(2), rule(),
)

# ── Performance note ───────────────────────────────────────────────────────────
story += section(
    "A Note on Performance",
    Paragraph(
        "Expanding the use cases does not affect the quality or output of the diagrams. "
        "The skill's rendering engine, brand logic, and validation loop are unchanged. "
        "The diagram always reflects exactly what you provide.",
        s_body),
    Paragraph(
        "Claude Code runs on a 200,000-token context window. For typical diagram sessions "
        "even with a full Fathom transcript, you will use well under 20 percent of "
        "available context. There is no degradation in output quality.",
        s_med),
    sp(2), rule(),
)

# ── Brand reference ────────────────────────────────────────────────────────────
story += section(
    "Brand Reference",
    tbl([
        ["Brand",                  "Colours",                           "When to use"],
        ["Automate Accelerator",   "Orange #F47920 + Purple #412F8F",   "AA client and internal projects"],
        ["Inspra AI",              "Green #39E100",                     "Inspra client and internal projects"],
    ], widths=[52*mm, 66*mm, 48*mm]),
    sp(2), rule(),
)

# ── FAQ ────────────────────────────────────────────────────────────────────────
story += section("Common Questions",
    tbl([
        ["Question", "Answer"],
        ["I do not have a logo file — where do I get it?",
         "Download from the shared team folder on Google Drive and place in "
         "~/.claude/skills/brand-doc/assets/ as described in setup."],
        ["Can I use this for a prospect before they sign?",
         "Yes. A diagram at proposal stage shows you understand the client's business "
         "and have already mapped a solution."],
        ["How long does it take?",
         "With a Fathom transcript: roughly 5 minutes. From manual notes: 10 to 15 minutes."],
        ["Where do the files get saved?",
         "You tell Claude where to save them when it asks. "
         "Default to your client's project folder on your Desktop."],
        ["What if I only have partial information?",
         "Claude will ask for anything it cannot determine. "
         "Mark items as TBD and they will appear as open questions in the diagram."],
        ["Can the diagram have more than three rows or phases?",
         "Yes. Tell Claude how many phases you need and it will adapt the layout."],
        ["Does using this for internal work affect quality?",
         "No. The skill renders identically regardless of subject matter."],
        ["How do I get updates to the skill?",
         "Claude Cowork: replace the SKILL.md content in your Project Instructions. "
         "Claude Code: replace the file at ~/.claude/skills/diagram/SKILL.md."],
    ], widths=[72*mm, 94*mm]),
    sp(1), rule(),
)

# ── Skill location ─────────────────────────────────────────────────────────────
story += section(
    "Where the Skill Lives — Updates",
    Paragraph(
        "<b>Claude Cowork:</b> The skill lives inside your Project Instructions on the Cowork tab. "
        "To update: open the project, paste the new SKILL.md content, and save. "
        "All team members with project access get the update instantly.",
        s_body),
    Paragraph(
        "<b>Claude Code:</b> The skill lives at "
        "<font face='Courier' color='#412F8F'>~/.claude/skills/diagram/SKILL.md</font>. "
        "Replace this file with the new version from the shared team folder. No other changes needed.",
        s_body),
)

# ── Build ──────────────────────────────────────────────────────────────────────
os.makedirs(os.path.dirname(SAVE_PATH), exist_ok=True)
doc = SimpleDocTemplate(
    SAVE_PATH, pagesize=A4,
    leftMargin=20*mm, rightMargin=20*mm,
    topMargin=24*mm, bottomMargin=22*mm,
    title="Diagram Skill — Team Guide",
    author="Automate Accelerator",
)
doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
print("SAVED:", SAVE_PATH)
