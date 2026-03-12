---
name: agent-ops-reports
description: "Generate performance reports and QA reports for Inspra AI voice agent projects. Analyzes call data, scores call quality, tracks KPIs, and produces client-ready reports. Use whenever the user mentions performance report, QA report, call audit, call scoring, client report, agent metrics, call analysis, or wants to review how the voice agent is performing post-launch. Also triggers on 'how is the agent doing', 'audit these calls', 'score these transcripts', or 'create a report for the client'."
---

# Agent Ops — Performance & QA Reports

Generate two types of reports for Inspra AI projects: **Performance Reports** (metrics & KPIs) and **QA Reports** (call quality audits). Both are client-facing and output as `.docx` files using `python-docx`.

## Input

- Call logs / transcripts (from Vapi, n8n exports, or manual)
- Report type: performance, QA, or both
- Reporting period (daily, weekly, monthly)
- Client-specific KPIs (if any beyond defaults)

## Document Generation

Both report types are generated as `.docx` files using the `python-docx` library. These are client-facing deliverables — professional appearance matters.

### Common Formatting Standards

- **Font**: Calibri or Arial, 11pt for body text
- **Heading 1**: 16pt bold (report title)
- **Heading 2**: 13pt bold (section headings)
- **Tables**: Use Word Table Grid style with header row shading (dark fill, white text)
- **Margins**: Standard 1-inch margins
- **Header/Footer**: Include "Prepared by Inspra AI" and page numbers
- **Spacing**: 1.15 line spacing for body, 6pt after paragraphs

### python-docx Usage

```python
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

doc = Document()

# Title
title = doc.add_heading('[Client] — Report Title', level=0)
title.runs[0].font.size = Pt(16)
title.runs[0].font.bold = True

# Section heading
doc.add_heading('Section Name', level=2)
heading_run = doc.paragraphs[-1].runs[0]
heading_run.font.size = Pt(13)
heading_run.font.bold = True

# Body text
para = doc.add_paragraph('Body text here.')
para.style.font.size = Pt(11)
para.style.font.name = 'Calibri'

# Table with header shading
table = doc.add_table(rows=1, cols=4)
table.style = 'Table Grid'
# Shade header row
for cell in table.rows[0].cells:
    cell.paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)
    from docx.oxml.ns import qn
    shading = cell._element.get_or_add_tcPr()
    shading_elm = OxmlElement('w:shd')
    shading_elm.set(qn('w:fill'), '2F5496')
    shading.append(shading_elm)
```

## Performance Report

### Metrics to Track

| Category | Metric | How to Calculate |
|----------|--------|-----------------|
| Volume | Total calls | Count of calls in period |
| Volume | Calls by type | Inbound vs outbound breakdown |
| Volume | Peak hours | Calls per hour heatmap |
| Conversion | Answer rate | Answered / total attempted |
| Conversion | Booking rate | Bookings / answered calls |
| Conversion | Goal completion | Calls achieving primary intent / total |
| Quality | Avg call duration | Mean duration in seconds |
| Quality | Avg sentiment | Positive / neutral / negative distribution |
| Quality | Transfer rate | Calls transferred to human / total |
| Quality | Drop-off point | Where in the flow callers hang up |
| Efficiency | First-call resolution | Issues resolved without callback / total |
| Efficiency | Avg response latency | Agent response time in ms |

### Content Structure Guide

Use the following as the content structure for the Performance Report `.docx`. This serves as a template — populate each section with actual data.

```markdown
# [Client Name] — Voice Agent Performance Report
**Prepared by**: Inspra AI
**Period**: [Start Date] — [End Date]
**Agent**: [Agent Name]

---

## Executive Summary
[3-4 sentences: overall performance, key wins, areas of concern]

## Key Metrics

| Metric | This Period | Previous Period | Change |
|--------|------------|-----------------|--------|
| Total Calls | X | X | +/-X% |
| Answer Rate | X% | X% | +/-X% |
| Booking Rate | X% | X% | +/-X% |
| Avg Duration | Xs | Xs | +/-Xs |
| Sentiment (Positive) | X% | X% | +/-X% |
| Transfer Rate | X% | X% | +/-X% |

## Call Volume Trends
[Daily/weekly breakdown, peak hours]

## Conversion Funnel
[Answered → Intent Identified → Goal Attempted → Goal Completed → Drop-off points]

## Top Issues
1. [Most common reason for failed calls]
2. [Second most common]
3. [Third]

## Recommendations
1. [Actionable improvement based on data]
2. ...

## Appendix
[Raw data tables if needed]
```

