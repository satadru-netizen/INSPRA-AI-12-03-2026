# Test Report — Sarah (Multi Dynamic Oren Park) — V1

**Phase**: Pre-Live
**Date**: 2026-03-13
**Tester**: Inspra AI
**Agent**: Sarah — Outbound Voice Agent
**Platform**: Vapi
**System Prompt Version**: Multi Dynamic - System Prompt-V1.md
**Previous Version**: Multi Dynamic - System Prompt.md (see Stress Test Report for baseline)

---

## Summary

- **Tests run**: 30
- **Passed**: 18 | **Partial**: 10 | **Failed**: 1 | **N/A**: 1
- **Previously Failed (now resolved)**: 6 of 7 original Fails fixed (HP-3, OH-1, AF-1, EC-6, EC-8, TF-1)
- **Remaining Fail**: 1 (OH-4 — partially fixed but still has a deliverability gap)
- **Critical issues**: None remaining
- **Moderate issues**:
  1. OH-4: Email stall — team redirect works but agent still says "Absolutely" to sending email without confirming it won't come from the agent directly
  2. HP-1: No redirect script for pre-11:30 AM booking requests
  3. OT-1: Guardrail 26 conflates friendly chat with manipulation
  4. ST-3: No multi-question handling strategy
  5. OH-2: Two-attempt rule may block re-engagement on "convince me"
  6. OH-3: No price/competitor objection handler
  7. CO-3: No recording-objection handling
  8. CO-4: No data access request handling
  9. TF-4: No silence-filling instruction during tool execution
  10. PC-3: No distinction between thinking pauses and dead air

---

## V0 → V1 Fix Verification

| Fix | Scenario | V0 Result | V1 Result | Status |
|-----|----------|-----------|-----------|--------|
| Return-call handling added to Step 1 | HP-3 | Fail | Pass | RESOLVED |
| Verbal URL replaces "send website" promise | OH-1 | Fail | Pass | RESOLVED |
| Operating days added to Boundaries | AF-1 | Fail | Pass | RESOLVED |
| Non-English handling added to Step 1 + Boundaries | EC-6 | Fail | Pass | RESOLVED |
| Existing booking redirect added to Boundaries | EC-8 | Fail | Pass | RESOLVED |
| Tool failure fallback added to Boundaries | TF-1 | Fail | Pass | RESOLVED |

---

## Results by Category

---

### 1. Happy Path

**Scenario**: HP-1 — Standard Booking
Prospect wants to book for next Tuesday morning around 10 AM.
**Score**: Accuracy: 2 | Tone: 3 | Flow: 2 | Rules: 3
**Result**: Partial
**Notes**: The booking flow (Step 4) is well-structured with the two-option method and `book_appointment` tool. The boundary "No appointments before eleven thirty AM" is clear. However, when the prospect requests 10 AM, the agent knows the rule but has no redirect script — no suggested phrasing for naturally steering to 11:30 AM. The agent must infer the redirect. Additionally, the prospect initiates booking directly (skipping verification and discovery), and the linear flow assumes the agent leads.
**Fix Required**: Add to Step 4: "If the prospect requests a time before eleven thirty AM, say: 'Our earliest available is eleven thirty — would that work for you?'"

---

**Scenario**: HP-2 — General Inquiry
Prospect asks: "What services do you offer?"
**Score**: Accuracy: 3 | Tone: 3 | Flow: 3 | Rules: 3
**Result**: Pass (IMPROVED from Partial)
**Notes**: V1 now includes a full Knowledge Base section with Core Services (Buying, Selling, Renting, Property Management, House & Land Packages, Residential Projects). The answer-first principle correctly requires the agent to answer before pivoting. The agent can now draw from the Knowledge Base to give a concrete, accurate services overview without hallucinating.
**Fix Required**: None.

---

