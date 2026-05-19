---
name: chat-analyze
description: Analyze conversation history, extract insights, summarize discussions, and identify action items from chats. Use when the user needs to analyze past conversations, extract topics, identify decisions, or summarize message history from any channel.
---

# Chat Analyze

Intelligent conversation analysis for extracting insights, summaries, and action items from chat history.

## Features

- **Summarization**: Get concise summaries of long conversations
- **Topic Extraction**: Identify main themes and subjects
- **Action Items**: Pull out todos and commitments
- **Sentiment Analysis**: Understand conversation tone
- **Participant Analysis**: See who said what

## Usage Examples

### Summarize Conversation
```
Summarize yesterday's chat with the team
Give me a summary of our meeting
What did we discuss last week?
```

### Extract Action Items
```
What are the action items from today's discussion?
Extract todos from my chat with Sarah
What commitments did I make?
```

### Analyze Patterns
```
Analyze my message patterns
What topics do I discuss most?
Show me conversation trends
```

## Using the sessions_list Tool

```
# List recent sessions
sessions_list --activeMinutes 60 --limit 20

# Get session history
sessions_history --sessionKey <key> --limit 100
```

## Analysis Script

```bash
# Quick analysis
./scripts/analyze.sh --session <key> --mode summary

# Extract action items
./scripts/analyze.sh --session <key> --mode actions

# Full analysis
./scripts/analyze.sh --session <key> --mode full
```

## Output Formats

### Summary View
- Conversation length
- Key participants
- Main topics
- Key decisions

### Action Items View
- ✅ Completed items
- ⏳ Pending items
- 👤 Assigned to
- 📅 Due dates

## Supported Channels

- WhatsApp
- Telegram
- iMessage
- Discord
- Slack
- Session history