### .docx Generation — Performance Report

- **Filename**: `[Client]_PerformanceReport_[Period].docx` (e.g., `AcmeCorp_PerformanceReport_Feb2026.docx`)
- **Title**: 16pt bold, centered at top of document
- **Headings**: 13pt bold for all section headings (Executive Summary, Key Metrics, etc.)
- **Body text**: 11pt Calibri or Arial
- **Executive Summary**: Prominently placed at the top immediately after the report header block. Use a slightly larger font (12pt) or a bordered paragraph to make it stand out.
- **Metrics table**: Word table with Table Grid style
  - Header row shaded (dark blue fill, white text)
  - **Change column color-coding**: Use font color to indicate direction — green (`RGBColor(0, 128, 0)`) for positive changes, red (`RGBColor(255, 0, 0)`) for negative changes
  - Center-align numeric columns
- **Top Issues / Recommendations**: Numbered list paragraphs with proper indentation

## QA Report

### Scoring Rubric

Read `references/qa-rubric.md` for the full scoring criteria.

Audit a sample of calls (minimum 10 per period, or 10% of total, whichever is larger). Score each on:

| Dimension | Weight | What to Evaluate |
|-----------|--------|-----------------|
| Greeting & ID | 10% | Professional opening, identified self and company |
| Listening | 15% | Didn't interrupt, acknowledged caller, answered questions first |
| Accuracy | 20% | Correct information given, no hallucinations |
| Tone & Empathy | 15% | Warm, patient, matched caller's energy appropriately |
| Flow & Efficiency | 15% | Smooth progression, no loops or dead ends |
| Compliance | 10% | Stayed within boundaries, proper disclosures |
| Resolution | 15% | Achieved call objective or appropriate escalation |

**Score**: Each dimension 1-5. Weighted total out of 100.

### Content Structure Guide

Use the following as the content structure for the QA Report `.docx`. This serves as a template — populate each section with actual data.

```markdown
# [Client Name] — QA Audit Report
**Prepared by**: Inspra AI
**Period**: [Start Date] — [End Date]
**Calls Audited**: [X] of [Total]

---

## Summary Score: [X]/100

## Score Breakdown

| Dimension | Score | Notes |
|-----------|-------|-------|
| Greeting & ID | X/5 | |
| Listening | X/5 | |
| Accuracy | X/5 | |
| Tone & Empathy | X/5 | |
| Flow & Efficiency | X/5 | |
| Compliance | X/5 | |
| Resolution | X/5 | |

## Flagged Calls

### Call #[ID] — [Date, Time]
**Score**: [X]/100
**Issue**: [What went wrong]
**Transcript Excerpt**:
> Caller: [relevant line]
> Agent: [problematic response]
**Recommended Fix**: [Specific change to prompt/tool/flow]

[Repeat for each flagged call]

## Patterns & Trends
- [Recurring issue 1 across multiple calls]
- [Recurring issue 2]

## Prompt Improvement Suggestions
1. [Based on QA findings — specific change to system prompt]
2. ...

## Comparison to Previous Period
| Dimension | Previous | Current | Trend |
|-----------|----------|---------|-------|
| Overall | X/100 | X/100 | +/- |
...
```

### .docx Generation — QA Report

- **Filename**: `[Client]_QAReport_[Period].docx` (e.g., `AcmeCorp_QAReport_Feb2026.docx`)
- **Title**: 16pt bold, centered at top of document
- **Headings**: 13pt bold for all section headings
- **Body text**: 11pt Calibri or Arial
- **Summary Score**: Prominently displayed near the top — use a large font (18-20pt bold) or a highlighted/shaded paragraph so the overall score stands out immediately
- **Score Breakdown table**: Word table with Table Grid style, header row shaded (dark blue fill, white text)
- **Flagged Calls**: Each flagged call in its own subsection (Heading 3)
  - Transcript excerpts rendered in a bordered and lightly shaded text block (use paragraph shading with a light gray fill, e.g., `D9E2F3`, and a border around the paragraph)
  - Issue and Recommended Fix in bold labels followed by normal-weight text
- **Comparison table**: Same styling as Score Breakdown table

## Report Delivery

- Generate as `.docx` — this is the primary client-facing deliverable
- Include period-over-period comparison when prior data exists
- Flag any metric that moved more than 10% in either direction
- Always end with concrete, actionable recommendations — not vague "improve call quality"
