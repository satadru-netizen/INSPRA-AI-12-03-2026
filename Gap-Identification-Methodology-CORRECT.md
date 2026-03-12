# Gap Identification Methodology — Corrected & Evidence-Based

**Date**: March 12, 2026  
**Purpose**: Show systematic logic for gap identification using three-point validation  
**Status**: REVISED WITH CORRECTIONS

---

## Universal Methodology Framework

**For EVERY gap identified, I apply this three-point test:**

```
┌─────────────────────────────────────────────────────────────────┐
│ STEP 1: Template Principle                                      │
│ ───────────────────────────────────────────────────────────────  │
│ What does SKILL.md say should be in this phase?                 │
│ Where does template-structure.md place this responsibility?     │
│                                                                  │
│ STEP 2: Transcript Evidence                                     │
│ ───────────────────────────────────────────────────────────────  │
│ Does the client explicitly state this requirement?              │
│ Is this stated as non-negotiable or important?                  │
│ What's the actual quote from transcript?                        │
│                                                                  │
│ STEP 3: Current Blueprint Coverage                              │
│ ───────────────────────────────────────────────────────────────  │
│ Does current blueprint document this?                           │
│ If mentioned, is it adequate/detailed?                          │
│ If not mentioned, it's a GAP candidate                          │
│                                                                  │
│ GAP VERDICT:                                                     │
│ IF (Evidence in transcript) AND                                 │
│    (Template says it belongs here) AND                          │
│    (Blueprint lacks/inadequately covers)                        │
│ THEN: GAP = TRUE                                                │
└─────────────────────────────────────────────────────────────────┘
```

---

## Phase-by-Phase Analysis with Corrections

### PHASE 1: Requirements & Knowledge Base

**SKILL.md Guiding Principle:**
```
"Extraction Process: From the input, extract and organize:
- Client: Company, contacts, industry
- Pain Points: What's broken today
- Goals: What success looks like

For each applicable phase, document:
- Phase name and objective
- Specific sub-tasks (pulled from template, customized to THIS CLIENT)
- Tools/platforms involved  
- Dependencies on prior phases"
```
**Translation**: Phase 1 should contain ALL business rules, client preferences, and operational constraints that guide the AI agent's behavior.

---

#### GAP 1: AI Disclosure & Authenticity Requirement — VERDICT: TRUE GAP ✓

**Test 1: Template Principle**
```
SKILL.md says: "Extract... Goals: What success looks like"
              "Specific sub-tasks... customized to THIS CLIENT"
              
Template-structure.md says: "Phase 1: Requirements & Knowledge Base
                            - Collect existing knowledge base materials
                            - Define business rules and compliance requirements"

✓ PRINCIPLE SUPPORT: YES
   This is a CLIENT-SPECIFIC requirement that should be in Phase 1
```

**Test 2: Transcript Evidence**
```
@40:00 | Megha: "I don't want to lie... This is AI... how does it work? 
                  I am calling on behalf of Megha, of Multi Dynamic Oren Park."

@44:37 | Megha: "Definitely, this is Megha, at least it's Megha 
                  calling from Multi Dynamic."

@39:58 | Megha: "will be the best to, you know, say, because people will 
                  know if this is AI, but why should we shouldn't even lie. 
                  Okay. So how is the, I don't want to, okay, maybe how will 
                  be the, know, this is, hi, this is, you know, this is AI, 
                  how does it work?"

✓ EVIDENCE STRENGTH: EXPLICIT & EMPHATIC
   Client states this is non-negotiable ("I don't want to lie", stated 3+ times)
```

**Test 3: Current Blueprint Coverage**
```
Phase 1 Checklist Current State:
- [ ] Document target audience: local residents...
- [ ] Define secondary audience: Australia-wide...
- [ ] Collect objection handling document...
- [ ] Document lead categorization rules...
- [ ] Document Multi Dynamic track record...
- [ ] Define appointment booking rules...
- [ ] Define call attempt rules...
- [ ] Document agent assignment...
- [ ] Define compliance requirements...

❌ BLUEPRINT COVERAGE: MISSING
   No checkbox or requirement for "AI disclosure must be transparent"
   (Note: Phase 4 mentions "AI disclosure" in the opening but 
           doesn't document it as a requirement/why it matters)
```

