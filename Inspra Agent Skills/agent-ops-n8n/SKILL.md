---
name: agent-ops-n8n
description: "Build n8n automation workflows for Inspra AI voice agent projects. Handles webhook integrations, post-call processing, CRM syncing, notification pipelines, and any backend automation the voice agent needs. Use whenever the user mentions n8n workflows, backend automation, webhook setup, post-call actions, CRM sync, transcript processing, or needs to connect a voice agent to external systems. Also triggers on 'automate this', 'create a workflow for', 'connect Vapi to', or 'process call data'. Always reads n8n docs via MCP before building."
---

# Agent Ops — n8n Integration Builder

Build backend automation workflows that power the voice agent's integrations. Every workflow follows: trigger → process → action → notify.

## Principle

Always read n8n documentation via MCP tools before building. Use these tools to verify node configurations, authentication methods, and current API patterns. Don't assume — check the docs.

### n8n Workflows MCP Tools
- `mcp__claude_ai_n8n_workflows__search_n8n_workflows_docs` — search n8n workflow documentation by keyword
- `mcp__claude_ai_n8n_workflows__fetch_n8n_workflows_documentation` — fetch full doc pages for specific n8n topics
- `mcp__claude_ai_n8n_workflows__search_n8n_workflows_code` — search for code examples and workflow snippets

### Context7 MCP Tools (additional doc sources)
- `mcp__claude_ai_n8n_context7__search_context7_documentation` — broader search across n8n and related library docs
- `mcp__claude_ai_n8n_context7__fetch_context7_documentation` — fetch detailed documentation from context7 sources

Start with the n8n workflows tools for node-specific lookups. Fall back to context7 tools for broader questions or when the workflows tools don't return enough detail.

## Input

- Blueprint (which integrations are needed)
- Agent tools (what the agent calls during conversation)
- External service credentials/details
- Trigger type (webhook, schedule, event)

## Common Workflow Patterns

### 1. Post-Call Processing
**Trigger**: Vapi end-of-call webhook
**Flow**:
```
Webhook (Vapi) → Extract transcript + metadata → Save to Google Sheets/Airtable
                                                → Update CRM record
                                                → Send summary to Slack/email
                                                → Tag call outcome (booked/no-show/callback)
```

### 2. Appointment Booking Sync
**Trigger**: Vapi tool call webhook (calendar_book)
**Flow**:
```
Webhook → Validate slot availability → Create calendar event
       → Send confirmation SMS/email to caller
       → Update CRM with appointment
       → Notify staff via Slack
```

### 3. Lead Capture & CRM Update
**Trigger**: Vapi tool call or end-of-call
**Flow**:
```
Webhook → Extract caller info → Check if exists in CRM
       → Create new lead OR update existing
       → Assign to sales rep
       → Trigger follow-up sequence (GHL/HubSpot)
```

### 4. Real-Time Agent Support
**Trigger**: Vapi function call (knowledge lookup)
**Flow**:
```
Webhook → Query vector DB / API → Format response → Return to Vapi
```
Must respond within 3 seconds — keep this pipeline fast.

### 5. Daily/Weekly Reports
**Trigger**: Cron schedule
**Flow**:
```
Schedule → Query call logs (Vapi API) → Aggregate metrics
         → Generate report → Send to client via email
         → Post summary to Slack
```

### 6. Escalation Pipeline
**Trigger**: Vapi transfer event or escalation tag
**Flow**:
```
Webhook → Capture conversation context → Create support ticket (Zendesk/Freshdesk)
       → Notify on-call team → Log escalation reason
```

## Build Process

1. **Research first** — use n8n MCP tools to look up node docs for every service involved
2. **Map the flow** — draw the workflow on paper: trigger → nodes → output
3. **Build incrementally** — start with trigger + first node, test, then add nodes one at a time
4. **Error handling** — add error branches for every external API call. If Google Sheets is down, the workflow shouldn't silently fail
5. **Test with sample data** — use Vapi's test webhook payload to validate the full pipeline
6. **Document** — write a brief description of what the workflow does, its trigger, and what services it touches

## Workflow Design Rules

- **One workflow per concern** — don't cram post-call processing, booking, and reporting into one workflow. Split them.
- **Idempotent where possible** — if the same webhook fires twice, the workflow shouldn't create duplicate records. Use upsert over insert.
- **Timeout awareness** — Vapi function call webhooks expect a response within 5 seconds. For real-time tool support, keep the chain fast. Move slow operations (email, CRM) to async branches.
- **Credential management** — never hardcode API keys in HTTP nodes. Use n8n's credential system.
- **Logging** — add a final node that logs success/failure to a sheet or monitoring tool for debugging.

## Output

For each workflow, produce:
- n8n workflow JSON (importable)
- Setup doc: what credentials to configure, what env vars to set
- Test instructions: how to trigger a test run and verify output
- Webhook URL(s) to configure in Vapi
