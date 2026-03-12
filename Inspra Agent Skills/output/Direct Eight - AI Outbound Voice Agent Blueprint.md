# Direct Eight — AI Outbound Voice Agent Blueprint
**Prepared by**: Inspra AI
**Date**: March 10, 2026
**Agent Type**: Outbound (Cold Calling Campaign)

---

## Discovery Summary

### Client Profile
- **Company**: Direct Eight
- **Industry**: Commercial Cleaning (Melbourne / Victoria, Australia)
- **Contacts**: Simon (Primary), Prakash
- **Services**: Commercial cleaning (primary), facility management, asset management, emergency response
- **USP**: CleanPlan tech management platform, fully in-house staff (no subcontracting), family-run business with deep local market knowledge
- **Target Clients**: Businesses with commercial spaces — offices, retail, hospitality, hospitals

### Pain Points
- **Lead conversion is the #1 friction** — generating leads is manageable, but converting them is tough
- **No outbound campaign infrastructure** — no cold calling or AI systems in place today
- **Heavily manual, high-touch sales process** — team goes out to meet every potential client in person
- **Website currently down** (being rebuilt) — limits digital lead generation and bot training material
- **CRM exists but is underutilized** — had a CRM but never used it effectively

### Project Goals
- Launch a **pilot outbound AI cold calling campaign** to generate and convert commercial cleaning leads
- **Book meetings** via Google Calendar / Zoom for qualified prospects
- **Live transfer** high-potential leads directly to a dedicated team mobile number
- **Callback scheduling** — collect info from prospects who prefer human contact, notify team via email
- Consolidate operations into a **single CRM platform** (proposed by Inspra)
- Validate AI-driven outbound as a scalable channel before ramping up volume

---

## Phase 1: Requirements & Knowledge Base
**Objective**: Gather all domain knowledge and business rules to train the AI agent

- [ ] Receive company profile, service descriptions, and sales materials from Simon via email
- [ ] Scrape and index Direct Eight website once it's back online
- [ ] Document target audience: commercial businesses in Melbourne/Victoria needing cleaning services (offices, retail, hospitality, hospitals)
- [ ] Identify key personas: facility managers, office managers, operations directors, business owners
- [ ] Collect existing sales scripts or outreach language (if any) from Simon/Prakash
- [ ] Document CleanPlan platform as a key differentiator for the pitch
- [ ] Define compliance requirements (Australian telemarketing regulations, do-not-call registry)
- [ ] Document objection handling scenarios (price, existing provider, not interested, COVID/sanitization questions)

**Dependencies**: Client to provide knowledge base materials via shared Google Drive link
**Tools**: Google Drive, Email

---

## Phase 2: Data & List Building
**Objective**: Build a targeted prospect list for the outbound campaign

- [ ] Define target criteria: commercial businesses in Melbourne/Victoria with cleaning needs
- [ ] Source prospects from Sales Navigator / Lusha / ZoomInfo
- [ ] Filter by industry (offices, retail, hospitality, healthcare), location (Melbourne/Victoria), company size
- [ ] Validate and cleanse contact data (phone numbers, decision-maker names, titles)
- [ ] Prepare initial batch of **150–200 data points** for pilot campaign
- [ ] Upload validated list to CRM platform

**Dependencies**: Phase 1 (target audience defined)
**Tools**: Sales Navigator, Lusha/ZoomInfo, CRM

---

## Phase 3: Platform Setup
**Objective**: Configure CRM and integrations for campaign operations

- [ ] Create CRM account for Direct Eight (platform TBD — to be proposed by Inspra)
- [ ] Provide Simon & Prakash with login credentials
- [ ] Integrate Google Calendar for meeting bookings
- [ ] Configure Zoom meeting link generation for booked appointments
- [ ] Set up email notifications for:
  - Booked meetings
  - Callback requests (prospect wants human contact)
  - Live transfer logs
- [ ] Configure booking automation rules
- [ ] Walk Simon & Prakash through CRM setup (screen-share session — scheduled for next Tuesday)

**Dependencies**: Phase 1 (requirements finalized)
**Tools**: CRM (TBD), Google Calendar, Zoom, Email/SMTP

---

## Phase 4: AI Voice Agent Development
**Objective**: Build and configure the outbound cold calling AI agent

- [ ] Develop system prompt trained on Direct Eight's services, CleanPlan USP, and industry terminology
- [ ] Configure outbound voice agent with natural conversation flow
- [ ] Build call flow logic:
  - **Opening**: Introduce Direct Eight, identify decision maker
  - **Pitch**: Commercial cleaning services + CleanPlan differentiator
  - **Qualify**: Determine current cleaning situation, pain points, interest level
  - **Interested → Book meeting**: Schedule via Google Calendar with Zoom link
  - **High interest → Live transfer**: Transfer to dedicated mobile number
  - **Wants human contact**: Collect name + phone, send email notification to team
  - **Not interested**: Graceful exit, log outcome
  - **Objection handling**: Price, existing provider, timing, COVID/sanitization positioning
