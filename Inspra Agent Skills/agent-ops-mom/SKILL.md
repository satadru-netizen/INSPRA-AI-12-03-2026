---
name: agent-ops-mom
description: "Generate structured Minutes of Meeting (MoM) documents for Inspra AI projects. Accepts meeting transcripts, raw notes, or voice-to-text dumps and produces a clean, actionable MoM. Use whenever the user mentions meeting notes, MoM, meeting summary, action items from a call, or wants to document a client meeting. Triggers on phrases like 'summarize this meeting', 'create MoM', 'meeting notes', or 'what were the action items'."
---

# Agent Ops — Minutes of Meeting (MoM)

Transform meeting transcripts or raw notes into structured, actionable MoM documents for Inspra AI projects.

## Input

Accept any of:
- Full meeting transcript (auto-generated or manual)
- Raw bullet-point notes
- Voice-to-text dump
- Partial notes with context ("we discussed X, Y, Z with the client")

## Extraction Rules

1. **Attendees**: Extract all names mentioned. If roles/companies are stated, include them.
2. **Duration**: Calculate from timestamps if available, otherwise note "~X minutes" if mentioned.
3. **Executive Summary**: 3-5 sentences max. What was this meeting about and what was decided.
4. **Key Decisions**: Only firm decisions — not discussions or opinions. Each decision is a single clear statement.
5. **Action Items**: Each gets its own line with:
   - What needs to be done (specific, not vague)
   - Who owns it (by name)
   - Deadline (if mentioned, otherwise "TBD")
6. **Open Questions**: Anything raised but not resolved.
7. **Follow-up**: Next meeting details, prep needed, agenda items.

## Content Structure Template

The following markdown template defines the sections and structure to follow when building the MoM document:

```markdown
# Inspra AI x [Client/Company] — [Meeting Type]

**Date**: [Date] | **Duration**: ~[X] minutes
**Attendees**: [Name 1 (Role/Company)], [Name 2], ...

---

## Executive Summary

[3-5 sentence summary of the meeting's purpose and outcomes]

---

## Key Decisions

1. [Decision 1]
2. [Decision 2]
...

---

## Action Items

| # | Action | Owner | Deadline |
|---|--------|-------|----------|
| 1 | [Specific task] | [Name] | [Date/TBD] |
| 2 | [Specific task] | [Name] | [Date/TBD] |
...

---

## Open Questions

1. [Unresolved question 1]
2. [Unresolved question 2]
...

---

## Follow-up

- **Next Meeting**: [Date, time]
- **Attendees for Next**: [Any additions/changes]
- **Agenda**:
  - [Item 1]
  - [Item 2]
  ...
- **Prep Required**: [What needs to happen before next meeting]
```

## Document Generation

Generate the MoM as a **`.docx` file** using the `python-docx` library. Do not output raw markdown — the template above is the content structure guide only.

### File Naming

Save to the project workspace with the naming convention:
```
[Client]_MoM_[Date].docx
```
Example: `AcmeCorp_MoM_2026-03-10.docx`

### Formatting Rules

- **Title**: Bold, 16pt — use the header format `Inspra AI x [Client]`
- **Section headings**: Bold, 13pt
- **Body text**: 11pt, Calibri or Arial font
- **Action items table**: Proper Word table with borders; header row shaded (light grey)
- **`python-docx` styles to use**: `Heading 1`, `Heading 2`, `Normal`, `Table Grid`

### Build Process

1. Parse the input (transcript / notes) using the Extraction Rules above.
2. Structure the content following the Content Structure Template above.
3. Generate the `.docx` file using `python-docx`, applying the formatting rules.
4. Save the file to the project workspace.

## Quality Rules

- Action items are **specific and assignable** — "Discuss integration" is not an action item; "Tarique to share Google Drive link for asset uploads by Friday" is.
- Never invent information not present in the input. If something is ambiguous, put it in Open Questions.
- Keep Executive Summary tight — a busy stakeholder should get the full picture in 30 seconds.
- If the transcript mentions someone should attend the next meeting, capture that in Follow-up.
- Separate decisions from discussions — only confirmed agreements go in Key Decisions.