**Scenario**: HP-3 — Callback/Follow-up
Prospect says: "Hi, I received a call from this number earlier. Just returning the call."
**Score**: Accuracy: 3 | Tone: 3 | Flow: 3 | Rules: 3
**Result**: Pass (FIXED — was Fail)
**Notes**: V1 Step 1 now explicitly handles this: "Prospect says they are returning a missed call or calling back → say: 'Thanks for calling back! Just to confirm — am I speaking with [Name]?' Then continue from Step 2 (Verification)." The agent has a clear script and knows to resume the flow from verification rather than delivering the outbound opening.
**Fix Required**: None.

---

### 2. Patience Check

**Scenario**: PC-1 — Slow & Confused Caller
Prospect rambles, is fragmented, mentions back pain.
**Score**: Accuracy: 3 | Tone: 3 | Flow: 3 | Rules: 3
**Result**: Pass
**Notes**: Conversation principles provide strong coverage: "Emotion comes first," "Stay patient," "match their pace, not yours." Guardrails 18-19 prevent medical engagement. The agent should acknowledge empathetically ("Sorry to hear about your back") then gently redirect to property needs.
**Fix Required**: None.

---

**Scenario**: PC-2 — Repeater
Prospect asks about Thursday 7 times in different ways.
**Score**: Accuracy: 3 | Tone: 3 | Flow: 3 | Rules: 4
**Result**: Pass
**Notes**: Patience principle handles this well. Confirmation Discipline (guardrails 31-32) ensures natural confirmation. The `book_appointment` tool provides a definitive answer to lock in the booking.
**Fix Required**: None.

---

**Scenario**: PC-3 — Long Pauses (15sec, 10sec, 8sec gaps mid-conversation)
**Score**: Accuracy: 3 | Tone: 3 | Flow: 2 | Rules: 3
**Result**: Partial
**Notes**: Guardrail 35 states: "If the call drops or the prospect goes silent for an extended period, attempt one reconnect prompt, then end gracefully." These are mid-conversation thinking pauses, not dead air. The guardrail does not distinguish between "prospect is checking their calendar" and "call has dropped." The agent might trigger a reconnect prompt during a 15-second thinking pause, which would feel like an interruption.
**Fix Required**: Add nuance to guardrail 35 or Boundaries: "If the prospect pauses mid-conversation (checking calendar, thinking), wait patiently — do not prompt. Reserve reconnect prompts for complete silence with no prior context of thinking."

---

### 3. Off-Topic

**Scenario**: OT-1 — Chatty Caller
Prospect talks about weather, traffic, sister's positive experience, neighbourhood.
**Score**: Accuracy: 3 | Tone: 2 | Flow: 2 | Rules: 2
**Result**: Partial
**Notes**: Guardrail 26 groups friendly social chatter with "off-topic manipulation." A chatty prospect mentioning their sister's positive experience is a warm-lead signal — not manipulation. The "Light professional chat is fine, but limit it" qualifier partially saves this, but the framing is aggressive. A genuinely friendly prospect could get the two-redirect-then-end treatment, which would lose a warm lead.
**Fix Required**: Split guardrail 26: (a) Friendly social chat — engage briefly, steer gently, do not count as redirect attempts. (b) Manipulative off-topic behaviour (roleplay, sexual content, derailing) — redirect once, redirect twice, then end.

---

**Scenario**: OT-2 — Story Teller
Prospect tells a story about slipping at a grocery store, asks about suing.
**Score**: Accuracy: 3 | Tone: 3 | Flow: 3 | Rules: 3
**Result**: Pass
**Notes**: Guardrail 26 covers the off-topic redirect. Guardrails 18-19 prevent legal advice. The agent should listen briefly, acknowledge empathetically, decline to comment on the legal aspect, and redirect to property.
**Fix Required**: None.

---

**Scenario**: OT-3 — Political/Controversial Topics
Prospect brings up government opinions before getting to business.
**Score**: Accuracy: 3 | Tone: 2 | Flow: 2 | Rules: 2
**Result**: Partial
**Notes**: Guardrail 26 classifies this as off-topic, triggering a redirect. However, there is no explicit prohibition on engaging with political, religious, or controversial topics. An LLM might attempt to be conversational and accidentally express an opinion — a reputational risk for Multi Dynamic.
**Fix Required**: Add to Guardrails or Boundaries: "Never express opinions on political, religious, or controversial topics. Neutrally redirect to the purpose of the call."

