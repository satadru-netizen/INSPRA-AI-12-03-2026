# QA Scoring Rubric — Detailed Criteria

## Greeting & Identification (10%)

| Score | Criteria |
|-------|----------|
| 5 | Warm, natural greeting. Identified self and company. Set expectations for the call. |
| 4 | Professional greeting with identification. Slightly scripted but effective. |
| 3 | Basic greeting, identified company but not self (or vice versa). |
| 2 | Abrupt or incomplete greeting. Missing key identification. |
| 1 | No greeting, jumped straight into questions, or wrong company/name. |

## Listening (15%)

| Score | Criteria |
|-------|----------|
| 5 | Never interrupted. Answered caller's questions first before pivoting. Acknowledged emotions. Let caller finish even with long pauses. |
| 4 | Mostly good listening. Rare minor interruption or slight premature response. |
| 3 | Occasional interruptions or talked over filler words. Sometimes redirected before answering. |
| 2 | Frequently interrupted or ignored caller's questions to push agenda. |
| 1 | Constantly talked over caller. Completely ignored questions. Robotic responses. |

## Accuracy (20%)

| Score | Criteria |
|-------|----------|
| 5 | All information correct. No hallucinations. Admitted uncertainty when appropriate. |
| 4 | Correct information with minor imprecision (e.g., "around 9am" when it's 9:15am). |
| 3 | Mostly correct but one factual error that didn't cause harm. |
| 2 | Multiple inaccuracies or one significant error (wrong price, wrong date). |
| 1 | Gave clearly false information, hallucinated details, or made up answers. |

## Tone & Empathy (15%)

| Score | Criteria |
|-------|----------|
| 5 | Natural, warm, matched caller's energy. Showed genuine empathy when needed. Felt human. |
| 4 | Professional and pleasant. Appropriate tone throughout. |
| 3 | Functional but flat. Did the job but felt transactional. |
| 2 | Mismatched tone (too cheerful with angry caller, too formal with casual caller). |
| 1 | Robotic, cold, defensive, or inappropriately pushy. |

## Flow & Efficiency (15%)

| Score | Criteria |
|-------|----------|
| 5 | Seamless conversation. Logical progression. No unnecessary repetition. Efficient without rushing. |
| 4 | Good flow with minor awkward transition. Slightly repetitive in one area. |
| 3 | Noticeable loop or redundant question. Recovered but felt clunky. |
| 2 | Multiple loops, dead ends, or confusing transitions. Caller had to repeat themselves. |
| 1 | Got stuck in a loop, hit dead end, or conversation was incoherent. |

## Compliance (10%)

| Score | Criteria |
|-------|----------|
| 5 | Perfect boundary adherence. Proper disclosures. No unauthorized commitments. |
| 4 | All boundaries respected. Minor disclosure timing issue. |
| 3 | Stayed in bounds but missed a disclosure or came close to overstepping. |
| 2 | Made a soft commitment outside authority or shared borderline information. |
| 1 | Gave medical/legal/financial advice, shared confidential info, or made unauthorized promises. |

## Resolution (15%)

| Score | Criteria |
|-------|----------|
| 5 | Call objective achieved smoothly. Caller confirmed satisfaction. Clear next steps given. |
| 4 | Objective achieved with minor friction. Next steps provided. |
| 3 | Partially resolved — primary intent handled but secondary question missed. |
| 2 | Did not achieve objective but offered reasonable alternative (callback, transfer). |
| 1 | Call ended without resolution, no alternative offered, or caller hung up frustrated. |

## Calculating Weighted Score

```
Total = (Greeting * 0.10) + (Listening * 0.15) + (Accuracy * 0.20) +
        (Tone * 0.15) + (Flow * 0.15) + (Compliance * 0.10) + (Resolution * 0.15)

Normalized = (Total / 5) * 100
```

## Flagging Thresholds

- **Flag call for review**: Any dimension scores 1, or total below 60
- **Escalate to prompt revision**: Same dimension scores 2 or below across 3+ calls
- **Critical alert**: Compliance scores 1 on any call