**Gap Verdict:**
```
✓ TEMPLATE: Supports inclusion (Phase 1 should have business rules)
✓ TRANSCRIPT: Explicit requirement stated multiple times
✗ BLUEPRINT: Not documented in Phase 1

CONCLUSION: ACTUAL GAP = TRUE ✓

Why this matters:
- Phase 4 developer doesn't know THIS specific client strongly prefers 
  transparent AI disclosure
- Could be interpreted as "just mention it's AI" vs "make it a conversation 
  opener"
- Affects brand perception and customer trust
```

---

#### GAP 2: Natural Conversation & Warm Tone Requirement — VERDICT: PARTIAL GAP ⚠️

**Test 1: Template Principle**
```
SKILL.md: "Specific sub-tasks... customized to THIS CLIENT"
Template: "Train on domain-specific terminology"
                    (Implies: Communication style IS domain-specific)

✓ PRINCIPLE SUPPORT: YES (but weaker than GAP 1)
   Communication requirements are client-specific design decisions
```

**Test 2: Transcript Evidence**
```
@39:58 | Megha: "Could we make more natural? ... I want to make 
                  more natural and authentic, even the AI, number one. 
                  ... strong script and dialogues, you know, funny."

@40:00 | Megha: "and more trying to help, could we make more natural?"

Interpretation: "No strong scripting, be helpful and natural"

✓ EVIDENCE STRENGTH: EXPLICIT
   Client rejects "strong script" and requests "natural, authentic, helpful"
```

**Test 3: Current Blueprint Coverage**
```
Phase 1: [NO MENTION of communication style requirements]

Phase 4: "- [ ] Configure outbound voice agent with natural, warm 
              conversation flow"

⚠️ BLUEPRINT COVERAGE: PARTIALLY MENTIONED
   - Mentioned in Phase 4 (IMPLEMENTATION phase)
   - NOT documented in Phase 1 (REQUIREMENTS phase)
   - This means Phase 1 knows WHAT to do but not WHY

Current status: "Natural tone" as implementation detail, not documented 
                as discovered client requirement/preference
```

**Gap Verdict:**
```
✓ TEMPLATE: Supports inclusion in Phase 1
✓ TRANSCRIPT: Explicit requirement from client
⚠️ BLUEPRINT: Mentioned in Phase 4, missing from Phase 1 

CONCLUSION: PARTIAL GAP = TRUE but different severity ⚠️

Reason: The requirement IS in the blueprint, but in WRONG PHASE.
It should be in Phase 1 with RATIONALE so Phase 4 developer 
understands the "WHY" (client trust, brand image, differentiator).
```

---

#### GAP 3: Referral Capture Process — VERDICT: TRUE GAP ✓

**Test 1: Template Principle**
```
SKILL.md: "Extract... Goals: What success looks like"

From template-structure.md: "Phase 1: [includes] 
- Collect existing knowledge base materials
- Define business rules"

Referral capture is a BUSINESS PROCESS/RULE, not an implementation detail.

✓ PRINCIPLE: YES
```

**Test 2: Transcript Evidence**
```
@46:35 | Megha: "If they said no, if they said no, okay, whatever 
                  your family, friend, anyone, they are looking to buy 
                  or sell. I want to like encourage to family and 
                  friend as well."

@46:51 | Megha: "I want to like encourage to family and friend as well."

Context: This happens when prospect says "not interested" — 
         it's a salvage strategy to capture referrals

✓ EVIDENCE: EXPLICIT
   Client explicitly states this is a desired behavior
```

**Test 3: Current Blueprint Coverage**
```
Discovery Goals mention:
"- **Capture referrals** — ask for family and friend referrals 
                           when prospect is not interested"

Phase 4 mentions:
"- **Not interested → Referral ask**: Ask about family/friends 
                                       who may be interested"

❌ BUT PHASE 1 checklist does NOT include:
   - [ ] Document referral capture process
   - [ ] Define referral data capture fields
   - [ ] Define referral logging/tagging in CRM

Missing: HOW to capture, WHAT to collect, WHERE to store, WHEN to follow up
```

**Gap Verdict:**
```
✓ TEMPLATE: Business rule → belongs in Phase 1
✓ TRANSCRIPT: Explicit strategy mentioned
✗ BLUEPRINT: Identified as goal, mentioned in Phase 4, 
             but NO documented PROCESS in Phase 1

CONCLUSION: ACTUAL GAP = TRUE ✓

Why this matters:
- Phase 4 developer has vague "ask about friends" direction
- No specification of: referral data fields, CRM tagging, follow-up timing
- This is a KEY lead generation pipeline — needs documented process
```

---

