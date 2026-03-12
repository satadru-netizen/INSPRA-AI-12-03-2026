# Bright Smile Dental — AI Inbound Receptionist Agent Blueprint
**Prepared by**: Inspra AI
**Date**: 10 March 2026
**Agent Type**: Inbound

---

## Discovery Summary

### Client Profile
- **Company**: Bright Smile Dental
- **Location**: Parramatta, Sydney
- **Industry**: Healthcare — Dental Practice
- **Size**: 3-dentist practice
- **Operating Hours**: Mon–Sat, 8:00 AM – 6:00 PM
- **Key Contacts**:
  - Dr. Sarah Chen (Owner)
  - Maria (Office Manager)
- **Existing Tech**: Google Calendar for scheduling, basic website
- **Budget**: Flexible — ROI expected within 3 months

### Pain Points
1. **Missed inbound calls**: 30% of calls go unanswered during peak hours (10 AM – 2 PM)
2. **Receptionist overload**: Single receptionist cannot simultaneously handle phone calls and walk-in patients
3. **After-hours gap**: No call handling outside Mon–Sat 8 AM – 6 PM — all after-hours calls are lost
4. **Repetitive inquiries**: High volume of routine questions (hours, location, services, insurance) consuming staff time
5. **No voice solution**: Competitors use chatbots, but Bright Smile wants a voice-first experience that feels warm and professional

### Project Goals
1. **Reduce missed calls to near-zero** — AI handles overflow and after-hours calls
2. **Free up receptionist capacity** — Maria can focus on walk-ins and in-office tasks during peak hours
3. **Automate appointment booking & rescheduling** — Direct Google Calendar integration for real-time scheduling
4. **Handle general inquiries** — Hours, location, services, and insurance questions answered instantly
5. **Deliver warm, professional voice experience** — Not robotic; matches the clinic's patient-friendly brand
6. **Demonstrate ROI within 3 months** — Measurable reduction in missed calls, increase in booked appointments

---

## Phase 1: Requirements & Knowledge Base
**Objective**: Gather all domain knowledge and business rules needed to build the AI receptionist.

- [ ] Collect clinic services list (general dentistry, cosmetic, orthodontics, emergency, etc.)
- [ ] Document accepted insurance providers and common insurance FAQs
- [ ] Gather appointment types and durations (consultation, cleaning, filling, crown, etc.)
- [ ] Record clinic hours, location details, parking info, public transport directions
- [ ] Document dentist profiles (Dr. Sarah Chen + 2 others) and their specialties/availability
- [ ] Collect existing phone scripts or greeting templates from Maria
- [ ] Define business rules: cancellation policy, no-show policy, minimum booking notice
- [ ] Identify compliance requirements (Australian healthcare privacy — APPs under the Privacy Act 1988)
- [ ] Map peak-hour call patterns and common caller scenarios
- [ ] Define escalation rules (when to transfer to a human — e.g., emergencies, complaints, complex insurance)

**Tools**: Google Docs, client-provided materials
**Dependencies**: None (starting phase)

---

## Phase 2: Data & Contact Database
**Objective**: Set up the patient contact infrastructure for the inbound agent.

- [ ] Import existing patient contact list from clinic records (if available)
- [ ] Set up contact database structure in platform (patient name, phone, email, preferred dentist)
- [ ] Define patient segments (new patient vs. returning patient)
- [ ] Map Google Calendar structure — confirm calendar IDs for each dentist
- [ ] Validate data quality and remove duplicates
- [ ] Set up new patient intake data collection fields (name, DOB, insurance, reason for visit)

**Tools**: Google Calendar, clinic patient records, CRM/platform
**Dependencies**: Phase 1 (need business rules before structuring data)

---

## Phase 3: Platform Setup
**Objective**: Configure the voice agent platform and all integrations.

- [ ] Google Calendar integration — read/write access for all 3 dentist calendars
- [ ] Configure appointment booking automation (check availability, create event, send confirmation)
- [ ] Set up rescheduling/cancellation workflow in calendar
- [ ] SMS confirmation setup (appointment reminders and booking confirmations)
- [ ] Email notification setup for clinic staff (new bookings, cancellations, escalations)
- [ ] Configure call routing: peak hours (overflow to AI), after-hours (AI primary), standard hours (ring receptionist first, AI fallback)
- [ ] Set up phone number (Australian local number or porting existing clinic number)
- [ ] Notification to Maria/Dr. Chen for escalated calls (Slack, SMS, or email)

**Tools**: Google Calendar API, SMS provider, voice platform (Vapi/Livekit — TBC), clinic phone system
**Dependencies**: Phase 1 & 2 (calendar structure and business rules required)

---

## Phase 4: AI Voice Agent Development
**Objective**: Build, train, and configure the inbound AI receptionist agent.

- [ ] Develop system prompt with warm, professional tone matching Bright Smile's brand
- [ ] Train on dental terminology, common procedures, and insurance language
- [ ] Configure inbound call handling flow:
  - Greeting and caller identification (new vs. returning patient)
  - Appointment booking (check availability across 3 dentists, book, confirm)
  - Appointment rescheduling and cancellation
  - General inquiries (hours, location, directions, services offered)
  - Insurance questions (accepted providers list, direct billing info)
  - After-hours messaging (take message, confirm callback next business day)
  - Emergency routing (redirect to emergency dental services or instruct to call 000)
- [ ] Integrate Google Calendar for real-time availability checks
- [ ] Configure voice selection — warm, natural Australian-friendly voice
- [ ] Set up demo environment (dedicated test phone number or web link)
- [ ] Build fallback handling — graceful handoff to voicemail or Maria when needed
- [ ] Implement call summary logging (what was discussed, actions taken)

