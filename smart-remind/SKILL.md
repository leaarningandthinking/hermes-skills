---
name: smart-remind
description: Smart reminder and scheduling assistant using OpenClaw's cron system. Use when the user needs to set reminders, schedule tasks, create recurring alerts, or manage timed notifications.
---

# Smart Remind

Intelligent reminder system integrated with OpenClaw's cron scheduler for precise, reliable notifications.

## Features

- **One-time Reminders**: "Remind me in 20 minutes"
- **Scheduled Tasks**: "Remind me tomorrow at 9am"
- **Recurring Alerts**: "Every Monday morning"
- **Context-aware**: Reminders include conversation context
- **Multi-channel Delivery**: Can send to chat, phone, etc.

## Usage Examples

### One-time Reminders
```
Remind me in 30 minutes to call Mom
Set a reminder for 3pm to take medicine
Alert me in 2 hours about the meeting
```

### Scheduled Reminders
```
Remind me tomorrow at 8am to check emails
Set reminder for Friday 6pm
At 9:00 tomorrow, remind me about the deadline
```

### Recurring Reminders
```
Every weekday at 8am, remind me to drink water
Remind me every Monday at 9am for weekly standup
Daily at 10pm, remind me to review my day
```

## Cron Job Creation

When setting a reminder, use the `cron` tool:

```json
{
  "schedule": { "kind": "at", "at": "2024-02-08T15:30:00" },
  "payload": { "kind": "systemEvent", "text": "Reminder: Call Mom" },
  "sessionTarget": "main"
}
```

## Best Practices

- Include context in reminder text (what and why)
- Set appropriate time gaps for follow-ups
- Use "iso" parameter with continuous sync for periodic checks
- Progressive disclosure for different reminder types

## Scripts

Use `./scripts/remind.sh` for batch reminder operations or quick setup.
