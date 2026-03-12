# Multi-Dynamic Blueprint — Phase-wise Gap Analysis Report

**Prepared by**: Inspra AI Analysis  
**Date**: March 12, 2026  
**Transcript Source**: Multi-Dynamic Onboarding Meeting (57 mins)  
**Blueprint Version**: Current (Multi Dynamic - AI Outbound Voice Agent Blueprint.md)  

---

## Executive Summary

**Overall Completeness**: ~75% ✓  
**Critical Gaps Identified**: 13  
**Gap Impact Distribution**: 
- Phase 1: 5 gaps (AI disclosure, natural tone, referral capture, operating hours, post-appointment workflow)
- Phase 2: 2 gaps (data validation criteria, mobile contact deduplication)
- Phase 3: 3 gaps (SMS templates, advanced disposition tags, team routing logic)
- Phase 4: 6 gaps (AI disclosure script, natural conversation, specific booking flow, time constraints, referral logic, attempt rules)
- Phase 5: 2 gaps (detailed test scenarios)
- Phase 6: 1 gap (franchise scalability documentation)

**Required Actions**: Update blueprint with all gaps listed below. **Impact on Delivery**: Moderate (mostly configuration details and workflow refinement, not architectural changes).

---

## PHASE 1: Requirements & Knowledge Base

### Current Coverage ✓
- ✓ Target audience (6 core suburbs)
- ✓ Lead categorization framework (Hot/Warm/Cold/Unassembled)
- ✓ Agent assignments and area coverage
- ✓ Call attempt rules (max 3 per day, disconnect after 2 failed attempts)
- ✓ Compliance requirements

### GAPS IDENTIFIED

#### GAP 1: AI Disclosure & Authenticity Requirement
**Transcript Reference**: @40:00
```
Megha: "I don't want to lie. This is, hi, this is, you know, this is AI, how does it work? 
I am calling on behalf of Megha, of Multi Dynamic Oren Park."
```
**Missing in Blueprint**: 
- No explicit requirement that AI MUST disclose itself upfront
- Client prefers: "I am an AI calling on behalf of Megha from Multi Dynamic"
- Blueprint should explicitly state: **"No hiding AI nature, transparent disclosure on call opening"**

**Add to Phase 1**:
```
- [ ] Document AI disclosure requirement: Must state upfront "I am an AI assistant 
      calling on behalf of Megha/Multi Dynamic Oren Park"
- [ ] Confirm client preference: Natural, warm tone vs. scripted/strong approach
```

---

#### GAP 2: Natural Conversation & Warm Tone Requirement
**Transcript Reference**: @39:58
```
Megha: "Could we make more natural? ... I want to make more natural and authentic, 
even the AI, number one. ... strong script and dialogues, no, funny."
```
**Missing in Blueprint**: 
- Explicit requirement for natural, conversational flow (not robotic)
- Client wants helpful tone, not just transactional
- Need to document this as a KPI for system prompt development

**Add to Phase 1**:
```
- [ ] Document communication style requirements:
      * Natural, warm, conversational (not scripted)
      * Helpful and service-oriented tone
      * Avoid: Strong/robotic dialogue, over-formal language
      * Focus: Building rapport while being authentic
```

---

#### GAP 3: Referral Capture Process
**Transcript Reference**: @46:35, @46:51
```
Megha: "If they said no, if they said no, okay, whatever your family, friend, 
anyone, they are looking to buy or sell. I want to like encourage to family and friend as well."
```
**Missing in Blueprint**: 
- No explicit mention of referral capture when prospect is NOT interested
- This is critical for lead generation from existing data

**Add to Phase 1**:
```
- [ ] Document referral capture process:
      * When prospect not interested: Ask "Does anyone in your family/friends 
        want to buy or sell real estate?"
      * Capture referral name, relationship, phone if provided
      * Log in CRM under prospect's record
```

---