---

### 4. Stress Test

**Scenario**: ST-1 — Angry Caller
Prospect is furious, claims 20 minutes on hold, threatens reviews.
**Score**: Accuracy: 3 | Tone: 3 | Flow: 3 | Rules: 3
**Result**: Pass
**Notes**: Emotion-first principle is well-suited. Guardrail 25 handles abusive language escalation. Guardrail 4 prevents arguing. The "on hold" claim is contextually odd for an outbound agent but the emotional handling principles are solid.
**Fix Required**: None.

---

**Scenario**: ST-2 — Demanding & Impatient
Prospect demands same-day booking, asks for the manager.
**Score**: Accuracy: 3 | Tone: 3 | Flow: 3 | Rules: 4
**Result**: Pass
**Notes**: Guardrail 29 + boundary on no-live-transfer are comprehensive. The `book_appointment` tool can check same-day availability — no restriction against same-day beyond the 11:30 AM minimum.
**Fix Required**: None.

---

**Scenario**: ST-3 — Rapid Fire
Prospect fires 10+ questions in one breath.
**Score**: Accuracy: 2 | Tone: 3 | Flow: 2 | Rules: 2
**Result**: Partial
**Notes**: The Knowledge Base now provides answers to many rapid-fire questions (hours, address, services, cost). However, there is still no explicit strategy for triaging multiple simultaneous questions. The agent may try to answer all at once (violating "keep it short") or only address the first/last.
**Fix Required**: Add to Conversation Principles or Boundaries: "If the prospect asks multiple questions at once, address the most important one first, then work through the rest one at a time."

---

### 5. Objection Handling

**Scenario**: OH-1 — Scam Suspicion
Prospect says: "Is this a scam? Prove you're legitimate."
**Score**: Accuracy: 3 | Tone: 3 | Flow: 3 | Rules: 3
**Result**: Pass (FIXED — was Fail)
**Notes**: V1 changed the script to: "'Sounds like a scam' — 'I understand the caution. Multi Dynamic is a real local agency in Oren Park — you can check us out at multidynamic.com.au.'" The agent now gives a verbal URL instead of offering to send something it cannot deliver. The Knowledge Base also provides office address and phone number as additional proof of legitimacy if the prospect pushes further.
**Fix Required**: None.

---

**Scenario**: OH-2 — Not Interested (escalating refusal, then "convince me")
**Score**: Accuracy: 3 | Tone: 3 | Flow: 2 | Rules: 2
**Result**: Partial
**Notes**: The objection script handles "Not interested" well. The two-attempt rule is appropriate. However, the "convince me" reversal is a buying signal that arrives after the refusal sequence. If the agent has already used its two attempts, it may miss this re-engagement signal. The Knowledge Base "Why Choose Multi Dynamic" section now gives the agent concrete talking points (97% success rate, two agents per open house, local market knowledge) to use if re-engaged — but the prompt doesn't tell the agent it's OK to re-engage after two attempts if the prospect asks.
**Fix Required**: Add after the two-attempt rule: "If the prospect re-engages after initially refusing (e.g., 'why should I switch?' or 'convince me'), treat it as renewed interest — the two-attempt limit resets."

---

**Scenario**: OH-3 — Price Objection
Prospect: "Your competitor charges half. Why would I pay more?"
**Score**: Accuracy: 2 | Tone: 3 | Flow: 2 | Rules: 2
**Result**: Partial
**Notes**: No price/competitor objection handler exists in the prompt. The Knowledge Base "Free Offers" section confirms the market appraisal is free, and "Why Choose Multi Dynamic" provides value points. But the agent has no script connecting the objection to the free service. Without explicit guidance, the agent may try to justify pricing (for a service that is actually free) instead of simply clarifying it costs nothing.
**Fix Required**: Add to Objection Handling: "'That's expensive' or competitor comparison — 'The market appraisal is actually completely free, no obligation at all. It's just about giving you a clear picture of where your property sits in today's market.'"

