# Multi Dynamic — Vapi Platform Configuration Fixes

These are structural fixes that cannot be solved by prompt engineering alone. They address recurring issues found across V7–V12 live call testing.

---

## 1. Transcriber — Switch to Deepgram Nova-2 with Keyword Boosting

**Current issue:** STT garbles critical phrases — "DNC list" → "real cities", "Oran Park" → "Orrin Park" / "Rampart" / "Elrond Park"

**Fix:**
- Confirm the assistant is using **Deepgram Nova-2** (per project guidelines)
- Enable **keyword boosting** with the following terms:

```json
{
  "transcriber": {
    "provider": "deepgram",
    "model": "nova-2",
    "keywords": [
      "DNC:2",
      "do not call:2",
      "Oran Park:3",
      "Multi Dynamic:2",
      "Catherine Field:2",
      "Coviti:2",
      "Harrington Park:2",
      "Gregory Hills:2",
      "Gladstone Hill:2",
      "remove my number:2",
      "take me off:2",
      "harassment:2",
      "market appraisal:1"
    ],
    "language": "en-AU"
  }
}
```

Set `language` to `en-AU` (Australian English) to improve accent recognition.

---

## 2. Blocked Token — Suppress "Goodbye" After Closing

**Current issue:** Agent says "Goodbye" after closing message or DNC confirmation despite prompt-level prohibition (persisted across V8–V12).

**Fix:** Add `"Goodbye"` to the model's stop sequences or use Vapi's response filtering:

```json
{
  "model": {
    "messages": [...],
    "toolIds": [...],
    "stop": ["Goodbye", "Bye", "Goodbye.", "Bye."]
  }
}
```

Alternatively, if Vapi supports post-processing hooks, strip any trailing farewell tokens from the assistant's response before TTS.

---

## 3. Pre-End-Call Hook — DNC Confirmation Check

**Current issue:** Agent calls end_call without confirming DNC removal — prospect never hears their number will be removed.

**Fix:** Add a server-side validation in the Vapi server URL (webhook) that intercepts the `end_call` tool call and checks:

```
IF call transcript contains DNC signals (fuzzy match)
AND assistant's last message does NOT contain "removed from our list"
THEN:
  - Block end_call
  - Inject message: "I'll make sure your number is removed from our list."
  - Then allow end_call to proceed
```

Implementation approach — in the Vapi server URL handler:

```javascript
// In your Vapi server URL webhook handler
if (request.message.type === 'tool-calls') {
  const endCall = request.message.toolCalls.find(t => t.function.name === 'end_call');
  if (endCall) {
    const transcript = request.message.transcript;
    const isDNC = detectDNCSignal(transcript); // fuzzy match function
    const lastAssistantMsg = getLastAssistantMessage(transcript);
    const hasConfirmation = lastAssistantMsg.includes('removed from our list');

    if (isDNC && !hasConfirmation) {
      // Force the confirmation before allowing end_call
      return {
        results: [{
          toolCallId: endCall.id,
          result: 'BLOCKED: DNC confirmation required. Say the removal confirmation first.'
        }]
      };
    }
  }
}
```

---

## 4. Fuzzy DNC Detection — Server-Side Logic

**Current issue:** STT garbles DNC phrases, so prompt-level trigger matching fails.

**Fix:** Add a fuzzy DNC detection function in your server URL handler:

```javascript
function detectDNCSignal(transcript) {
  const userMessages = transcript
    .filter(m => m.role === 'user')
    .map(m => m.content.toLowerCase());

  const fullText = userMessages.join(' ');

  // Keyword clusters — if 2+ from different groups appear, flag as DNC
  const removalWords = ['remove', 'delete', 'take off', 'take me off', 'get rid'];
  const targetWords = ['number', 'my number', 'phone', 'contact'];
  const listWords = ['list', 'database', 'system', 'records', 'dnc', 'do not call'];
  const hostileWords = ['shouldn\'t call', 'not supposed', 'stop calling', 'harassment',
                         'harassing', 'why calling', 'why are you calling', 'shouldn\'t have called'];

  const hasRemoval = removalWords.some(w => fullText.includes(w));
  const hasTarget = targetWords.some(w => fullText.includes(w));
  const hasList = listWords.some(w => fullText.includes(w));
  const hasHostile = hostileWords.some(w => fullText.includes(w));

  // DNC if: explicit removal request OR hostile + list/removal mention
  return (hasRemoval && (hasTarget || hasList)) ||
         (hasHostile && (hasTarget || hasList || hasRemoval));
}
```

---

## 5. Required Tool Chain — Force log_call_outcome Before end_call

**Current issue:** Agent sometimes calls end_call without log_call_outcome, meaning the call outcome is never saved to CRM.

**Fix:** In Vapi assistant configuration, make `log_call_outcome` a prerequisite for `end_call`:

Option A — Server-side enforcement:
```javascript
if (request.message.type === 'tool-calls') {
  const endCall = request.message.toolCalls.find(t => t.function.name === 'end_call');
  const logOutcome = request.message.toolCalls.find(t => t.function.name === 'log_call_outcome');

  if (endCall && !logOutcome && !hasLoggedOutcomeThisCall) {
    return {
      results: [{
        toolCallId: endCall.id,
        result: 'BLOCKED: You must call log_call_outcome before end_call.'
      }]
    };
  }
}
```

Option B — In the `end_call` tool description, add:
```
"This tool will fail if log_call_outcome has not been called first."
```

---

## Summary of Platform Fixes

| Fix | Layer | Addresses |
|-----|-------|-----------|
| Deepgram Nova-2 + keyword boosting + en-AU | Transcriber | STT garbling of DNC phrases and suburb names |
| Stop sequences for "Goodbye" | Model config | Persistent farewell after closing |
| Pre-end-call DNC confirmation hook | Server URL | Agent ending call without confirming removal |
| Fuzzy DNC detection | Server URL | STT garbling preventing DNC pattern matching |
| Required log_call_outcome before end_call | Server URL | Missing CRM logging |