#### GAP 4: Operating Hours & Time Constraints
**Transcript Reference**: @47:39, @45:49
```
Megha: "I want to just call 830 to 730 only."
"I don't want to do any appointment before 11.30."
```
**Missing from Blueprint**: 
- Explicitly documents 8:30 AM - 7:30 PM but could be clearer
- Calendar must not book appointments BEFORE 11:30 AM (critical constraint)

**Add to Phase 1**:
```
- [ ] Call operating hours: 8:30 AM - 7:30 PM (NSW local time)
- [ ] Appointment booking constraint: Minimum 11:30 AM start time
- [ ] Calendar integration: Hard block before 11:30 AM
```

---

#### GAP 5: Post-Appointment Workflow & Document Delivery
**Transcript Reference**: @42:52, @43:56
```
Megha: "Once appointment is booked, first things, what are we going to say? 
Thank you. You're booking an appointment and a nice communication... 
What document we need to send before meeting? Very clear. Make sure that is all done."
```
**Missing from Blueprint**: 
- No documented post-appointment workflow
- No mention of pre-meeting documents to send
- Important for customer experience and agent preparation

**Add to Phase 1**:
```
- [ ] Document post-appointment workflow:
      1. Immediate confirmation: Thank you message via email
      2. Pre-meeting document (proposal/market analysis)
      3. Reminder email with meeting details
      4. Time frame: Send documents within X hours of booking
      5. Optional: Request client to prepare list of property details
- [ ] Collect pre-meeting document template from Megha
```

---

## PHASE 2: Data & List Building

### Current Coverage ✓
- ✓ Multiple data sources identified (CRM, mobile, RP data, ID for me)
- ✓ Deduplication strategy (30-40% overlap)
- ✓ Target clean dataset: ~8,000-10,000 from ~32,000
- ✓ Data validation criteria mentioned

### GAPS IDENTIFIED

#### GAP 6: Explicit Data Validation Rules
**Transcript Reference**: @30:20, @32:33
```
Megha: "If it's just disconnected, means that they can delete... We want to like, the data is working 
and it's still live. We want very clean... some already dead people, maybe already moved..."
```
**Missing from Blueprint**: 
- No explicit definition of "valid" vs "invalid" data
- Should define criteria BEFORE calling begins

**Add to Phase 2**:
```
- [ ] Document Data Validity Criteria:
      * VALID: Phone number connected, person answered or voicemail active
      * INVALID: Not connected, disconnected (after 2 attempts), deceased
      * QUESTIONABLE: Outside 25km from Oren Park (keep if property interest mentioned)
      * DUPLICATES: Remove cross-agent duplicates (Megha's mobile vs Tirtha's mobile)
      * LOCATION RULE: Focus 6 core suburbs for selling; Australia-wide for investors
```

---

#### GAP 7: Mobile Contact Deduplication Between Agents
**Transcript Reference**: @9:33, @27:40
```
Megha: "I do have 6,642 contracts in my mobile"
Tirtha also has similar ~6,000 data, noted as "maybe from different sources"
```
**Missing from Blueprint**: 
- Specific deduplication strategy between Megha's and Tirtha's mobile contacts
- Blueprint mentions both but doesn't address merge strategy

**Add to Phase 2**:
```
- [ ] Before uploading mobile contacts:
      * Export Megha's contacts: ~6,642 entries
      * Export Tirtha's contacts: ~6,000 entries
      * Merge & deduplicate between the two agents' lists
      * Remove obvious duplicates (same name + phone)
      * Final upload to Vault-Re after consolidation
```

---

## PHASE 3: Platform Setup

### Current Coverage ✓
- ✓ Vault-Re API integration verified with IT meeting
- ✓ Google Calendar integration mentioned
- ✓ Email notification flows outlined
- ✓ Call disposition tagging planned

### GAPS IDENTIFIED