**Tools**: Voice agent platform (Vapi/Livekit — TBC), Google Calendar API
**Dependencies**: Phase 1, 2, 3 (knowledge base, data, and platform must be ready)

---

## Phase 5: Testing & QA
**Objective**: Validate the agent handles all real-world scenarios accurately and naturally.

- [ ] Internal team tests — simulate new patient booking, rescheduling, insurance inquiry, after-hours call
- [ ] Test Google Calendar integration end-to-end (booking creates correct event, no double-bookings)
- [ ] Test edge cases: fully booked day, dentist on leave, caller requesting specific dentist, unclear request
- [ ] Demo to Dr. Sarah Chen and Maria — collect feedback on tone, accuracy, and flow
- [ ] Prepare feedback collection sheet for structured input
- [ ] Test call routing logic (peak hours overflow, after-hours primary, standard hours fallback)
- [ ] Validate SMS/email confirmations are sent correctly
- [ ] Verify escalation paths work (transfer to Maria, emergency routing)
- [ ] Iterate on system prompt and flows based on feedback (minimum 2 revision cycles)

**Tools**: Test phone, feedback sheet, voice platform analytics
**Dependencies**: Phase 4 (agent must be built before testing)

---

## Phase 6: Deployment
**Objective**: Launch the AI receptionist into production at Bright Smile Dental.

- [ ] Pre-launch meeting with Dr. Chen and Maria — confirm go-live checklist
- [ ] **Decision Gate: Client Approval** — Dr. Chen signs off on agent performance
- [ ] Deploy to production phone system (connect to clinic's main line or dedicated overflow line)
- [ ] Configure live call routing with clinic's phone provider
- [ ] Staff briefing — train Maria on monitoring dashboard, escalation handling, and manual overrides
- [ ] Monitor first 48 hours — review all call logs, flag any issues
- [ ] Week 1 daily check-ins with Maria
- [ ] Week 2-4 weekly performance reviews
- [ ] Establish ongoing support channel (email/Slack for issue reporting)

**Tools**: Voice platform, clinic phone system, monitoring dashboard
**Dependencies**: Phase 5 (QA must pass and client must approve)

---

## Phase 7: Website Chatbot (Conditional — Future Scope)
**Objective**: Add a text-based chatbot to Bright Smile's website to complement the voice agent.

- [ ] Conversation flow design mirroring voice agent capabilities
- [ ] Website widget integration on existing site
- [ ] Connect chatbot to same Google Calendar backend
- [ ] Sync with voice agent knowledge base

**Note**: Not included in current scope. Competitors are using chatbots — this could be a Phase 2 engagement if voice agent proves successful.

**Dependencies**: Phase 6 (voice agent must be live and validated first)

---

## Phase 8: Future Scope (Conditional)
**Objective**: Document expansion opportunities for future engagement.

- [ ] Outbound appointment reminder calls (reduce no-shows)
- [ ] Patient follow-up calls (post-procedure check-ins)
- [ ] Review/feedback collection calls
- [ ] Multi-location support (if Bright Smile expands)
- [ ] Integration with dental practice management software (if they upgrade from Google Calendar)

**Note**: Separate proposal required. Not included in current scope.

---

## Timeline & Dependencies

```
Phase 1: Requirements & Knowledge Base ─────────────┐
                                                     │
Phase 2: Data & Contact Database ────────────────────┤
                                                     │
Phase 3: Platform Setup ─────────────────────────────┘
         │
         ▼
Phase 4: AI Voice Agent Development
         │
         ▼
Phase 5: Testing & QA
         │
         ▼
    [Decision Gate: Client Approval?]
         │ Yes
         ▼
Phase 6: Deployment & Go-Live
         │
         ▼
    Ongoing Support & Optimization
         │
         ▼ (Future)
Phase 7: Website Chatbot
Phase 8: Future Scope
```

**Estimated Timeline**: 4–6 weeks (Phases 1–6)
- Phases 1–3: ~1.5–2 weeks (can partially overlap)
- Phase 4: ~1–1.5 weeks
- Phase 5: ~1 week (including revision cycles)
- Phase 6: ~0.5–1 week (deployment + initial monitoring)

---

## Out of Scope
- Website chatbot development (documented as Phase 7 for future)
- Outbound calling (reminders, follow-ups — documented as Phase 8 for future)
- Dental practice management software integration (they currently use Google Calendar only)
- Multi-language support (not requested)
- SMS marketing campaigns
- Website redesign or development
- Hardware/phone system replacement (integration with existing system only)

---

## Next Steps

| # | Action Item | Owner | Timeline |
|---|-------------|-------|----------|
| 1 | Send blueprint to Dr. Chen and Maria for review and approval | Inspra AI | Immediately |
| 2 | Schedule kickoff call to confirm platform choice (Vapi vs. Livekit) and agent direction (inbound confirmed) | Inspra AI + Dr. Chen | Within 3 days |
| 3 | Maria to compile: services list, insurance providers, dentist availability, existing phone scripts | Maria (Office Manager) | Within 1 week |
| 4 | Confirm Google Calendar access — share calendar IDs and grant API permissions | Maria / Dr. Chen | Within 1 week |
| 5 | Confirm call routing preferences — overflow only vs. AI-first during peak hours | Dr. Chen | At kickoff call |
| 6 | Inspra to set up voice platform account and begin Phase 1 | Inspra AI | After kickoff |

---

## ROI Tracking Plan
To meet the 3-month ROI expectation:
- **Baseline**: 30% missed calls during peak hours (current state)
- **Target**: <5% missed calls within 30 days of deployment
- **Metrics to track**: Calls handled by AI, appointments booked by AI, calls escalated to human, after-hours calls captured, patient satisfaction (optional survey)
- **Monthly reporting**: Inspra to provide performance report at 30, 60, and 90 days
