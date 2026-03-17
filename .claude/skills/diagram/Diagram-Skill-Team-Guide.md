# Diagram Skill — Team Setup & Usage Guide

**For:** Automate Accelerator & Inspra AI teams
**Tool:** Claude Code (desktop CLI)
**Skill:** `/diagram`

---

## What This Skill Does

Generates two branded PDF deliverables from a client call:

1. **Diagram PDF** — a landscape swim lane chart mapping the client's current systems, proposed integrations, and future phases, in your brand colours
2. **Companion write-up PDF** — a written report explaining each system, phased rollout plan, investment summary, and next steps

Both files are produced automatically every time. You always deliver both to the client.

Both brands are built in — Automate Accelerator and Inspra AI. The skill detects which brand to use based on what you tell it.

---

## One-Time Setup

### Step 1 — Install Claude Code

Download and install Claude Code from your Anthropic account. You need an active Anthropic subscription.

### Step 2 — Copy the skill file

Place the skill file at this exact path on your machine:

```
~/.claude/skills/diagram/SKILL.md
```

If the `diagram` folder does not exist, create it.

### Step 3 — Copy the brand logo assets

Place the logo files at this exact path:

```
~/.claude/skills/brand-doc/assets/
```

Required files:
- `Inspra-logo-dark.png`
- `Inspra-logo-light.png`
- `AA-logo-dark.png`
- `AA-logo-white.png`

If the `brand-doc/assets` folder does not exist, create it.

> Both the skill file and logo assets are in the shared team folder on Google Drive.

---

## How to Invoke the Skill

Type any of the following in Claude Code to trigger the diagram skill:

### Slash command (recommended)
```
/diagram
```

### Natural language phrases — all of these work
| Phrase | When to use |
|---|---|
| `blueprint` | General system or integration map |
| `draw a blueprint` | Same as above |
| `data flow` | Showing how data moves between systems |
| `architecture diagram` | Technical system overview |
| `system integration` | Mapping how tools connect |
| `lead flow` | Lead gen or outreach pipeline |
| `process flow` | Any step-by-step business process |
| `pipeline map` | Sales or marketing pipeline |
| `swim lane diagram` | Multi-phase or multi-team layout |
| `map the systems` | Quick trigger phrase |
| `visualise the architecture` | Same as architecture diagram |
| `draw the flow` | Any process or data flow |
| `diagram the integration` | Connecting two or more platforms |

**All of the above trigger the same skill.** Use whichever phrase is natural in context.

---

## Two Ways to Use It After a Client Call

### Option A — Manual input (from your notes)

1. Open Claude Code
2. Type `/diagram`
3. Claude will ask questions. Answer from your call notes:
   - Client name
   - Which brand (AA or Inspra)
   - Their existing systems and tools
   - What you are proposing to build or integrate
   - Any phased rollout or future items
   - Where to save the files
4. Claude generates both PDFs and reports the file paths

### Option B — Paste a Fathom transcript (faster)

1. Open Claude Code
2. Type `/diagram` then paste the full Fathom transcript into the same message
3. Claude reads the transcript and automatically extracts:
   - Client name and brand from context
   - Current systems from tools and platforms mentioned
   - Proposed integrations from solutions discussed
   - Phases from any "Phase 1 / Phase 2" or "short-term / long-term" language
   - Open questions from unresolved items or action points
4. Claude summarises what it extracted and asks only for anything it could not determine
5. Both PDFs are generated automatically

> **Tip:** Fathom transcripts work best when the call covered what systems the client currently uses and what you are recommending. The more detail in the transcript, the less Claude will need to ask.

---

## What the Two Output Files Look Like

### Diagram PDF
- Landscape, branded with your logo and brand colours
- Swim lane rows (e.g. Current State, Phase 1, Phase 2)
- Colour-coded system boxes with a legend
- Arrows showing data or process flow
- Question badges on any open items
- Client name and date in the header