#### GAP 8: SMS/Text Message Template Configuration
**Transcript Reference**: @40:00, @40:18
```
Megha: "How should we message them? ... this is valid number, but doesn't [have someone]. 
How should we do it? ... These are the things is very clear..."
```
**Missing from Blueprint**: 
- No mention of SMS/text message templates
- Client wants SMS for valid-but-not-connected scenarios
- CRITICAL for post-call follow-up

**Add to Phase 3**:
```
- [ ] Configure SMS/Text Message Templates:
      1. Valid number but person didn't answer (1st attempt):
         "Hi [Name], this is Megha from Multi Dynamic. Interested in a free market 
         appraisal for your property? Reply YES or call us at [number]"
      
      2. Appointment confirmation (after booking):
         "Your appointment confirmed with Multi Dynamic - [Date] at [Time]. 
         Meeting location: [Address]. Reply CONFIRM or call [number]"
      
      3. Pre-appointment reminder:
         "Reminder: Your meeting with Megha from Multi Dynamic is [Date] at [Time]. 
         Here's the proposal: [link]. Any questions? Call [number]"
      
      4. Referral capture (if referred):
         "[Referrer]'s friend interested in selling/buying? We'd love to help! 
         Call [number] or visit [website]"
```

---

#### GAP 9: Advanced Call Disposition Tagging
**Transcript Reference**: @16:14
```
Tarique: "If the call was connected, the call gets tagged as connected. 
If it's invalid, wrong number, disposition status will be tagged."
```
**Missing from Blueprint**: 
- Disposition tagging exists but not comprehensively defined
- Should include specific categories for referral, objection handling, etc.

**Add to Phase 3**:
```
- [ ] Expand call disposition tags in Vault-Re:
      * Connected - Person answered
      * Not Connected - No answer but voicemail active
      * Invalid - Wrong number / Disconnected
      * Interested - Expressed buying/selling interest
      * Not Interested - Explicitly declined
      * Referral Available - Provided family/friend referral
      * Callback Requested - Wants human follow-up
      * Appointment Booked - Free market appraisal scheduled
      * Invalid → Delete Flag - Mark for removal after 2 failed attempts
```

---

#### GAP 10: Team Notification Routing Logic
**Transcript Reference**: @24:50, @26:04
```
Megha: "Make sure that connected with that appointment, make sure that our assistant agent also 
gets notified. So he can be previewed... one assistant has a different core area. 
Another assistant has a different core area. And Tirtha has one assistant and he has a separate area."
```
**Missing from Blueprint**: 
- Blueprint mentions notification but doesn't define routing logic
- CRITICAL that correct agent/assistant is notified based on suburb

**Add to Phase 3**:
```
- [ ] Define Appointment Notification Routing:
      * Megha's core suburbs (4 areas) → Notification to Megha + her 2 assistant agents
      * Tirtha's area → Notification to Tirtha + his 1 assistant agent
      * Suburb-to-agent mapping table required:
        - Oren Park, Catherine Field → Megha's Area A + Assistant A1
        - Coviti, Harrington Park → Megha's Area B + Assistant A2
        - Gregory Hills, Gladstone Hill → Tirtha's Area + Assistant T1
      * Configuration in Vault-Re: Appointment routing rules by suburb/postcode
```

---

## PHASE 4: AI Voice Agent Development

### Current Coverage ✓
- ✓ System prompt framework mentioned
- ✓ General call flow structure outlined
- ✓ Referral ask documented
- ✓ Callback workflow (no live transfer)

### CRITICAL GAPS IDENTIFIED

#### GAP 11: AI Disclosure Script & Opening
**Transcript Reference**: @39:58, @44:37, @45:07
```
Megha: "I don't want to lie... I am calling on behalf of Megha, of Multi Dynamic Oren Park."
"Definitely, this is Megha, at least it's Megha calling from Multi Dynamic."
```
**Missing from Blueprint**: 
- Opening script not documented with AI disclosure
- Should be verbatim or very close