- [ ] Configure calendar/booking integration (Google Calendar + Zoom)
- [ ] Set up live transfer to designated team mobile number(s)
- [ ] Set up callback/notification flow (email to Simon)
- [ ] Provision demo phone number or web call link for testing
- [ ] Create call flowchart document for client review

**Dependencies**: Phases 1–3 complete
**Tools**: Vapi, Google Calendar API, Zoom, CRM

---

## Phase 5: Testing & QA
**Objective**: Validate agent performance before going live

- [ ] Deliver prototype to Simon & Prakash for internal testing
- [ ] Provide structured feedback sheet for documenting issues
- [ ] Simon & Prakash test as mock prospects (various scenarios)
- [ ] Demo to client stakeholders in recurring Tuesday meeting
- [ ] Review and verify:
  - Calendar bookings are created correctly
  - Live transfers connect to the right number
  - Callback notifications arrive via email
  - CRM records are populated properly
- [ ] Iterate on system prompt and call flow based on feedback
- [ ] Confirm client approval before proceeding to deployment

**Dependencies**: Phase 4 (prototype delivered — target: 2–3 days after knowledge base received)
**Tools**: Vapi, Feedback Sheet, CRM

---

## Phase 6: Deployment & Optimization
**Objective**: Go live with pilot campaign and optimize over 3–4 weeks

- [ ] Pre-launch meeting with Simon & Prakash
- [ ] **Decision Gate**: Client Approval ✅ (Yes → Deploy / No → Return to Phase 5)
- [ ] Deploy agent with initial batch of **150–200 contacts**
- [ ] Monitor first 48 hours closely
- [ ] Provide client dashboard for listening to call recordings
- [ ] Weekly recurring meetings (Tuesdays) to review:
  - Call recordings and outcomes
  - Conversion metrics
  - Areas for optimization
- [ ] Ryan to audit calls and flag improvement areas
- [ ] 3–4 week optimization phase with iterative prompt tuning
- [ ] Once optimized, ramp up daily dialing volume

**Dependencies**: Phase 5 (client approval)
**Tools**: Vapi, CRM Dashboard, Call Recording Platform

---

## Timeline & Dependencies

```
Phase 1 (Requirements & KB)     → Week 1
    ↓
Phase 2 (Data & List Building)  → Week 1–2 (parallel with Phase 1 once criteria defined)
    ↓
Phase 3 (Platform Setup)        → Week 1–2 (CRM ready by next Tuesday meeting)
    ↓
Phase 4 (Agent Development)     → Week 1–2 (prototype in 2–3 days after KB received)
    ↓
Phase 5 (Testing & QA)          → Week 2–3 (client testing + Tuesday review meeting)
    ↓
Phase 6 (Deployment & Optimization) → Week 3–7 (go-live + 3–4 week optimization)
```

**Key Milestones**:
- **Next Tuesday**: CRM walkthrough session, calendar/Zoom integration
- **2–3 days after KB received**: Prototype delivered
- **Following Tuesday**: Prototype review meeting
- **Post-approval**: Go live with 150–200 contacts
- **+3–4 weeks**: Optimization complete, ramp up volume

---

## Out of Scope
- Website chatbot (not discussed)
- Inbound call handling (outbound only for this pilot)
- Website development/rebuild (handled separately by Direct Eight)
- Marketing automation beyond call campaign notifications
- Multi-channel campaigns (email, SMS) — outbound voice calls only for pilot

---

## Next Steps

| Action | Owner | Due |
|--------|-------|-----|
| Send email to Simon requesting knowledge base materials (company profile, scripts, FAQs) | Ryan | Immediately |
| Share Google Drive link for asset upload | Ryan | Immediately |
| Provide company profile, service docs, any existing scripts | Simon / Prakash | Before next Tuesday |
| Get website back online | Simon / Direct Eight | This week |
| Set up CRM with login credentials | Dhruv | Before next Tuesday |
| Send recurring Tuesday meeting invite | Ryan | Today |
| Prepare call flowchart for client review | Inspra AI Team | With prototype |
| Deliver prototype (demo bot) | Inspra AI Team | 2–3 days after KB received |

---

## Recurring Cadence
- **Weekly Tuesday meetings** throughout engagement
- **Call recording reviews** by Ryan + client team weekly
- **Optimization iterations** based on real call data post-launch
