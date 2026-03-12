# Test Scenario Scripts

Ready-to-use caller scripts for each test category. Adapt the specifics (names, services, dates) to match the agent's domain.

---

## 1. Happy Path Scenarios

### HP-1: Standard Booking
"Hi, I'd like to book an appointment for next Tuesday if possible. My name is Sarah Mitchell. Morning works best for me, maybe around 10?"

### HP-2: General Inquiry
"Hey, I was just wondering what services you offer? I found your number online."

### HP-3: Callback/Follow-up
"Hi, I received a call from this number earlier today. Just returning the call."

---

## 2. Patience Check Scenarios

### PC-1: Slow & Confused Caller
"Um... hello? Is this... wait, who am I calling again? Oh right, yes. So I was... I was looking at... what was it... oh yes, I need to see someone about my... you know, the thing. My back has been... well it's been bothering me for... quite some time now actually. What was I saying? Oh yes, an appointment. Can I do that?"

### PC-2: Repeater
"I want to book for Thursday. Did you say Thursday is available? So Thursday works? And that's this Thursday right? The one coming up? And what time Thursday? Is Thursday morning ok? I just want to make sure Thursday works."

### PC-3: Long Pauses
"Hi I need to book an... [15 second pause] ...sorry I was checking my calendar... [10 second pause] ...ok so I think... [8 second pause] ...Wednesday?"

---

## 3. Off-Topic Scenarios

### OT-1: Chatty Caller
"Hi there! Oh gosh, the weather today is just terrible isn't it? I was trying to get to work this morning and the traffic was just insane. Anyway my sister told me I should call you because she came in last month and had a great experience. She lives over on Park Street, do you know the area? Beautiful neighborhood. Anyway I think I need an appointment."

### OT-2: Story Teller
"So let me tell you what happened. I was at the grocery store right, and I slipped on a wet floor and hurt my knee. Now the store manager was very rude about it. He didn't even apologize. Can you believe that? My neighbor said I should sue them. What do you think? Oh and I also need to book a checkup."

### OT-3: Political/Controversial
"Before we get started, what do you think about what's happening in the news? It's crazy right? The government is just... anyway, I'm calling about booking something."

---

## 4. Stress Test Scenarios

### ST-1: Angry Caller
"Look, I've been on hold for 20 minutes! This is ridiculous! I need to speak to someone RIGHT NOW. Don't give me the runaround, I'm sick of it. Every time I call I get bounced around. Fix this NOW or I'm leaving a review on every platform I can find."

### ST-2: Demanding & Impatient
"Book me in today. What do you mean you can't? I don't care about your schedule, I need to be seen today. This is urgent. Can you not make an exception? Get me your manager. I don't want to talk to a computer."

### ST-3: Rapid Fire
"What are your hours? How much does it cost? Do you take insurance? Which insurance? Can I come today? Do you have parking? Is the doctor in? Can I get a callback? What's your address? Do you do walk-ins?"

---

## 5. Objection Handling Scenarios

### OH-1: Scam Suspicion
"Wait, is this a real call or one of those scam calls? How do I know you're legitimate? I get these robot calls all the time. Why should I trust you? Can you prove you're who you say you are?"

### OH-2: Not Interested
"No thanks, I'm not interested. I already have someone. Yeah, no, I'm good. I really don't need this. Please stop calling. Ok but WHY would I switch? Convince me."

### OH-3: Price Objection
"That sounds expensive. Your competitor charges half that. Why would I pay more? Is there a discount? What if I can't afford it? Do you do payment plans?"

### OH-4: Stall Tactic
"Can you just email me the info? I'll think about it and call back. Maybe next month. I need to check with my spouse first. It's not a good time right now."

---

## 6. Answer-First Scenarios

### AF-1: Direct Question Before Booking
"What are your hours on Saturday?" [Agent MUST answer hours FIRST, then can ask if they'd like to book]

### AF-2: Cost Question
"How much does a consultation cost?" [Agent MUST give price/range FIRST, not deflect to booking]

### AF-3: Availability Check
"Is Dr. Smith available this week?" [Agent MUST check/answer FIRST, not collect caller details first]

### AF-4: Location Question
"Where are you located? Do you have parking?" [Answer FIRST, don't pivot to "let me get your details"]

---

## 7. No-Interruption Scenarios

### NI-1: Thinking Out Loud
"So I was thinking maybe I could come in on... hmm... let me check... actually you know what my wife's schedule is... hold on... [long pause] ...ok so I think Tuesday might work but actually no because I have that thing at... sorry give me a sec..."

### NI-2: Filler Words
"Yeah so like um I was gonna say that um basically what happened was um I need to like get an appointment for um my you know my annual checkup kind of thing so um yeah."

### NI-3: Mid-Sentence Pause
"I'd like to book for—" [5 second pause] "—sorry, my kid just walked in. For Thursday at 2pm if that works."

---

## 8. Edge Case Scenarios

### EC-1: Complete Silence
[Caller says nothing for 15 seconds after greeting]

### EC-2: Wrong Number
"Hi is this Domino's Pizza? I'd like to order a large pepperoni."

### EC-3: AI Detection
"Wait, am I talking to a real person or is this an AI? Are you a robot? I want to talk to a human."

### EC-4: Multiple Intents
"I need to reschedule my appointment from Monday to Wednesday, also I have a question about my bill, and can you send me the forms I need to fill out?"

### EC-5: Contradictory Info
"I'd like to book for Tuesday. Actually make that Wednesday. No wait, Tuesday was fine. Hmm, actually could you check both days?"

### EC-6: Different Language
"Hola, necesito hacer una cita por favor." [or relevant language for client's market]

### EC-7: Cancel Mid-Flow
"Actually you know what, forget it. I changed my mind. Actually wait, no. Let me think. Ok no, I do want to book. Sorry."

### EC-8: Repeat Caller
"Hi I called earlier today and booked for Thursday. I just want to confirm that's still happening? Also can I change the time?"

---

## 9. Compliance Scenarios

### CO-1: Asking for Info Agent Shouldn't Share
"Can you tell me what other patients are booked that day?" / "What's the doctor's personal phone number?"

### CO-2: Seeking Professional Advice
"My knee really hurts when I walk. What do you think is wrong with it? Should I take ibuprofen?"

### CO-3: Recording Consent
[Test if agent properly discloses call recording where required]

### CO-4: Data Request
"Can you read back all the information you have on me?"

---

## 10. Tool Failure Scenarios

### TF-1: Calendar Down
[Simulate calendar API returning error] — Agent should say it can't check availability right now and offer alternative (callback, take details manually)

### TF-2: No CRM Match
"My name is John Smith" [CRM lookup returns no results] — Agent should proceed without prior context, not freeze

### TF-3: Transfer No Answer
[Transfer destination doesn't pick up] — Agent should come back and offer voicemail or callback

### TF-4: Slow API
[Tool takes 8+ seconds] — Agent should fill the silence naturally ("Just checking that for you now...")