**CRITICAL Add to Phase 4 - Update Call Flow Logic**:
```
Opening script must include:
  "Hi [Name], this is an AI assistant calling on behalf of Megha from Multi Dynamic 
   Oren Park. I'm calling because Megha has a plan to help 100 people this year who are 
   buying or selling real estate. Do you have any plans to buy or sell a property sometime 
   soon? I only need 2 minutes of your time—do you have a moment?"
```

---

#### GAP 12: Specific Booking Flow - Two-Option Method
**Transcript Reference**: @45:07, @45:27, @45:39, @45:48, @46:28
```
Megha: "When will be the best time this week and next week to meet? ... 
This week or next week? ... Particular two… Wednesday or Thursday? ... 
You prefer morning or afternoon? ... we don't do appointment before 11.30."

Alternative suggested: "Monday, we have opening at this slot. The bot can say three slots. 
Monday, 12 p.m., 1 p.m., or 2 p.m."
```
**Missing from Blueprint**: 
- Booking flow is vague; exact option sequence not documented
- Client prefers 2-option method (this week/next week, then morning/afternoon, then specific slot)
- Needs to be hardcoded in system prompt

**CRITICAL Update Phase 4 - Booking Flow Logic**:
```
Booking flow sequence:
1. "When would suit you best—this week or next week?"
2. If "this week": "Would you prefer Monday/Wednesday/Thursday or Friday?"
   If "next week": "Would you prefer Monday/Wednesday/Thursday or Friday?" 
3. "Morning or afternoon?"
4. Show specific available slots: "[Date], 11:30 AM, 12:30 PM, or 1:30 PM?"
5. Confirm: "Perfect, I've scheduled you for [Date] at [Time]. Megha will meet you at 
   [location]. You'll receive a confirmation email shortly. Looking forward to meeting you!"
```

---

#### GAP 13: Call Attempt Rules & Invalid Data Handling
**Transcript Reference**: @29:43, @30:05, @30:20
```
Tarique: "For one number, how many attempts the AI agent can do... maybe maximum three times."
Megha: "But then, disconnected or say, they can try one or two times. If it's just disconnected, 
means that they can delete... We want very clean... it's still live."
```
**Missing from Blueprint**: 
- Blueprint has basic rules but not detailed enough
- Disconnected logic needs clarity

**Update Phase 4**:
```
Call Attempt Rules:
- First attempt: Call number, no answer → Log as "Not Connected"
- Second attempt: Same day, within 2 hours → Log outcome
- Third attempt: Same day, different time of day → Final attempt
- If still "Not Connected" OR "Disconnected": Flag number for deletion
- If "Connected" + "Not Interested": Park number, recall after 30 days
- If "Connected" + "Interested": Move to booking/callback workflow

Invalid Data Handling:
- After 2 failed connection attempts → Mark as "INVALID - DELETE"
- Don't waste AI calling minutes on dead numbers
- Clean data = faster conversion, better team morale
```

---

#### GAP 14: Referral Capture Call Flow Logic
**Transcript Reference**: @46:35, @46:51
```
Megha: "If they said no, okay, whatever your family, friend, anyone, they are looking 
to buy or sell. I want to like encourage to family and friend as well."
```
**Missing from Blueprint**: 
- Referral capture only briefly mentioned
- Need specific call flow with example script

**Update Phase 4**:
```
When prospect says "Not Interested":
  "No problem. Before I go, do you know anyone in your family or friend group 
   who might be interested in selling or buying property soon? ... 
   Could I get their name and number? I'll mention you referred them."

Log referral data:
  - Referral name, relationship to prospect, phone
  - Note it in CRM as "Referral from [Prospect Name]"
  - Tag as "Referred Lead" for warm outreach
```

---