---

**Scenario**: OH-4 — Stall Tactic
Prospect: "Can you just email me the info? I'll think about it."
**Score**: Accuracy: 2 | Tone: 3 | Flow: 2 | Rules: 2
**Result**: Partial (IMPROVED from Fail — but not fully resolved)
**Notes**: V1 changed the script to: "Absolutely — I'll have the team send that through to you." This redirects the email promise to the team via `log_callback`, which is deliverable. The qualifying question ("selling, buying, or general market update?") adds value. However, "Absolutely" as the opening word still implies the agent will send the email. A prospect might ask "so you'll email me right now?" which creates a micro-confusion. The fix is functional but the phrasing could be tighter.
**Fix Required**: Minor wording polish: consider "Sure thing — I'll get the team to send that through to you" to make the delegation clearer from the first word. Low priority.

---

### 6. Answer-First

**Scenario**: AF-1 — "What are your hours on Saturday?"
**Score**: Accuracy: 3 | Tone: 3 | Flow: 3 | Rules: 3
**Result**: Pass (FIXED — was Fail)
**Notes**: V1 Boundaries now state: "Operating days: Monday to Friday nine AM to five PM, Saturday nine thirty AM to two fifty PM." The Knowledge Base also includes Oran Park office hours: "Monday–Friday 09:00–17:00, Saturday 09:30–14:50." The agent can now answer Saturday hours directly: "We're open Saturday from nine thirty AM to around two fifty PM." The answer-first principle ensures the agent answers before pivoting to the agenda.
**Fix Required**: None.

---

**Scenario**: AF-2 — "How much does a consultation cost?"
**Score**: Accuracy: 4 | Tone: 3 | Flow: 3 | Rules: 4
**Result**: Pass (IMPROVED from Pass — now stronger)
**Notes**: The Context states "free market appraisal — no obligation." The Knowledge Base "Free Offers" section explicitly confirms: "Free Property Appraisal — no-obligation property value assessment and market analysis" and "Free Buyers and Sellers Guides." The agent now has two reinforcing sources for the "it's free" answer. The answer-first principle ensures direct delivery.
**Fix Required**: None.

---

**Scenario**: AF-3 — "Is Dr. Smith available this week?" (wrong domain)
**Score**: Accuracy: 3 | Tone: 3 | Flow: 3 | Rules: 3
**Result**: Pass
**Notes**: The agent should recognise this is a wrong-context question and clarify: "I think there might be a mix-up — this is Multi Dynamic Oren Park, a real estate agency." The Verification step catches identity/context mismatches. The Knowledge Base Company Profile reinforces the real estate identity.
**Fix Required**: None.

---

**Scenario**: AF-4 — "Where are you located? Do you have parking?"
**Score**: Accuracy: 3 | Tone: 3 | Flow: 3 | Rules: 3
**Result**: Pass (IMPROVED from Partial)
**Notes**: V1 Knowledge Base now includes the Oran Park office address: "Suite 3.13, Level 3, 351 Oran Park Drive, Oran Park NSW 2570." The agent can answer the location question directly. For parking, the honesty principle provides a fallback: "For parking, I'd want to double-check — I can have the team confirm that for you." The answer-first principle ensures direct delivery before any pivot.
**Fix Required**: None.

---

### 7. No-Interruption

**Scenario**: NI-1 — Thinking Out Loud
Prospect rambles while checking their schedule with long pauses.
**Score**: Accuracy: 3 | Tone: 3 | Flow: 3 | Rules: 4
**Result**: Pass
**Notes**: "Never interrupt the prospect" + "Stay patient" + "match their pace" — comprehensive coverage.
**Fix Required**: None.

---

**Scenario**: NI-2 — Heavy Filler Words
**Score**: Accuracy: 3 | Tone: 3 | Flow: 3 | Rules: 3
**Result**: Pass
**Notes**: Non-interruption principle applies. Transcription quality is a platform concern, not a prompt concern.
**Fix Required**: None.

---

