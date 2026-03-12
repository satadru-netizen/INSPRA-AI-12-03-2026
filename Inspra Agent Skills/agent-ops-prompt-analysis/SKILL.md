---
name: agent-ops-prompt-analysis
description: "Analyze and optimize voice agent system prompts for Inspra AI projects. Compares system prompts against real call transcripts to find gaps, hallucination risks, tone issues, and missing edge cases. Use whenever the user wants to review a system prompt, optimize agent instructions, find gaps between prompt and real calls, fix agent behavior issues, or improve conversation quality. Also triggers on 'the agent keeps doing X wrong', 'review this prompt', 'why is the agent saying X', or 'improve the system prompt'."
---

# Agent Ops — System Prompt Analysis

Analyze voice agent system prompts against real call transcripts to find gaps and optimize performance. Every prompt change should be evidence-based — driven by what's actually happening in calls, not theory.

## Input

Required:
- Current system prompt

Recommended:
- Call transcripts (at least 5-10 for meaningful analysis)
- QA report (from `agent-ops-reports`) if available
- Known issues or complaints

## Analysis Framework

### 1. Transcript Gap Analysis

Compare what the prompt instructs vs what actually happens in calls.

For each transcript, check:
- **Handled correctly**: Caller request matched a prompt instruction and agent followed it
- **Handled but not in prompt**: Agent improvised correctly — should this be codified?
- **Mishandled**: Agent did the wrong thing — is the prompt unclear, missing, or contradictory?
- **Not encountered yet**: Prompt instructions that no caller has triggered — are they necessary?

Output a gap matrix:

```
| Scenario | In Prompt? | Occurred in Calls? | Handled Well? | Action |
|----------|-----------|-------------------|---------------|--------|
| Angry caller | Yes | 3 times | 2/3 correct | Clarify de-escalation steps |
| Insurance question | No | 5 times | Improvised OK | Add to prompt |
| Booking cancellation | Yes | 0 times | N/A | Keep (likely to occur) |
| Multilingual caller | No | 1 time | Failed | Add language policy |
```

### 2. Hallucination Audit

Search transcripts for moments where the agent stated information not grounded in:
- The system prompt
- A tool response
- The caller's own words

Common hallucination patterns:
- Inventing business hours, prices, or policies
- Making up staff names or availability
- Confirming things that weren't checked ("Yes, we have that available" without calling a tool)
- Overpromising ("I'll make sure that gets resolved today")

### 3. Tone Consistency Check

Across all transcripts, evaluate:
- Does the agent's tone match what the prompt describes?
- Is tone consistent across different caller types (friendly, angry, confused)?
- Does the agent adapt appropriately or stay monotone?
- Are there moments where tone breaks (suddenly formal after being casual)?

### 4. Rule Adherence Check

For each rule in the prompt, verify across transcripts:
- "Always answer questions first" — did it actually do this every time?
- "Never interrupt" — any instances of premature responses?
- "Don't provide medical/legal advice" — any boundary violations?
- "Transfer when X" — did transfers happen at the right moments?

### 5. Structural Analysis

Review the prompt itself for:
- **Clarity**: Would a fresh LLM understand every instruction unambiguously?
- **Conflicts**: Do any instructions contradict each other?
- **Length**: Is it under 800 words? Bloated prompts degrade performance.
- **Priority**: Are the most important rules prominent or buried?
- **Specificity**: Vague instructions ("be helpful") vs actionable ("if the caller asks about pricing, quote $X for initial consultation")

## Output

Generate the analysis as a **Word document (.docx)** using `python-docx`.

### File Naming
`[AgentName]_PromptAnalysis_[Date].docx`

### Formatting Rules
- **Title** ("System Prompt Analysis — [Agent Name]"): Bold, 16pt
- **Section headings** (Summary, Gap Analysis, etc.): Bold, 13pt
- **Body text**: 11pt, Calibri or Arial
- **Tables** (Gap Matrix, Hallucination Flags, Rule Violations): proper Word tables with the header row shaded (light grey background, bold white text)
- **Revised System Prompt section**: visually separated from the analysis — use a distinct style such as a slightly indented block with a left-border paragraph shading or a bordered text box so the revised prompt stands apart from commentary
- **Change Log**: numbered list (Word numbered-list style)

### Content Structure (follow this when building the .docx)

The markdown template below defines the sections and content to include. Use it as the structural guide — the actual output is the `.docx` file, not markdown.

```markdown
# System Prompt Analysis — [Agent Name]
**Date**: [Date]
**Transcripts Reviewed**: [X]

---

## Summary
[3-4 sentences: overall prompt health, biggest gaps, priority fixes]

## Gap Analysis
[Gap matrix table from above]

## Hallucination Flags
| Transcript | Timestamp/Line | What Agent Said | Grounded In | Risk Level |
|-----------|---------------|-----------------|-------------|------------|
| Call #X | Line Y | "We're open until 8pm" | Not in prompt | High |

## Tone Issues
[Specific moments where tone was off, with transcript excerpts]

## Rule Violations
| Rule | Violations Found | Example | Severity |
|------|-----------------|---------|----------|
| Answer first | 2 of 10 calls | Call #3: deflected pricing question | Medium |

## Structural Issues
[Conflicts, ambiguities, bloat, missing sections]

## Revised System Prompt

[Full rewritten prompt with changes highlighted using **bold** for additions and ~~strikethrough~~ for removals]

### Change Log
1. [What changed and why, backed by transcript evidence]
2. ...
```

## Revision Rules

When rewriting the prompt:
- Every change must cite a specific transcript or QA finding — no theoretical improvements
- Don't add instructions for scenarios that haven't occurred and aren't likely
- Remove instructions that add no value (agent already does it naturally)
- Keep under 800 words — if growing, consolidate or move details to tool descriptions
- Test the revised prompt against the same transcripts that revealed the issues