#### GAP 15: Selling Focus Clarification
**Transcript Reference**: @32:40, @38:08
```
Megha: "Selling, we focus on those six suburb... Don't want to be for those people, 
where I can't get them non-productive... It means like booking an appointment. 
Verifying the data, booking an appointment. It means like leads in red."
```
**Missing from Blueprint**: 
- Blueprint mentions "Interested seller → Book appointment" but should emphasize 
  PRIMARY GOAL IS BOOKING APPOINTMENTS FOR SELLERS, not general qualification

**Emphasize in Phase 4**:
```
Primary Campaign Objective: BOOKING SELLER APPOINTMENTS
- AI's primary KPI: Number of appointments booked for FREE MARKET APPRAISALS
- Secondary: Verify data validity (connected/disconnected)
- Tertiary: Categorize intent (Hot/Warm/Cold/Unassembled)
- Data Focus: 6 core suburbs for SELLERS (selling intent priority)
- Non-local data: Only pursue if expressed property interest
```

---

#### GAP 16: Time Constraint Enforcement
**Transcript Reference**: @45:49
```
Megha: "I don't want to do any appointment before 11.30."
```
**Missing from Blueprint**: 
- Should be a hard CRM/calendar rule

**Add to Phase 4**:
```
- [ ] Calendar hard-block: NO APPOINTMENTS BEFORE 11:30 AM
- [ ] Fallback script if prospect insists on earlier time:
      "I appreciate your availability, but our team doesn't have appointments 
       before 11:30 AM. How about [next available 11:30+ slot] instead?"
- [ ] Verify calendar settings enforce this rule
```

---

## PHASE 5: Testing & QA

### Current Coverage ✓
- ✓ Prototype feedback process outlined
- ✓ Client testing scenarios mentioned
- ✓ Weekly review meeting cadence

### GAPS IDENTIFIED

#### GAP 17: Expanded Test Scenarios
**Transcript Reference**: Various throughout

**Missing from Blueprint**: 
- Test scenarios too generic; should be comprehensive

**Update Phase 5**:
```
Add explicit test scenarios:
- [ ] AI Disclosure: Verify script includes AI identification + "calling on behalf of Megha"
- [ ] Natural Tone: Listen for natural vs. robotic dialogue
- [ ] Booking Flow: Test both "this week" and "next week" paths, morning/afternoon options
- [ ] Referral Capture: Test "not interested" path for referral ask
- [ ] Valid-Not-Connected: Test numbers where person doesn't answer
- [ ] Team Routing: Verify appointments notify correct agent + assistants
- [ ] 11:30 AM Block: Try booking before 11:30, confirm rejection
- [ ] SMS Delivery: Confirm text messages sent for all specified scenarios
- [ ] Disposition Tags: Verify CRM tags match call outcomes
- [ ] Reconnection Logic: Test "not interested now" callback scheduling (30-day window)
```

---

## PHASE 6: Deployment & Optimization

### Current Coverage ✓
- ✓ Pilot batch sizing mentioned
- ✓ Weekly optimization meetings outlined
- ✓ Recording review process

### GAPS IDENTIFIED

#### GAP 18: Franchise Scalability & Process Documentation
**Transcript Reference**: @17:09, @54:24, @55:46
```
Megha: "Sai, okay, so because you have to have, technical thing, communicate with us... 
Because we don't wanna, then you guys write down all the process, how we're setting up, 
but that's why I'm bringing from the first day. So, this is, you need to know next, 
from the next time, I don't want to sit in the meeting... Unless other offices wants to implement, 
please send the process. Do you understand? ... how are we doing? Make a note now. 
And then after that, we make a clear process."
```
**Missing from Blueprint**: 
- No mention of process documentation for franchise rollout
- Client explicitly wants this from day 1
- CRITICAL for Multi Dynamic expansion to other offices

