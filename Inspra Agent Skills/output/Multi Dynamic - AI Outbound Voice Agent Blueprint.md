# Multi Dynamic Oren Park — AI Outbound Voice Agent Blueprint
**Prepared by**: Inspra AI
**Date**: March 12, 2026
**Agent Type**: Outbound (Data Verification & Appointment Booking Campaign)

---

## Discovery Summary

### Client Profile
- **Company**: Multi Dynamic Oren Park (Franchisee of Multi Dynamic Real Estate)
- **Industry**: Real Estate (New South Wales, Australia)
- **Structure**: Franchisee system — 7 offices, head office manages centrally
- **Contacts**: Megha Poudel (Principal Agent), Sahisa Sunuwar (Admin/Operations), Tirtha (Senior Agent), Apil (IT Support)
- **CRM**: Vault-Re (centralized across all offices)
- **Core Area**: Oren Park, Catherine Field, Coviti, Harrington Park, Gregory Hills, Gladstone Hill (6 suburbs)
- **USP**: 30-40 years combined experience, proven local track record (67+ properties sold), boutique agency service with result-driven focus, number one selling agent history

### Pain Points
- **New office with low brand awareness** — only 10-20% of local residents know Multi Dynamic Oren Park (opened 5 months ago)
- **Cold calling fatigue for human agents** — assistant agents are new to the industry (3-5 months), demotivated after repeated rejections across 50-60 daily calls
- **Massive unverified data pool** — ~30,000-35,000 contacts across multiple sources (CRM, mobile, RP data, ID for me) with significant duplicates, invalid numbers, and outdated entries
- **No automated data verification** — manual calling to verify contacts is time-consuming and unproductive for experienced agents
- **Agents spend time on non-productive activities** — principal agent wants to focus on post-appointment conversion, not cold calling
- **No systematic lead categorization** — contacts need to be classified as Unassembled, Cold, Warm, or Hot but this is done manually

### Project Goals
- **Verify and clean contact data** — call every contact, confirm validity, remove disconnected/invalid numbers
- **Qualify leads** — determine buying/selling intent and urgency (Unassembled, Cold, Warm, Hot)
- **Book appointments** — schedule free market appraisals for interested sellers
- **Capture referrals** — ask for family and friend referrals when prospect is not interested
- **Categorize systematically** — tag all contacts by status, intent, and urgency in Vault-Re CRM
- **Free up human agents** — let AI handle initial outreach so assistant agents and principal can focus on high-value face-to-face work
- **Create a repeatable process** — document the system so it can be rolled out to other Multi Dynamic offices

---

## Phase 1: Requirements & Knowledge Base
**Objective**: Gather all domain knowledge and business rules for the AI agent

- [ ] Document target audience: local residents in 6 core suburbs (Oren Park, Catherine Field, Coviti, Harrington Park, Gregory Hills, Gladstone Hill)
- [ ] Define secondary audience: Australia-wide contacts with local property interest
- [ ] Collect objection handling document from Megha Poudel
- [ ] Document lead categorization rules:
  - Hot: buying/selling within 3 months
  - Warm: buying/selling within 6-12 months
  - Cold: interested but 12+ months out
  - Unassembled: no decision, beyond 12 months
- [ ] Document Multi Dynamic Oren Park's track record and key selling points (67+ sold, top selling agent history, 30-40 years experience)
- [ ] Define appointment booking rules (two-option method, no appointments before 11:30 AM, operating hours 8:30 AM - 7:30 PM)
- [ ] Define call attempt rules: max 3 attempts per number per day, disconnected after 2 failed attempts = delete
- [ ] Document agent assignment: Megha (core suburbs), Tirtha (separate area), each with assistant agents covering sub-areas
- [ ] Define compliance requirements: Australian telemarketing regulations, do-not-call registry

**Dependencies**: Megha to provide objection handling document
**Tools**: Vault-Re CRM, Email

---

## Phase 2: Data & List Building
**Objective**: Consolidate and prepare contact lists for outbound campaign

- [ ] Export existing Vault-Re CRM contacts (~2,844 contacts for Oren Park office)
- [ ] Export Megha's mobile contacts (~6,000+) to CSV
- [ ] Export Tirtha's mobile contacts (similar volume) to CSV
- [ ] Source RP data for 6 core suburbs (~12,000-13,000 contacts)
- [ ] Source ID for me data for core area (~12,000-13,000 contacts)
- [ ] Deduplicate across all sources (estimated 30-40% overlap)
- [ ] Validate and cleanse contact data (phone numbers, names, addresses)
- [ ] Target: clean dataset of ~8,000-10,000 verified contacts from ~32,000 raw
- [ ] Upload consolidated list to Vault-Re CRM
- [ ] Ensure minimum data per contact: full name, phone number, address, email (where available)

**Dependencies**: Phase 1 (target criteria defined), IT Support (Apil) for data exports
**Tools**: Vault-Re CRM, Excel/CSV, RP Data platform, ID for me platform

---

## Phase 3: Platform Setup
**Objective**: Configure CRM and calendar integrations

- [ ] Verify Vault-Re API capabilities with Vault-Re support team (separate meeting with IT)
- [ ] Integrate Google Calendar with Vault-Re (verify no overlap issues)
- [ ] Configure appointment notifications to:
  - Megha Poudel (principal agent)
  - Relevant assistant agent (based on suburb/area assignment)
  - Tirtha (for his assigned area)
- [ ] Set up email notification flow for callback requests
- [ ] Configure SMS/text message templates for:
  - Post-call follow-up when number is valid but not connected
  - Appointment confirmation
  - Pre-appointment document/proposal delivery
