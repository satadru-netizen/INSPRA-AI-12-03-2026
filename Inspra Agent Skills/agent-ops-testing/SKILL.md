---
name: agent-ops-testing
description: "Generate and run comprehensive test scenarios for Inspra AI voice agents — both pre-live and post-live. Covers edge cases, patience checks, off-topic handling, stress tests, objection handling, interruption detection, and conversation quality. Use whenever the user wants to test a voice agent, QA an assistant, run test calls, create test scenarios, stress test an agent, or validate agent behavior before or after deployment. Also triggers on 'test the bot', 'QA the agent', 'run test cases', or 'check if the agent handles X'."
---

# Agent Ops — Voice Agent Testing

Generate and execute comprehensive test scenarios that push the voice agent to its limits. Testing happens in two phases: **pre-live** (before client deployment) and **post-live** (after deployment, ongoing).

## Input

- Agent configuration (system prompt, tools, flowchart)
- Test phase: pre-live or post-live
- Specific concerns (optional — e.g., "client worried about angry callers")

## Test Categories

Read `references/test-scenarios.md` for full scenario scripts per category.

### 1. Happy Path
Verify the agent handles standard calls correctly end-to-end. Every intent from the flowchart gets a clean run.

### 2. Patience Check
Caller is slow, confused, elderly, repeats themselves, takes long pauses, asks the same question multiple ways. Agent must remain calm, never rush, never show frustration.

**Fail signals**: Agent repeats itself robotically, cuts caller off, skips ahead without confirming understanding.

### 3. Off-Topic Handling
Caller goes on tangents — talks about weather, their day, unrelated complaints, personal stories. Agent should acknowledge politely, then gently steer back.

**Fail signals**: Agent ignores the tangent completely (feels robotic), or follows the tangent and never returns to the task.

### 4. Stress Test
Angry caller, rapid-fire questions, raised voice, demands to speak to a human, threatens to leave a bad review. Agent stays calm, empathetic, and solution-focused.

**Fail signals**: Agent gets defensive, argues, matches the caller's tone, or gives up too quickly.

### 5. Objection Handling
Caller pushes back hard — "I don't want to book", "This sounds like a scam", "Why should I trust you?", "Your competitor is cheaper", "I already have someone for this". Agent addresses objections without being pushy.

**Fail signals**: Agent ignores the objection, gets pushy/salesy, or collapses and ends the call.

### 6. Answer-First Check
Caller asks a direct question. Agent must answer it BEFORE pivoting to its agenda. This is critical — nothing kills trust faster than dodging questions.

**Fail signals**: Agent deflects ("Great question! Let me first get your details..."), ignores the question, or gives a non-answer.

### 7. No-Interruption Check
Caller is mid-sentence. Agent must wait for the caller to finish before speaking. Test with long pauses mid-sentence and with filler words ("um", "so like", "let me think...").

**Fail signals**: Agent talks over the caller, responds to incomplete sentences, or fills silences too quickly.

### 8. Edge Cases
- Silence (caller says nothing for 10+ seconds)
- Background noise / poor audio
- Wrong number ("Is this Pizza Hut?")
- Multiple intents in one sentence
- Caller speaks a different language
- Caller asks agent if it's AI
- Caller gives contradictory information
- Caller wants to cancel mid-booking
- Repeat caller (already booked, calling again)

### 9. Compliance & Boundaries
- Agent never shares information it shouldn't (pricing it doesn't know, medical advice, legal guarantees)
- Agent doesn't make promises outside its authority
- Call recording disclosure (if required by jurisdiction)
- Data handling (doesn't read back sensitive info unnecessarily)

### 10. Tool Failure Simulation
- What happens when calendar API is down?
- CRM lookup returns no results?
- Transfer destination doesn't answer?
- Agent should have a graceful fallback for every tool failure.

## Test Execution

### Pre-Live Testing

1. Generate test scripts from each category above (read `references/test-scenarios.md`)
2. Customize scenarios to the specific agent's domain and flowchart
3. Run each scenario — either via test calls or conversation simulation
4. Score each on the rubric below
5. Document failures with exact transcript excerpts
6. Fix and retest until all categories pass

### Post-Live Testing

Same categories, but:
- Use real call transcripts to identify new edge cases
- Focus on patterns where the agent underperforms
- Run regression tests after any prompt or tool changes
- Monthly QA cycle minimum

## Scoring Rubric

Each test scores on 4 dimensions:

| Dimension | 1 (Fail) | 2 (Partial) | 3 (Pass) | 4 (Excellent) |
|-----------|----------|-------------|----------|----------------|
| **Accuracy** | Wrong info given | Mostly correct, minor errors | All info correct | Correct + adds helpful context |
| **Tone** | Robotic/rude/pushy | Functional but flat | Professional and warm | Natural, empathetic, human-like |
| **Flow** | Dead end or loop | Recovered but awkward | Smooth progression | Seamless, felt like a real conversation |
| **Rules** | Broke core rules (interrupted, dodged questions) | Minor rule bend | All rules followed | Rules followed naturally, not mechanically |

**Pass threshold**: No dimension below 2, average >= 3.

## Output

Generate the test report as a `.docx` file using `python-docx`.

**Filename**: `[AgentName]_TestReport_[Phase]_[Date].docx` (Phase = PreLive or PostLive, Date = YYYY-MM-DD)

### Document Formatting

- **Title**: Bold, 16pt — "Test Report — [Agent Name]"
- **Body font**: 11pt, Calibri or Arial
- **Summary section**: Prominently displayed with phase, date, tester, total tests run, and pass/partial/fail counts
- **Results by category**: Each category as a Heading 2, with a score table per scenario containing columns for Scenario, Accuracy, Tone, Flow, Rules, and Result
- **Score value colors**: Green font for pass (scores 3–4), yellow font for partial (score 2), red font for fail (score 1)
- **Priority fixes**: Numbered list with bold headers per item
- **Retest items**: Checkbox list using ballot box characters (☐)

### Content Structure (follows the markdown template below as a guide)

```markdown
# Test Report — [Agent Name]
**Phase**: Pre-Live / Post-Live
**Date**: [Date]
**Tester**: [Name]

## Summary
- Tests run: [X]
- Passed: [X] | Partial: [X] | Failed: [X]
- Critical issues: [list]

## Results by Category

### [Category Name]
**Scenario**: [Brief description]
**Score**: Accuracy: X | Tone: X | Flow: X | Rules: X
**Result**: Pass / Partial / Fail
**Notes**: [What happened, transcript excerpt if relevant]
**Fix Required**: [What needs to change]

[Repeat per scenario]

## Priority Fixes
1. [Most critical issue — what broke and how to fix]
2. ...

## Retest Items
- [ ] [Item to retest after fix]
```

The markdown template above defines the content structure — follow it when building the `.docx`. The Scoring Rubric and Test Categories sections above are reference material, not output content.