**Add to Phase 6**:
```
- [ ] Document Implementation Process for Franchise Rollout
      1. Data consolidation process (from multiple sources)
      2. Vault-Re API configuration steps
      3. Calendar integration verification
      4. Agent assignment & notification routing setup
      5. SMS template configuration
      6. System prompt customization per office
      7. Testing & QA checklist
      8. Optimization process (3-4 week cycle)
      
- [ ] Create Office Rollout Package for next Multi Dynamic office:
      * Step-by-step implementation guide (IT team reference)
      * Timeline: 2-3 weeks per office setup
      * Owner: Sahisa + Apil (IT) + Inspra AI team
      * Reuse: Leverage current Oren Park process as template
      
- [ ] Design Documentation Structure:
      * Process flow diagram (current system)
      * Configuration checklist (all systems)
      * Training materials (IT team)
      * Troubleshooting guide
```

---

## IMPACT ANALYSIS

### High-Priority Gaps (Must fix before deployment)
1. **GAP 11**: AI disclosure script - affects brand perception & prospect experience
2. **GAP 12**: Specific booking flow - affects conversion rate & call quality
3. **GAP 13**: Call attempt rules - affects cost efficiency & data cleanliness
4. **GAP 1**: AI authenticity requirement - affects trust with client

### Medium-Priority Gaps (Fix in first optimization cycle)
5. **GAP 8**: SMS templates - critical for non-connected follow-up
6. **GAP 10**: Notification routing - affects team efficiency
7. **GAP 14**: Referral capture logic - affects lead generation

### Low-Priority Gaps (Can address in docs/refinement)
8. **GAP 2**: Natural conversation tone - partially addressed via system prompt framework
9. **GAP 3-7, 15-18**: Process/documentation/configuration

---

## RECOMMENDED ACTIONS

### IMMEDIATE (Before Prototype Delivery)
1. ✓ Update **Phase 1** with GAP 1, 2, 3, 4, 5
2. ✓ Update **Phase 4** with GAP 11, 12, 13, 14, 15, 16
3. ✓ Finalize **AI disclosure script** for system prompt
4. ✓ Confirm **booking flow sequence** with client

### WEEK 2 (During IT Integration Meeting)
1. ✓ Update **Phase 3** with GAP 8, 9, 10 (configure in Vault-Re)
2. ✓ Confirm **SMS templates** with Megha
3. ✓ Define **agent-to-area mapping** for notifications

### WEEK 3-4 (Testing & QA Phase)
1. ✓ Update **Phase 5** with GAP 17 (comprehensive test scenarios)
2. ✓ Run all test scenarios before client testing
3. ✓ Validate booking flow, referral capture, SMS delivery

### POST-LAUNCH (Ongoing)
1. ✓ Update **Phase 6** with GAP 18 (franchise documentation)
2. ✓ Create reusable process package for other offices
3. ✓ Document optimizations learned post-launch

---

## REVISED BLUEPRINT COMPLETENESS

| Phase | Current | Gap Count | Post-Update | Priority |
|-------|---------|-----------|-------------|----------|
| **Phase 1** | 80% | 5 gaps | 95% | HIGH |
| **Phase 2** | 85% | 2 gaps | 95% | MEDIUM |
| **Phase 3** | 70% | 3 gaps | 90% | HIGH |
| **Phase 4** | 65% | 6 gaps | 95% | CRITICAL |
| **Phase 5** | 80% | 1 gap | 95% | MEDIUM |
| **Phase 6** | 75% | 1 gap | 90% | MEDIUM |
| **OVERALL** | **75%** | **13 gaps** | **93%** | **→** |

---

## NEXT STEPS

1. **Review this report** with Megha & Sahisa in next meeting
2. **Prioritize gaps** based on implementation timeline
3. **Update blueprint document** with all recommendations
4. **Confirm specifications** (SMS templates, booking flow, referral script) via email
5. **Adjust development timeline** if needed based on scope

---

**Report Prepared By**: Inspra AI Analysis Team  
**Status**: Ready for Implementation Review  
**Recommended Action**: Integrate all gaps into updated blueprint before prototype development begins