### Companion write-up PDF
- Portrait document, same brand styling
- Sections: overview, how to read the diagram, detail per system, phased rollout, investment summary, next steps
- Written in plain professional language for the client
- Saved to the same folder as the diagram

Both files are named consistently:
- Diagram: `AA_ClientName_Blueprint_v1_YYYYMMDD.pdf`
- Write-up: `AA_ClientName_Blueprint_Writeup_YYYYMMDD.pdf`

(Replace `AA_` with `Inspra_` for Inspra projects.)

---

## When to Use It

This skill is not limited to client-facing work. Any time you need to visualise a system, process, or workflow — for a client, a team, or internally — this is the right tool.

### Client-facing use cases

| Situation | What to map |
|---|---|
| Onboarding call | Client's current systems and what you are building for them |
| Proposal / pre-sign | The proposed solution so the client can see it before committing |
| Strategy session | Recommended integrations, phased rollout, and expected outcomes |
| Quarterly review | Progress to date and what is coming in the next phase |
| Upsell conversation | Phase 2 additions or new integrations you are recommending |
| Handover to delivery team | Full system map so nothing is lost in translation |

### System integration team

| Situation | What to map |
|---|---|
| New integration scoping | Source systems, destination platforms, data flow between them |
| API or webhook mapping | How data moves from one tool to another (e.g. CRM → dialler → reporting) |
| Troubleshooting a broken flow | Visual of the current architecture to identify where the failure sits |
| Documenting a completed build | Final state of the integration for client records and internal reference |
| Comparing before vs after | Current state row vs proposed row to show what changes |

### Content and marketing team

| Situation | What to map |
|---|---|
| Content pipeline | From brief creation through to publishing and distribution |
| Lead gen workflow | Outreach sequence, platform touchpoints, and handoff to sales |
| Campaign flow | Ad platform → landing page → CRM → follow-up sequence |
| Multi-channel strategy | How different channels connect and feed each other |
| Reporting structure | Where data comes from and how it reaches the client dashboard |

### Voice AI team (Inspra)

| Situation | What to map |
|---|---|
| Voice agent architecture | Telephony platform → AI agent → CRM → escalation path |
| Call routing logic | How inbound calls are triaged and routed |
| Integration with client systems | How the voice agent connects to the client's existing stack |
| Post-call data flow | What happens to call data, transcripts, and outcomes |

### Internal team use cases

| Situation | What to map |
|---|---|
| Internal process design | Any recurring team workflow that needs to be documented |
| New team member onboarding | How the business operates, which tools do what, who owns what |
| SOP visualisation | Standard operating procedures shown as a flow |
| Planning a new service offering | Map the delivery process before you launch it |
| Retrospective or post-mortem | What the process looked like and where it broke down |

> **Rule of thumb:** If you have left a meeting and someone would benefit from seeing how things connect, use this skill. It works for any meeting — client, internal, or cross-team.

Send client-facing PDFs within 24 hours of the call. For internal use, save to the relevant team or project folder.

---

## Brand Reference

| Brand | Primary Colour | When to use |
|---|---|---|
| Automate Accelerator | Orange `#F47920` + Purple `#412F8F` | AA client projects |
| Inspra AI | Green `#39E100` | Inspra client projects |

---

## Common Questions

**I do not have a logo file — where do I get it?**
Download from the shared team folder on Google Drive.

**Can I use this for a prospect before they sign?**
Yes. A diagram at proposal stage shows you understand their business and looks highly professional.

**How long does it take?**
With a Fathom transcript: roughly 5 minutes. From manual notes: 10-15 minutes once you have your notes ready.

**Where do the files get saved?**
You tell Claude where to save them when it asks. Default to your client's project folder on your Desktop.

**What if I only have partial information from the call?**
Claude will ask for anything it cannot determine. You can also mark items as "TBD" and they will appear as open questions in the diagram.

---

## Skill Location (for updates)

```
~/.claude/skills/diagram/SKILL.md
```

When the skill is updated, download the new version from the shared team folder and replace the file at the path above.
