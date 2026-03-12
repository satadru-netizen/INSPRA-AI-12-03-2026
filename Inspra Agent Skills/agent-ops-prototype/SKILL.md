---
name: agent-ops-prototype
description: "Build prototype AI voice agents for Inspra AI projects using Vapi or Livekit. Takes a blueprint and call flowchart and produces a fully configured assistant with model, voice, transcriber, and system prompt. Use whenever the user wants to create a voice agent, build a prototype, configure a Vapi assistant, set up a Livekit agent, or mentions 'build the agent' or 'create the assistant'. Leverages existing create-assistant, create-workflow, and create-squad skills."
---

# Agent Ops — Prototype Agent Builder

Build a production-ready voice agent prototype from a blueprint and call flowchart. This skill orchestrates the existing Vapi/Livekit skills with Inspra AI's standards.

## Input

Required:
- Blueprint document (from `agent-ops-blueprint`)
- Call flowchart (from `agent-ops-flowchart`)

Optional:
- Client's existing scripts or FAQs
- Sample call recordings or transcripts
- Specific model/voice preferences

## Build Sequence

### Step 0: Confirm Platform & Direction (MANDATORY — STOP HERE UNTIL ANSWERED)

You MUST ask the user these two questions and WAIT for their response before doing anything else. Do not generate any files, system prompts, configs, or code until the user has explicitly replied.

Ask:
1. **Platform**: Vapi or Livekit?
2. **Direction**: Inbound, outbound, or both?

This is a hard stop — not a suggestion. The reason this exists: clients change their minds between the blueprint and the build phase. What the blueprint says and what the client actually wants today may differ. Even if the user's message explicitly states "Vapi inbound," ask them to confirm. Even in a test or demo context, ask. There are no exceptions.

If you find yourself thinking "the user already told me, I can skip this" — that is exactly the situation this rule exists for. Ask anyway. Your first response to the user must be the confirmation questions, not any built artifacts.

### 1. Agent Architecture Decision

Using the confirmed platform and direction from Step 0, determine:

| Question | Options |
|----------|---------|
| Single agent or squad? | Single if one role; squad if multiple handoffs (e.g., reception → booking → support) |
| Platform? | Use the answer confirmed in Step 0 |
| Inbound, outbound, or both? | Use the answer confirmed in Step 0 |

### 2. Model Selection

Read `references/model-guide.md` for current recommendations. Default stack:

- **LLM**: GPT-4o (balanced speed/quality) or Claude Sonnet (complex reasoning)
- **Voice**: Choose based on brand tone — professional, warm, energetic
- **Transcriber**: Deepgram Nova-2 (default) or custom if multilingual
- **Language**: Match client's market

### 3. System Prompt Development

Read `references/system-prompt-framework.md` for the mandatory framework. Every system prompt must follow this structure and include all default rules. The framework now uses a `[Guardrails] — DEFAULT` section (replacing the old `[Hard Compliance Rules]` and `[Boundaries]` sections). This Guardrails section contains 30+ non-negotiable rules that must be included in every system prompt — they are never removed or weakened. The framework is non-negotiable — it defines how Inspra AI agents behave.

Keep system prompts **under 800 words**. Concise instructions perform better than walls of text.

### 4. Configuration

Use the `create-assistant` skill to configure:
- Assistant name and metadata
- Model, voice, transcriber settings
- First message (greeting)
- End-of-call message
- Silence timeout, max duration
- Voicemail detection (outbound)
- Background sound (if applicable)

For squads, use `create-squad` to define:
- Member assistants and their roles
- Handoff conditions between members
- Shared context that transfers between agents

### 5. Phone Number Setup

For testing:
- Provision a Vapi test number OR
- Import client's Twilio/Vonage/Telnyx number

Use `create-phone-number` skill for configuration.

### 6. Demo Setup

Provide the client with:
- Test phone number to call/receive calls
- Web demo link (if applicable)
- Brief instructions on what to test

## Output Files

All client-facing documents must be generated as `.docx` files directly — not as `.md` files with a separate conversion script. Write a Python script using `python-docx` that generates the `.docx` in one step and execute it immediately. Do not save intermediate markdown files.

### System Prompt — `.docx`

Save as `[Client]_SystemPrompt_[AgentName].docx`. Generate directly using `python-docx`:
- Document title at the top
- Each framework section as **Heading 2**
- Prompt content in code-style blocks (monospace font, shaded background)

### Demo Instructions — `.docx`

Save as `[Client]_DemoInstructions_[AgentName].docx`. Generate directly using `python-docx`:
- Clean, client-friendly formatting
- Each test scenario includes: test number, what to test, and expected behavior

### Assistant JSON Config — `.json`

The Vapi or Livekit assistant configuration stays as a `.json` file (not converted to `.docx`).

## Output Checklist

Before marking prototype complete:
- [ ] System prompt follows the mandatory framework from `references/system-prompt-framework.md`
- [ ] System prompt reviewed and under 800 words
- [ ] System prompt saved as `.docx` file (`[Client]_SystemPrompt_[AgentName].docx`)
- [ ] First message sounds natural when read aloud
- [ ] All intents from flowchart are handled
- [ ] Fallback/escalation path works
- [ ] Tools connected and functional
- [ ] Test number provisioned
- [ ] Demo instructions saved as `.docx` file (`[Client]_DemoInstructions_[AgentName].docx`)
- [ ] Assistant JSON config saved as `.json`
