#!/usr/bin/env bash

# Quick Capture Script
# Fast idea logging to memory, notes, or tasks

set -e

CONTENT=""
DEST="memory"
TAG=""
TIME=$(date +"%Y-%m-%d %H:%M")
WORKSPACE="$HOME/.openclaw/workspace"

print_usage() {
    cat <<'EOF'
Usage: ./capture.sh "content" [options]

Destinations:
  --to memory    Save to memory/YYYY-MM-DD.md (default)
  --to daily     Save to today's daily note
  --to tasks     Create a task/todo
  --to <file>    Save to specific file

Options:
  --tag <tag>    Add a tag/label
  --time <time>  Override timestamp

Examples:
  ./capture.sh "Great idea for app" --to memory --tag app
  ./capture.sh "Call dentist" --to tasks --tag urgent
  ./capture.sh "Link: design.com" --to daily

EOF
}

if [[ $# -eq 0 ]]; then
    print_usage
    exit 0
fi

CONTENT="$1"
shift

while [[ $# -gt 0 ]]; do
    case $1 in
        --to)
            DEST="$2"
            shift 2
            ;;
        --tag)
            TAG="$2"
            shift 2
            ;;
        --time)
            TIME="$2"
            shift 2
            ;;
        *)
            shift
            ;;
    esac
done

# Create memory directory if needed
mkdir -p "$WORKSPACE/memory"

# Build entry
ENTRY="## [$TIME]"
[[ -n "$TAG" ]] && ENTRY="$ENTRY #$TAG"
ENTRY="$ENTRY
$CONTENT
"

# Save to destination
case $DEST in
    memory)
        FILE="$WORKSPACE/memory/$(date +%Y-%m-%d).md"
        echo "$ENTRY" >> "$FILE"
        echo "✅ Captured to memory: $FILE"
        ;;
    daily)
        FILE="$WORKSPACE/daily/$(date +%Y-%m-%d).md"
        mkdir -p "$WORKSPACE/daily"
        echo "$ENTRY" >> "$FILE"
        echo "✅ Captured to daily: $FILE"
        ;;
    tasks)
        echo "📝 Task captured: $CONTENT"
        echo "   Tag: ${TAG:-none}"
        ;;
    tasks|reminders)
        echo "📝 Task captured: $CONTENT"
        echo "   Use: remindctl or things CLI to add"
        ;;
    *)
        if [[ -f "$DEST" ]] || [[ -d "$(dirname "$DEST" 2>/dev/null)" ]]; then
            echo "$ENTRY" >> "$DEST"
            echo "✅ Captured to: $DEST"
        else
            echo "❌ Invalid destination: $DEST"
            exit 1
        fi
        ;;
esac

echo ""
echo "Time: $TIME"
[[ -n "$TAG" ]] && echo "Tag: $TAG"
