# Voice Agent Model Selection Guide

## LLM Options

| Model | Best For | Latency | Notes |
|-------|----------|---------|-------|
| GPT-4o | General purpose, balanced | ~300ms | Default choice for most projects |
| GPT-4o-mini | Cost-sensitive, simple flows | ~200ms | Good for high-volume outbound |
| Claude Sonnet 4.6 | Complex reasoning, nuanced conversations | ~400ms | Better at following complex rules |
| Claude Haiku 4.5 | Fast + capable | ~250ms | Good middle ground |

## Voice Options

Match voice to brand personality:

| Tone | Recommended Voices | Use Case |
|------|-------------------|----------|
| Professional & warm | Cartesia - British Female, ElevenLabs - Rachel | Medical, legal, finance |
| Friendly & energetic | ElevenLabs - Josh, Cartesia - American Male | Sales, recruitment |
| Calm & patient | Deepgram - Asteria, ElevenLabs - Elli | Support, reception |
| Authoritative | ElevenLabs - Adam, Cartesia - British Male | B2B, enterprise |

Always test voice with actual scripts before committing — some voices handle domain terms better than others.

## Transcriber Options

| Transcriber | Best For | Notes |
|-------------|----------|-------|
| Deepgram Nova-2 | Default — English, fast, accurate | Best price/performance |
| Deepgram Nova-2 Medical | Healthcare terminology | Use for clinics, hospitals |
| Talkscriber | Multilingual | When callers switch languages |

## Configuration Defaults

```
silenceTimeoutSeconds: 30
maxDurationSeconds: 600 (10 min)
backgroundSound: office (inbound) / none (outbound)
voicemailDetection: enabled (outbound only)
endCallPhrases: ["goodbye", "have a great day", "talk soon"]
```

Adjust per project — appointment booking calls may need longer max duration, support calls need longer silence timeout for lookup pauses.