#### GAP 5: Post-Appointment Workflow & Document Delivery — VERDICT: TRUE GAP ✓

**Test 1: Template Principle**
```
SKILL.md: "Extract... specific sub-tasks customized to THIS CLIENT"
Template: Phase 5 mentions "Demo to client stakeholders"

Implication: If there's a POST-BOOKING workflow, it must be 
designed in Phase 1 so it can be tested in Phase 5

✓ PRINCIPLE: YES (implicit but strong)
```

**Test 2: Transcript Evidence**
```
@42:52 | Megha: "Once appointment is booked, first things, what are 
                  we going to say? Thank you. You're booking an 
                  appointment and a nice communication. Nice to talk 
                  to you about the phone. And now you have booked in 
                  your appointment for your next this, this, this. 
                  Okay. And then, okay, then another one, what is the, 
                  we're going to send before we meeting the appointment? 
                  What document we need to send it?"

@43:56 | Megha: "Make sure that is all done. These are the things 
                  we want in the process. So, make sure they're 
                  feeling good."

Decoding: Multi-step workflow AFTER appointment booking:
1. Thank you confirmation
2. Pre-meeting document (proposal/market analysis)
3. Reminder email
4. Request client preparation

✓ EVIDENCE: EXPLICIT MULTI-STEP WORKFLOW
   Client specifies exact sequence and emotional tone ("make sure 
   they're feeling good")
```

**Test 3: Current Blueprint Coverage**
```
Phase 1: [NO MENTION]

Phase 4: "- **Interested seller → Book appointment**: Free market 
                                  appraisal via calendar"
         (STOPS AT BOOKING - doesn't continue to after-booking)

Phase 5: "- [ ] Verify: Calendar appointments created correctly 
                       (no overlaps)
                       Callback notifications arriving via email
                       Text message templates sending correctly"
         (Mentions SMS but not the WORKFLOW)

❌ BLUEPRINT COVERAGE: MISSING
   No documented post-booking workflow or document delivery process
```

**Gap Verdict:**
```
✓ TEMPLATE: Client-specific process → Phase 1 requirement
✓ TRANSCRIPT: Explicit workflow described
✗ BLUEPRINT: Completely absent

CONCLUSION: ACTUAL GAP = TRUE ✓

Why this matters:
- Phase 5 testing can't validate what doesn't exist in Phase 1
- Phase 4 won't know whether to automate emails or trigger them manually
- Affects customer experience quality pre-meeting
- Team can't be prepared without knowing what's being sent to customer
```

---

### PHASE 3: Platform Setup

#### GAP 8: SMS/Text Message Templates — VERDICT: FALSE GAP ✗

**Test 1: Template Principle**
```
SKILL.md: "Configure CRM and calendar integrations"
Template: "Phase 3: Platform Setup - SMTP/email configuration, 
                    Notification setup"

✓ PRINCIPLE: SMS templates SHOULD be in Phase 3
```

**Test 2: Transcript Evidence**
```
@40:00 | Megha: "How should we message them? ... this is valid 
                  number, but doesn't [have someone]. How should 
                  we do it? ... These are the things is very clear..."

✓ EVIDENCE: Explicit need for SMS messaging
```

**Test 3: Current Blueprint Coverage**
```
Current Phase 3 ALREADY includes:

"- [ ] Configure SMS/text message templates for:
      - Post-call follow-up when number is valid but not connected
      - Appointment confirmation
      - Pre-appointment document/proposal delivery
- [ ] Set up call disposition tagging in Vault-Re..."

✓ BLUEPRINT COVERAGE: PRESENT & DETAILED
```

**Gap Verdict:**
```
CURRENT BLUEPRINT: COVERS THIS ✓

CONCLUSION: NOT A GAP ✗

My error: I marked this as a gap when it's already documented.
This is a FALSE POSITIVE in my gap analysis.
```

---

#### GAP 10: Team Notification Routing Logic — VERDICT: TRUE GAP ✓

**Test 1: Template Principle**
```
SKILL.md: "Configure... notification setup"
SKILL.md: "Integrations... Configure appointment notifications"

Implies: Notification LOGIC (who gets notified based on what?) 
should be in Platform Setup

✓ PRINCIPLE: YES
```