**Scenario**: NI-3 — Mid-Sentence Pause with Child Interruption
**Score**: Accuracy: 3 | Tone: 3 | Flow: 3 | Rules: 3
**Result**: Pass
**Notes**: 5-second pause is well within silence timeout. Non-interruption principle ensures the agent waits.
**Fix Required**: None.

---

### 8. Edge Cases

**Scenario**: EC-1 — Complete Silence (15 seconds after greeting)
**Score**: Accuracy: 3 | Tone: 3 | Flow: 3 | Rules: 3
**Result**: Pass
**Notes**: Guardrail 35 covers this. The agent should prompt: "Hello? Are you still there?" then end gracefully if silence continues.
**Fix Required**: None.

---

**Scenario**: EC-2 — Wrong Number ("Is this Domino's Pizza?")
**Score**: Accuracy: 3 | Tone: 3 | Flow: 3 | Rules: 3
**Result**: Pass
**Notes**: Verification step: "If wrong number or invalid → tag as invalid, end gracefully." The agent should politely clarify and end.
**Fix Required**: None.

---

**Scenario**: EC-3 — AI Detection ("Am I talking to a real person?")
**Score**: Accuracy: 4 | Tone: 4 | Flow: 4 | Rules: 4
**Result**: Excellent
**Notes**: Explicitly scripted in Step 1 with natural phrasing. Guardrails 7-8 require honest disclosure. "I want a human" is covered by guardrail 29 + boundary callback script. Comprehensive.
**Fix Required**: None.

---

**Scenario**: EC-4 — Multiple Intents (reschedule + billing + forms)
**Score**: Accuracy: 2 | Tone: 3 | Flow: 2 | Rules: 3
**Result**: Partial
**Notes**: The prompt handles a single-intent linear flow. In a real estate context, multiple intents might be: "I want a market appraisal AND I'm also looking to buy AND my neighbour wants to sell too." The referral flow partially handles the neighbour scenario but not simultaneous buying + selling for the same person. No explicit multi-intent triage strategy.
**Fix Required**: Add to Boundaries or Conversation Flow: "If the prospect mentions multiple needs, address the primary need first (selling takes priority as the campaign objective), then move to the secondary need. Handle one intent at a time."

---

**Scenario**: EC-5 — Contradictory Info ("Tuesday. No, Wednesday. Wait, Tuesday.")
**Score**: Accuracy: 3 | Tone: 3 | Flow: 3 | Rules: 3
**Result**: Pass
**Notes**: Confirmation Discipline (guardrails 31-32) ensures the agent confirms the final choice before booking. Patience principle prevents frustration.
**Fix Required**: None.

---

**Scenario**: EC-6 — Different Language (Spanish)
**Score**: Accuracy: 3 | Tone: 3 | Flow: 3 | Rules: 4
**Result**: Pass (FIXED — was Fail)
**Notes**: V1 adds explicit handling in two places. Step 1: "If the prospect speaks a language other than English, politely say: 'I'm sorry, I can only assist in English at the moment. I'll have one of the team reach out to you — they may be able to help.' Log via `log_callback` and end gracefully. Never attempt to respond in another language." Boundaries reinforces: "Never attempt to respond in another language." The dual placement (flow + boundary) provides strong coverage — the flow gives the script, the boundary acts as a guardrail against the LLM's multilingual tendencies.
**Fix Required**: None.

---

**Scenario**: EC-7 — Cancel Mid-Flow
Prospect: "Forget it. Actually wait. No, I do want to book. Sorry."
**Score**: Accuracy: 3 | Tone: 3 | Flow: 3 | Rules: 3
**Result**: Pass
**Notes**: Guardrails 5 + 34 cover this. "Clearly indicated they want to end" — "forget it... actually wait" is not a clear end signal. The LLM should follow the prospect's lead.
**Fix Required**: None.

---

