---
name: agent-ops-tools
description: "Create and configure Vapi tools and function calls for Inspra AI voice agent projects. Handles tool definitions, API integrations, transfer call tools, end call tools, and external service connections. Use whenever the user needs to add tools to a voice agent, create function calls, set up calendar booking, CRM integration, call transfers, or any capability the agent needs to interact with external systems. Leverages the existing create-tool skill."
---

# Agent Ops — Tool & Function Call Creator

Design and build the tools a voice agent needs to do its job. Every tool the agent calls during a conversation is defined here.

## Input

- Blueprint (which integrations are needed)
- Call flowchart (which tools fire at which points)
- API documentation for external services (if custom)

## Common Tool Patterns

### 1. Calendar Booking
**When**: Agent needs to schedule appointments
**Type**: Function tool or API request
**Integrates with**: Google Calendar, Outlook, Cal.com, GHL
**Required params**: date, time, caller name, contact info, purpose
**Returns**: Confirmation with date/time/link

### 2. CRM Lookup / Update
**When**: Agent needs to check or store customer data
**Type**: API request tool
**Integrates with**: GHL, HubSpot, Salesforce, JobAdder
**Required params**: caller phone/email/name
**Returns**: Customer record or confirmation of update

### 3. Transfer Call
**When**: Agent needs to hand off to a human or another agent
**Type**: Transfer call tool
**Config**: Destination number/SIP, warm vs cold transfer, context message
**Important**: Always summarize the conversation before transferring

### 4. End Call
**When**: Conversation is complete or caller requests to hang up
**Type**: End call tool
**Config**: End message, post-call webhook trigger

### 5. Knowledge Base Query
**When**: Agent needs to look up information beyond its system prompt
**Type**: Function tool
**Integrates with**: Vector DB, FAQ API, document search
**Returns**: Relevant answer text

### 6. SMS / Email Notification
**When**: Send confirmation or follow-up after the call
**Type**: API request tool
**Integrates with**: Twilio SMS, GHL, SendGrid
**Required params**: recipient, message content

### 7. Custom API Integration
**When**: Project-specific logic (e.g., check appointment availability, verify insurance)
**Type**: API request tool
**Config**: Endpoint, method, headers, body template, response mapping

## Tool Design Rules

1. **Name tools clearly** — the LLM decides when to call them based on the name and description. `check_available_slots` is better than `api_call_1`.

2. **Write descriptions for the LLM** — the tool description tells the agent when to use it. Be explicit: "Use this tool when the caller wants to book an appointment and you have collected their name, preferred date, and preferred time."

3. **Minimize required parameters** — only require what's truly needed. Optional params for nice-to-haves. The fewer params, the less the agent has to collect before calling the tool.

4. **Handle failures gracefully** — every tool should have a fallback message the agent can say if the tool call fails. "I'm having trouble checking availability right now. Can I take your number and call you back?"

5. **Test tools independently** — before connecting to the agent, verify each tool works with sample data via the Vapi dashboard or API.

## Build Process

1. List all tools needed from the flowchart (every point where the agent interacts with an external system)
2. For each tool, define: name, description, type, parameters, expected response
3. Use the `create-tool` skill to build each one
4. Wire tools to the assistant configuration
5. Test each tool with sample inputs
6. Document tool behavior for the testing phase

## Output

For each tool, produce:
- Tool definition (JSON schema)
- Integration notes (what API/service, auth method)
- Sample request/response
- Failure fallback message
- Where in the call flow it fires
