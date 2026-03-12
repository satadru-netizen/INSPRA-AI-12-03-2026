---
name: agent-ops-blueprint
description: "Generate a project blueprint for Inspra AI voice agent delivery. Accepts a discovery call transcript, meeting notes, or step-by-step brief and produces a structured blueprint document with phase breakdown. Use whenever the user wants to create a project blueprint, scope a new voice agent project, document discovery findings, or start a new client engagement. Also use when the user provides a transcript and says 'create a blueprint' or 'scope this project'."
---

# Agent Ops — Blueprint Generator

Generate a structured project blueprint from a discovery call transcript or project brief. Output a clean, phase-based document and a Figma flowchart.

## Input Formats

Accept any of these:
- Discovery call transcript (raw text)
- Step-by-step project notes
- Bullet-point brief with client requirements

## Extraction Process

From the input, extract and organize:

### Discovery
- **Client**: Company name, contacts, industry
- **Pain Points**: What's broken today (list each clearly)
- **Goals**: What success looks like for this project

### Phase Planning

Evaluate which phases apply based on the project scope. Core phases (1-6) are almost always included. Phases 7-8 are conditional.

Read `references/template-structure.md` for the full phase template with sub-tasks.

For each applicable phase, document:
- Phase name and objective
- Specific sub-tasks (pulled from template, customized to this client)
- Tools/platforms involved
- Dependencies on prior phases

## Output: Blueprint Document

```markdown
# [Client Name] — AI [Agent Type] Agent Blueprint
**Prepared by**: Inspra AI
**Date**: [Date]
**Agent Type**: Inbound / Outbound / Both

---

## Discovery Summary
### Pain Points
- [extracted from input]

### Project Goals
- [extracted from input]

---

## Phase 1: Requirements & Knowledge Base
**Objective**: [one line]
- [ ] [sub-task 1]
- [ ] [sub-task 2]
...

## Phase 2: Data & List Building
...

[Continue for each applicable phase]

---

## Timeline & Dependencies
[Phase dependency chain]

## Out of Scope
[Anything explicitly excluded]

## Next Steps
[Immediate action items]
```

## Output: Figma Flowchart

After generating the blueprint document, create a visual flowchart in FigJam using the FigJam MCP server.

### Primary Method — FigJam MCP `generate_diagram`

Call the `generate_diagram` tool from the FigJam MCP server. This tool accepts a structured diagram description and creates the flowchart directly in FigJam — no manual design work needed.

**How to structure the diagram description passed to `generate_diagram`:**

Build a clear, structured description that includes:

1. **Nodes** — List every node with its label, shape, and color:
   - **Oval (green)**: Start node ("Project Start") and end node ("Ongoing Support")
   - **Rectangle (red/pink)**: Discovery phase items (pain points, client context)
   - **Rectangle (blue)**: Goals and standard phase items (Phases 1-6)
   - **Rectangle (orange)**: Development/build items (system prompt, integrations, testing)
   - **Rectangle (purple)**: Future scope items (chatbot, expansion phases)
   - **Diamond (yellow)**: Decision gates (e.g., "Client Approval?", "QA Passed?")

2. **Connections** — Define the flow between nodes:
   - Phase-to-phase sequential flow (top to bottom or left to right)
   - Decision diamonds branch into Yes/No paths
   - Sub-tasks branch off their parent phase node

3. **Layout** — Describe the visual structure:
   - Each phase as a vertical section with sub-tasks branching from it
   - Decision gates between phases where client approval is required
   - Color coding consistent with the style guide above

**Example description format for `generate_diagram`:**
```
Create a project blueprint flowchart with the following structure:
- Start with a green oval node "Project Start"
- Connect to a red rectangle "Discovery: [Client Pain Points]"
- Branch into blue rectangles for each goal
- Flow through phases sequentially: Phase 1 (blue) -> Decision Gate (yellow diamond "Client Approval?") -> Phase 2 (blue) -> ...
- Each phase has sub-task rectangles branching off (colored per phase type)
- Orange rectangles for build/dev tasks in Phase 3-4
- End with green oval "Ongoing Support"
[Include all specific phases, sub-tasks, and decision points from the blueprint]
```

### Fallback ONLY — Mermaid Diagram

Use Mermaid as a fallback **only** if:
- The `generate_diagram` tool returns an error, OR
- The FigJam MCP server is explicitly unavailable or not connected

Never default to Mermaid. Always attempt `generate_diagram` first.

## Quality Checks

Before finalizing:
- Every pain point from discovery maps to at least one goal
- Every goal maps to at least one phase
- No orphan phases (each has clear sub-tasks)
- Out-of-scope items are explicitly called out
- Next steps have owners assigned