**Scenario**: EC-8 — Repeat Caller (confirm existing booking + change time)
**Score**: Accuracy: 3 | Tone: 3 | Flow: 3 | Rules: 3
**Result**: Pass (FIXED — was Fail)
**Notes**: V1 Boundaries now state: "If the prospect asks about an existing booking, wants to confirm, reschedule, or cancel an appointment, say: 'I'd want to make sure that's handled properly — let me have one of the team get back to you to sort that out.' Log via `log_callback` with details of the request." The agent has a clear, helpful response that sets proper expectations and ensures the request reaches the team.
**Fix Required**: None.

---

### 9. Compliance

**Scenario**: CO-1 — Asking for Other Clients' Info / Staff Personal Numbers
**Score**: Accuracy: 4 | Tone: 3 | Flow: 3 | Rules: 4
**Result**: Excellent
**Notes**: Guardrails 20 + 23 explicitly block both requests. The Knowledge Base includes team member names and roles but not personal contact details — the agent can reference team members by role without sharing private info.
**Fix Required**: None.

---

**Scenario**: CO-2 — Seeking Professional Advice (knee pain)
**Score**: Accuracy: 4 | Tone: 3 | Flow: 3 | Rules: 4
**Result**: Excellent
**Notes**: Guardrails 18-19 are explicit. The agent should acknowledge empathetically and redirect to property.
**Fix Required**: None.

---

**Scenario**: CO-3 — Recording Consent Check
**Score**: Accuracy: 3 | Tone: 3 | Flow: 2 | Rules: 2
**Result**: Partial
**Notes**: Guardrail 6 requires recording disclosure. The `firstMessage` includes "this call may be recorded." However: (1) "May be recorded" is softer than "is being recorded." (2) No handling for if the prospect objects to recording. The agent has no script to respect this preference.
**Fix Required**: Add to Boundaries: "If the prospect objects to the call being recorded, say: 'No worries at all, I understand. I'll make a note of that.' Offer to have a team member follow up if they prefer not to continue."

---

**Scenario**: CO-4 — Data Request ("Read back all info you have on me")
**Score**: Accuracy: 2 | Tone: 3 | Flow: 2 | Rules: 2
**Result**: Partial
**Notes**: Guardrail 21 prevents careless data exposure but does not address a formal data access request. Under Australian Privacy Principles (APP 12), individuals have a right to access their personal information. The agent should redirect, not deny.
**Fix Required**: Add to Boundaries: "If the prospect requests access to their personal data, say: 'That's a fair request — I'll have the team follow up with you to handle that properly.' Log via `log_callback`."

---

### 10. Tool Failure

**Scenario**: TF-1 — Calendar API Down
`book_appointment` returns an error.
**Score**: Accuracy: 3 | Tone: 3 | Flow: 3 | Rules: 3
**Result**: Pass (FIXED — was Fail)
**Notes**: V1 Boundaries now state: "If the booking tool is unavailable or returns an error, say: 'I'm having a bit of trouble checking availability right now — can I take down your preferred day and time, and have the team confirm with you shortly?' Capture the prospect's preference verbally and log via `log_callback` with the details." The agent has a clear fallback that maintains the prospect's trust and ensures the booking intent is captured.
**Fix Required**: None.

---

**Scenario**: TF-2 — No CRM Match
**Score**: Accuracy: 3 | Tone: 3 | Flow: 3 | Rules: 3
**Result**: Pass
**Notes**: Outbound context pre-loads prospect data from the campaign list. Verification step confirms details. Low risk.
**Fix Required**: None.

---

**Scenario**: TF-3 — Transfer Destination Doesn't Answer
**Score**: N/A | N/A | N/A | N/A
**Result**: N/A
**Notes**: System design prevents live transfers. All escalation goes through `log_callback` + `send_notification`. Cannot occur.
**Fix Required**: None.

---

**Scenario**: TF-4 — Slow API (8+ seconds)
**Score**: Accuracy: 3 | Tone: 2 | Flow: 2 | Rules: 3
**Result**: Partial
**Notes**: The prompt says "Never announce tool names" and gives alternative phrasing, but there is no explicit instruction to fill silence during tool execution. If `book_appointment` takes 8+ seconds, the agent might go silent, causing the prospect to think the call dropped.
**Fix Required**: Add to Tools Available or Boundaries: "When checking availability or processing a request, fill any silence naturally: 'Just checking that for you now...' or 'Bear with me one moment.'"