- [ ] Set up call disposition tagging in Vault-Re (Connected, Not Connected, Invalid, Interested, Not Interested, Appointment Booked, Callback Requested)

**Dependencies**: Phase 1 (requirements), IT Support meeting with Vault-Re team (next week)
**Tools**: Vault-Re CRM, Google Calendar, Email/SMTP

---

## Phase 4: AI Voice Agent Development
**Objective**: Build and configure the outbound AI voice agent

- [ ] Develop system prompt following Inspra AI mandatory framework
- [ ] Configure outbound voice agent with natural, warm conversation flow
- [ ] Build call flow logic:
  - **Opening**: Introduce as calling on behalf of Megha/Multi Dynamic Oren Park, AI disclosure
  - **Verify**: Confirm contact name and suburb/location
  - **Qualify**: Determine buying/selling intent and timeline
  - **Categorize**: Tag as Hot, Warm, Cold, or Unassembled
  - **Interested seller → Book appointment**: Free market appraisal via calendar
  - **Interested buyer → Capture details**: Record buying criteria
  - **Not interested → Referral ask**: Ask about family/friends who may be interested
  - **Wants human contact → Log callback**: Capture details, notify team via email
  - **Invalid/disconnected → Tag and skip**: Mark for removal
- [ ] Configure calendar/booking integration (Google Calendar linked to Vault-Re)
- [ ] Set up callback notification flow (no live transfer — log and notify instead)
- [ ] Provision demo phone number for testing
- [ ] Create call flowchart document for client review

**Dependencies**: Phases 1-3 complete
**Tools**: Vapi, Google Calendar API, Vault-Re CRM

---

## Phase 5: Testing & QA
**Objective**: Validate agent performance before going live

- [ ] Deliver prototype to Megha and Sahisa for internal testing
- [ ] Provide structured feedback sheet
- [ ] Test scenarios: happy path, objections, invalid numbers, referral ask, appointment booking
- [ ] Demo to Megha in recurring meeting
- [ ] Verify:
  - Calendar appointments created correctly (no overlaps)
  - Correct agent/assistant notified based on area
  - Callback notifications arriving via email
  - Vault-Re CRM records tagged correctly (disposition, category)
  - Text message templates sending correctly
- [ ] Iterate on system prompt based on feedback
- [ ] Confirm client approval before deployment

**Dependencies**: Phase 4 (prototype delivered)
**Tools**: Vapi, Feedback Sheet, Vault-Re CRM

---

## Phase 6: Deployment & Optimization
**Objective**: Go live and optimize over 3-4 weeks

- [ ] Pre-launch meeting with Megha, Sahisa, and IT
- [ ] **Decision Gate**: Client Approval (Yes → Deploy / No → Return to Phase 5)
- [ ] Deploy agent with initial batch of contacts
- [ ] Monitor first 48 hours closely
- [ ] Provide Megha with dashboard access to listen to all call recordings
- [ ] Weekly recurring meetings to review:
  - Call recordings and outcomes
  - Data verification progress (valid vs invalid contacts)
  - Lead categorization accuracy
  - Appointment booking success rate
  - Areas for optimization
- [ ] 3-4 week optimization phase with iterative prompt tuning
- [ ] Document the process for rollout to other Multi Dynamic offices

**Dependencies**: Phase 5 (client approval)
**Tools**: Vapi, Vault-Re CRM Dashboard, Call Recording Platform

---

## Timeline & Dependencies

```
Phase 1 (Requirements & KB)     → Week 1
    ↓
Phase 2 (Data & List Building)  → Week 1-2 (parallel with Phase 1 once criteria defined)
    ↓
Phase 3 (Platform Setup)        → Week 1-2 (IT meeting with Vault-Re team next week)
    ↓
Phase 4 (Agent Development)     → Week 2-3 (prototype after IT meeting completed)
    ↓
Phase 5 (Testing & QA)          → Week 3-4 (client testing + review meetings)
    ↓
Phase 6 (Deployment & Optimization) → Week 4-8 (go-live + 3-4 week optimization)
```

**Key Milestones**:
- **Next week**: IT meeting with Vault-Re team to confirm API capabilities
- **Week 2**: Data consolidation and deduplication complete
- **Week 2-3**: Prototype delivered for testing
- **Post-approval**: Go live with initial contact batch
- **+3-4 weeks**: Optimization complete, process documented for other offices

---

## Out of Scope
- Inbound call handling (outbound only for this pilot — inbound planned for future phase)
- Website chatbot or web inquiry integration (mentioned but not in current scope)
- Listed property inquiry handling (mentioned for future)
- International contacts (Australian domestic only)
- Contacts beyond 25km radius of Oren Park for selling purposes
- Marketing automation beyond call campaign notifications

---

## Next Steps

| Action | Owner | Due |
|--------|-------|-----|
| Provide objection handling document | Megha Poudel | Before next meeting |
| Export mobile contacts to CSV | Megha + Tirtha | This week |
| Schedule IT meeting with Vault-Re support team | Sahisa + Apil (IT) | Early next week |
| Verify Vault-Re API capabilities | Inspra AI + Apil | During IT meeting |
| Confirm Google Calendar integration status | Apil (IT) | During IT meeting |
| Set up CRM disposition tags | Sahisa | Before prototype |
| Deliver prototype demo | Inspra AI | 2-3 days after IT meeting |
| Document process for office rollout | Sahisa + Inspra AI | After optimization |

---

## Recurring Cadence
- **Weekly meetings** throughout engagement (same time slot as discovery call)
- **Call recording reviews** by Megha + team weekly
- **Optimization iterations** based on real call data post-launch
- **Process documentation** ongoing for franchise rollout
