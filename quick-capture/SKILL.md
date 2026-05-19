---
name: quick-capture
description: Quick capture assistant for saving ideas, notes, and observations. Use when the user wants to quickly save thoughts, capture ideas, log observations, or add items to their knowledge base without interrupting workflow.
---

# Quick Capture

Fast idea capture system for saving thoughts without breaking flow.

## Supported Destinations

- **Memory**: Save to MEMORY.md or daily notes
- **Notes**: Apple Notes, Obsidian, or other note apps
- **Tasks**: Things, Reminders, or todo lists
- **Files**: Save to specific project files

## Quick Capture Patterns

### Ideas & Thoughts
```
Capture: "AI agent should have personality preferences"
Quick save: "Remember to check email at 3pm"
Note this: "Meeting with Sarah next Tuesday"
```

### Links & Resources
```
Save this link: https://example.com/article
Bookmark: "Python async patterns"
Resource: "Great design system reference"
```

### Action Items
```
Todo: "Fix the login bug before release"
Task: "Schedule dentist appointment"
Action item: "Send proposal to client"
```

## Capture Format

Automatically adds:
- Timestamp
- Context tags
- Source reference

## Script Usage

```bash
# Quick capture with automatic categorization
./scripts/capture.sh "Your idea here" --tag important --to memory

# Capture to specific destination
./scripts/capture.sh "Meeting notes" --to daily --time now
```

## Destinations

| Destination | Command | File |
|-------------|---------|------|
| Memory | `--to memory` | `memory/YYYY-MM-DD.md` |
| Daily | `--to daily` | Today's daily note |
| Tasks | `--to tasks` | Things/Reminders |
| Specific | `--to <file>` | Custom file path |