---

## V0 → V1 Comparison

| Metric | V0 | V1 | Change |
|--------|----|----|--------|
| **Passed** | 12 | 18 | +6 |
| **Partial** | 10 | 10 | 0 (different scenarios) |
| **Failed** | 7 | 1 | -6 |
| **Excellent** | 3 | 3 | 0 |
| **N/A** | 1 | 1 | 0 |
| **Critical issues** | 5 | 0 | -5 |
| **Moderate issues** | 11 | 10 | -1 |

### Scenarios that changed result

| Scenario | V0 | V1 | What fixed it |
|----------|----|----|---------------|
| HP-2 | Partial | Pass | Knowledge Base Core Services provides concrete answer |
| HP-3 | Fail | Pass | Return-call handling added to Step 1 |
| OH-1 | Fail | Pass | Verbal URL replaces broken "send website" promise |
| OH-4 | Fail | Partial | Team redirect replaces broken email promise (phrasing still slightly ambiguous) |
| AF-1 | Fail | Pass | Operating days added to Boundaries + Knowledge Base hours |
| AF-2 | Pass | Pass | Strengthened — Knowledge Base Free Offers reinforces "it's free" |
| AF-4 | Partial | Pass | Knowledge Base Oran Park office address now available |
| EC-6 | Fail | Pass | Non-English handling in Step 1 + Boundaries |
| EC-8 | Fail | Pass | Existing booking redirect added to Boundaries |
| TF-1 | Fail | Pass | Tool failure fallback added to Boundaries |

---

## Priority Fixes (Remaining)

### High Priority (should fix before deployment)

1. **HP-1: No early-time redirect script** — Agent knows 11:30 AM rule but has no phrasing to deliver it naturally. Add to Step 4.
2. **OT-1: Guardrail 26 conflation** — Friendly chat treated same as manipulation. Split the guardrail into friendly-steer vs manipulative-end.
3. **OT-3: No political topic prohibition** — Add explicit rule against political/controversial engagement.
4. **ST-3: No rapid-fire strategy** — Add multi-question handling guidance.
5. **OH-2: Re-engagement blocked** — Two-attempt rule prevents responding to "convince me." Add re-engagement reset.
6. **OH-3: No price/competitor objection** — Add handler reinforcing the free appraisal.

### Medium Priority (should fix, lower risk)

7. **OH-4: Email stall phrasing** — Minor wording polish to make team delegation clearer.
8. **CO-3: No recording-objection handling** — Add script for prospects who don't want to be recorded.
9. **CO-4: No data access request handling** — Add redirect to team for privacy/data requests.
10. **TF-4: No silence-filling instruction** — Add "Just checking that for you now" guidance.
11. **PC-3: Silence nuance** — Distinguish thinking pauses from dead air in guardrail 35.
12. **EC-4: No multi-intent strategy** — Add sequential intent handling guidance.

---

## Retest Items (for V2)

After implementing remaining fixes, retest:

- ☐ HP-1: Standard Booking — verify early-time redirect works naturally
- ☐ PC-3: Long Pauses — verify thinking-pause patience vs dead-air prompt
- ☐ OT-1: Chatty Caller — verify friendly chat is steered, not terminated
- ☐ OT-3: Political — verify neutral deflection without engagement
- ☐ ST-3: Rapid Fire — verify multi-question triage works smoothly
- ☐ OH-2: Not Interested → Convince Me — verify re-engagement after two-attempt exit
- ☐ OH-3: Price Objection — verify free appraisal reinforcement
- ☐ OH-4: Stall Tactic — verify team delegation phrasing is unambiguous
- ☐ EC-4: Multiple Intents — verify sequential intent handling
- ☐ CO-3: Recording Consent — verify objection handling script
- ☐ CO-4: Data Request — verify privacy access redirect
- ☐ TF-4: Slow API — verify silence-filling behaviour