**Test 2: Transcript Evidence**
```
@24:50 | Megha: "Make sure that connected with that appointment, 
                  make sure that our assistant agent also gets 
                  notified. So he can be previewed..."

@25:00 | Megha: "one assistant has a different core area. Another 
                  assistant has a different core area. And Tirtha 
                  has one assistant and he has a separate area."

@26:04 | Megha: "So booking an appointment, then, if someone is 
                  booking on behalf of me, then it goes to me and 
                  my assistant agents, wherever, that working on 
                  that area, okay, and then if that is, to Tirtha, 
                  is another city..."

Decoded requirement:
- Appointment in Megha's area → Notify Megha + relevant assistant
- Appointment in Tirtha's area → Notify Tirtha + his assistant
- Routing logic: SUBURB-BASED

✓ EVIDENCE: EXPLICIT ROUTING RULES (suburb → agent mapping)
```

**Test 3: Current Blueprint Coverage**
```
Current Phase 3:

"- [ ] Configure appointment notifications to:
      - Megha Poudel (principal agent)
      - Relevant assistant agent (based on suburb/area assignment)
      - Tirtha (for his assigned area)"

This says WHAT (who gets notified) but NOT HOW (routing logic/rules)

Missing: 
- Suburb-to-agent mapping table
- Specific routing rules in Vault-Re
- Assistant agent assignment by area

⚠️ BLUEPRINT COVERAGE: VAGUE, INCOMPLETE
   Mentions notification recipients but not the routing LOGIC
```

**Gap Verdict:**
```
⚠️ TEMPLATE: Supports detailed notification configuration
✓ TRANSCRIPT: Explicit routing rules provided
⚠️ BLUEPRINT: Mentions recipients but lacks routing logic

CONCLUSION: PARTIAL GAP = TRUE ⚠️

Why this matters:
- Configuration team needs to know: "If suburb = Oren Park || 
  Catherine Field, route to Megha + Assistant A1"
- Current blueprint is too vague to implement
- Could result in missed appointments or wrong agent notifications
```

---

### PHASE 4: AI Voice Agent Development

#### GAP 11: AI Disclosure Script & Opening — VERDICT: TRUE GAP ✓

**Test 1: Template Principle**
```
SKILL.md: "For each applicable phase, document:
- Phase name and objective
- Specific sub-tasks (pulled from template, customized to THIS CLIENT)"

Template-structure.md Phase 4: "Configure voice agent (inbound/outbound)"

Implication: System prompt/opening script is a critical sub-task

✓ PRINCIPLE: YES, opening script belongs in Phase 4 documentation
```

**Test 2: Transcript Evidence**
```
@40:00 | Megha: "I don't want to lie... I am calling on behalf of 
                  Megha, of Multi Dynamic Oren Park."

@44:37 | Megha: "Definitely, this is Megha, at least it's Megha 
                  calling from Multi Dynamic. And I do have a plan 
                  to help 100 people in this year, either they're 
                  buying or selling their real estate."

@45:07 | Megha: "If they're interested, means I said this year, 
                  100 people are interested in. Yes. Okay. Then we, 
                  okay, when will be the best time to this week and 
                  next week to meet, Megha."

Extracted opening script elements:
1. "This is an AI assistant" (disclosure)
2. "calling on behalf of Megha from Multi Dynamic Oren Park"
3. "I have a plan to help 100 people... buying or selling"
4. "Do you have any plans...?"

✓ EVIDENCE: VERY SPECIFIC SCRIPT DIRECTION
```

**Test 3: Current Blueprint Coverage**
```
Current Phase 4:

"- [ ] Build call flow logic:
      - **Opening**: Introduce as calling on behalf of Megha/Multi 
                      Dynamic Oren Park, AI disclosure"

⚠️ BLUEPRINT COVERAGE: VAGUE
   Says "AI disclosure" but doesn't provide:
   - Exact wording
   - Sequence of statements
   - What the "100 people plan" commitment is
   - Whether it's part of opening or qualifier
```

**Gap Verdict:**
```
✓ TEMPLATE: Opening script is critical Phase 4 documentation
✓ TRANSCRIPT: Specific script direction provided
⚠️ BLUEPRINT: Mentioned but without detail/accuracy

CONCLUSION: ACTUAL GAP = TRUE ✓

Why this matters:
- Vapi system prompt won't know exact opening sequence
- developer might miss "100 people" commitment reference
- Phrasing affects prospect response rate and trust
- Client expects specific language, not developer interpretation
```

---

#### GAP 12: Specific Booking Flow - Two-Option Method — VERDICT: TRUE GAP ✓

**Test 1: Template Principle**
```
SKILL.md: "specific sub-tasks (pulled from template, customized 
           to THIS CLIENT)"

Template: "Configure voice agent... Calendar/booking integration"

Booking algorithm is a critical sub-task

✓ PRINCIPLE: YES
```

