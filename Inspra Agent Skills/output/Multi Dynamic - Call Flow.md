# Multi Dynamic Oren Park — Outbound Call Flowchart

**Agent Type**: Outbound (Data Verification & Appointment Booking)
**Direction**: Outbound only (for this pilot)

---

## Call Flow Structure

```
Outgoing Call
    ↓
STEP 1: Opening + AI Disclosure
    "Hi, this is [Agent Name], an AI assistant calling on behalf of
     Megha Poudel from Multi Dynamic Oren Park. This call may be recorded."
    ↓
    ├── Prospect responds positively → Step 2
    ├── "Not a good time" → Capture callback time → Log callback → End
    ├── "Are you AI?" → Confirm AI identity → Continue
    ├── "Don't call me" / "Take me off the list" → Confirm removal → End
    └── Hard no / Hangup → Log disposition (Not Interested) → End
    ↓
STEP 2: Verification
    "Am I speaking with [Name]?"
    "Are you still based in [Suburb]?"
    ↓
    ├── Wrong number / Invalid → Tag as Invalid → End gracefully
    ├── Person confirmed, wrong area (outside core suburbs) →
    │       "Do you have any property in the Oren Park area?"
    │       ├── Yes → Continue to Step 3
    │       └── No → "Do you have plans to buy in the area?"
    │               ├── Yes → Continue to Step 3
    │               └── No → Tag as Out of Area → Referral Ask → End
    └── Person confirmed, in core area → Step 3
    ↓
STEP 3: Discovery / Qualification
    "Are you thinking about buying or selling any property
     within the next twelve months?"
    ↓
    ├── Selling within 3 months → Tag HOT → Step 4 (Offer Appraisal)
    ├── Selling within 6-12 months → Tag WARM → Step 4 (Offer Appraisal)
    ├── Selling beyond 12 months → Tag COLD → Note in CRM → Referral Ask → End
    ├── Buying within 3 months → Tag HOT BUYER → Capture criteria →
    │       Book appointment → Step 5
    ├── Buying within 6-12 months → Tag WARM BUYER → Capture criteria →
    │       Note in CRM → Referral Ask → End
    ├── Buying beyond 12 months → Tag COLD → Note in CRM → Referral Ask → End
    ├── No plans → Tag UNASSEMBLED → Referral Ask → End
    └── Unclear / Needs clarification → Ask one follow-up → Re-categorize
    ↓
STEP 4: The Offer (Free Market Appraisal)
    "Would you be interested in a free market appraisal of your property?
     No obligation at all — it gives you a clear picture of where your
     property sits in today's market."
    ↓
    ├── Yes → Step 5 (Booking)
    ├── "Maybe later" → Tag WARM → Note in CRM → Referral Ask → End
    ├── "Not interested" → Objection handling (one attempt) →
    │       If still no → Tag appropriately → Referral Ask → End
    └── "I already have an agent" → "No worries at all. If anything changes
            or you'd like a second opinion, we're always here." → Referral Ask → End
    ↓
STEP 5: Appointment Booking (Two-Option Method)
    "Would this week or next week suit you better?"
    → [Prospect picks]
    "Would [Day A] or [Day B] work for you?"
    → [Prospect picks]
    "Do you prefer morning or afternoon?"
    → [Prospect picks]
    → Check calendar for available slot → Offer specific time
    → Use book_appointment tool
    → Confirm: "Just to confirm, that's [Day] at [Time] with Megha
       from Multi Dynamic. You'll receive a confirmation shortly."
    ↓
STEP 6: Referral Ask (if not booking)
    "No worries at all. Just one last thing — do you know anyone among
     your family or friends who might be looking to buy or sell?
     We'd love to help them out."
    ├── Yes → Capture name and number → Log referral → Thank and end
    └── No → Thank and end
    ↓
STEP 7: Closing
    ├── Appointment booked → Confirm details, thank by name, end warmly
    ├── Callback requested → Confirm time, "One of our team will call you
    │       shortly" → Log callback → Send notification → End
    ├── Not interested → "Thanks for your time. If anything changes,
    │       Multi Dynamic Oren Park is always here. Have a great day."
    ├── Invalid/disconnected → Tag for removal → End
    └── Voicemail → "Hi, this is a message on behalf of Megha Poudel from
            Multi Dynamic Oren Park. We help local residents with their
            real estate needs. Feel free to reach out anytime. Have a great day."
    ↓
POST-CALL ACTIONS (automated)
    ├── Log call disposition in Vault-Re CRM
    │   (Connected/Not Connected/Invalid/Voicemail)
    ├── Tag lead category (Hot/Warm/Cold/Unassembled)
    ├── Tag intent (Seller/Buyer/Both/None)
    ├── Save call transcript and summary to CRM
    ├── If appointment booked → Create calendar event →
    │       Notify Megha + assigned assistant agent
    ├── If callback requested → Send email notification to team
    ├── If referral captured → Create new contact in CRM
    ├── If valid but not connected → Queue for text message follow-up
    └── If invalid/disconnected (2+ failed attempts) → Flag for removal
```

---

## Objection Handling Paths

```
OBJECTION: "Not interested"
    → "Totally fair. Just out of curiosity — are you thinking about any
       property changes in the next year or so?"
    ├── Engages → Re-enter Discovery (Step 3)
    └── Still no → Referral Ask → End gracefully

OBJECTION: "I already have an agent"
    → "That's great to hear. If anything changes or you'd like a second
       opinion, we're always here."
    → Referral Ask → End

OBJECTION: "Not a good time"
    → "No worries. When's a better time for a quick chat?"
    → Capture callback time → Log callback → End

OBJECTION: "How did you get my number?"
    → "Multi Dynamic reaches out to local residents in the Oren Park area.
       Apologies if the timing's off."
    → Continue if they engage, otherwise end gracefully

OBJECTION: "Don't call me again"
    → Comply immediately → Confirm removal → End call

OBJECTION: "Are you trying to sell me something?"
    → "Not at all — we're just reaching out to local residents to see if
       we can help with any property needs. No pressure at all."
    → Continue if they engage

OBJECTION: "Are you a real person?" / "Are you AI?"
    → "Yeah, I'm an AI assistant calling on behalf of Megha at Multi Dynamic —
       but everything I'm talking about is real."
    → Continue

After 2 genuine attempts at any objection → Let go warmly
```

---

## Tool Triggers

| Point in Flow | Tool | Purpose |
|---------------|------|---------|
| Step 5 (Booking) | `book_appointment` | Check calendar availability, create appointment |
| Step 7 (Callback) | `log_callback` | Log callback request, notify team via email |
| Step 6 (Referral) | `log_referral` | Create new contact record for referred person |
| Post-Call | `log_call_outcome` | Save disposition, category, intent, transcript to Vault-Re |
| Post-Call (not connected) | `send_sms` | Queue text message follow-up for valid but unanswered calls |

---

## Decision Point Summary

| Decision | Condition | Action |
|----------|-----------|--------|
| Valid contact? | Name + suburb confirmed | Continue to discovery |
| In core area? | One of 6 target suburbs | Continue to discovery |
| Outside area with property? | Has property in core area | Continue to discovery |
| Selling intent? | Within 12 months | Tag Hot/Warm/Cold + offer appraisal |
| Buying intent? | Within 12 months | Tag Hot/Warm/Cold + capture criteria |
| Wants appraisal? | Agrees to free market appraisal | Book appointment |
| Callback preferred? | Wants human contact | Log and notify team |
| Disconnected? | 2+ failed call attempts | Flag for removal |