**Test 2: Transcript Evidence**
```
@45:07 | Megha: "When will be the best time this week and next week 
                  to meet, Megha. You know, okay. This week or 
                  next week?"

@45:27 | Megha: "And then, always in the option, maximum two. Okay. 
                  And then, okay, they said, okay, next week. You 
                  want to Wednesday or Thursday?"

@45:39 | Megha: "Particular two. Okay. All right. Then you want to, 
                  they said, you prefer morning or afternoon?"

@45:48 | Megha: "morning. Then we do morning time. Okay. Okay. 
                  9.30 suit to you. Done. Or, we, I don't want to 
                  do any appointment before 11.30."

@46:28 | AI Suggestion: "...instead of, yeah. Correct. Proactively 
                  instead of..."

Breaking down the flow:
1. "This week OR next week?" (2-option choice)
2. If this week: "Wed or Thu?" (2-option choice)
   If next week: "Wed or Thu?" (2-option choice)
3. "Morning OR afternoon?" (2-option choice)
4. "11:30, 12:30, 1:30?" (3-option choice with constraint)
5. Confirm with full details

✓ EVIDENCE: EXPLICIT TWO-OPTION BOOKING FLOW (with fallback 3-option)
```

**Test 3: Current Blueprint Coverage**
```
Current Phase 4:

"- [ ] Build call flow logic:
      - **Interested seller → Book appointment**: Free market 
                              appraisal via calendar"

And under dependencies: "(two-option method mentioned in Phase 1 
                         but not detailed in Phase 4)"

❌ BLUEPRINT COVERAGE: NOT DOCUMENTED IN PHASE 4
   - No step-by-step booking flow
   - No mention that options should be limited to 2
   - No mention of time constraint (11:30 min)
   - No fallback logic if prospect wants different options
```

**Gap Verdict:**
```
✓ TEMPLATE: Booking logic is critical Phase 4 sub-task
✓ TRANSCRIPT: Specific flow algorithm provided
✗ BLUEPRINT: Completely missing detailed booking flow in Phase 4

CONCLUSION: CRITICAL GAP = TRUE ✓

Why this matters:
- Vapi prompt needs exact decision tree to implement
- 2-option method is conversion optimization technique
- Current blueprint would default to open-ended questions
- Would reduce conversion rate significantly
```

---

## Summary: Gap Identification Logic

**All gaps follow this formula:**

| Gap | Template Principle | Transcript Evidence | Blueprint Status | Verdict |
|-----|-------------------|-------------------|------------------|---------|
| **GAP 1** | Phase 1 = business rules | @40:00 "I don't want to lie, this is AI" | ❌ Missing | ✓ TRUE |
| **GAP 2** | Phase 1 = client preferences | @39:58 "make more natural, helpful tone" | ⚠️ Phase 4 only | ⚠️ PARTIAL |
| **GAP 3** | Phase 1 = business process | @46:35 "ask for referrals when not interested" | ⚠️ Vague mention | ✓ TRUE |
| **GAP 5** | Phase 1 = workflow requirement | @42:52 "post-appointment workflow with docs" | ❌ Missing | ✓ TRUE |
| **GAP 8** | Phase 3 = platform config | @40:00 "how should we message them?" | ✓ Present | ✗ FALSE |
| **GAP 10** | Phase 3 = notification logic | @24:50 "correct assistant notified per area" | ⚠️ Vague | ⚠️ PARTIAL |
| **GAP 11** | Phase 4 = opening script | @44:37 "exact script with '100 people' ref" | ⚠️ Vague | ✓ TRUE |
| **GAP 12** | Phase 4 = booking algorithm | @45:07 "2-option method with time constraint" | ❌ Missing | ✓ TRUE |

---

## Key Takeaway: Why Gaps Matter

**A gap exists when:**
1. SKILL.md template suggests it should be in this phase
2. Transcript provides explicit requirement/specification
3. Current blueprint doesn't document it adequately (missing, vague, or in wrong phase)

**For example, GAP 1 logic:**
- ✓ Phase 1 should have "business rules" (SKILL.md)
- ✓ Client explicitly wants "no hiding AI nature" (Transcript)
- ✗ Current blueprint doesn't document this requirement (Blueprint)
- → Therefore: **GAP = TRUE**

---

**Status**: This document shows the CORRECTED gap analysis with actual evidence for each one, including catching false positives (like GAP 8).
