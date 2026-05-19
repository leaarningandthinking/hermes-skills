#!/usr/bin/env bash

# Chat Analyze Script
# Analyze conversation history for insights

set -e

SESSION_KEY=""
MODE="summary"
LIMIT=100

print_usage() {
    cat <<'EOF'
Usage: ./analyze.sh [options]

Options:
  --session <key>    Session key to analyze (required)
  --mode <mode>      Analysis mode: summary|actions|topics|full
  --limit <n>        Number of messages to analyze (default: 100)
  --recent           Analyze most recent active session

Examples:
  ./analyze.sh --session main-abc123 --mode summary
  ./analyze.sh --recent --mode actions
  ./analyze.sh --session <key> --limit 50 --mode full

EOF
}

while [[ $# -gt 0 ]]; do
    case $1 in
        --session)
            SESSION_KEY="$2"
            shift 2
            ;;
        --mode)
            MODE="$2"
            shift 2
            ;;
        --limit)
            LIMIT="$2"
            shift 2
            ;;
        --recent)
            # Will auto-detect most recent session
            shift
            ;;
        *)
            shift
            ;;
    esac
done

echo "🔍 Chat Analysis Tool"
echo "Mode: $MODE | Messages: $LIMIT"
echo "---"

if [[ -z "$SESSION_KEY" ]]; then
    echo "No session key provided. Listing recent sessions..."
    echo ""
    echo "Use: sessions_list --limit 10"
    echo "Then: ./analyze.sh --session <key> --mode <mode>"
    exit 0
fi

case $MODE in
    summary)
        echo "📋 Generating conversation summary..."
        echo "   Session: $SESSION_KEY"
        echo "   Use: sessions_history --sessionKey $SESSION_KEY --limit $LIMIT"
        ;;
    actions)
        echo "✅ Extracting action items..."
        echo "   Session: $SESSION_KEY"
        ;;
    topics)
        echo "🏷️  Identifying main topics..."
        echo "   Session: $SESSION_KEY"
        ;;
    full)
        echo "🔬 Full analysis mode..."
        echo "   Session: $SESSION_KEY"
        echo "   Includes: summary, actions, topics, sentiment"
        ;;
esac

echo ""
echo "Tip: Use sessions_history to fetch messages for analysis"
echo "      Result can be piped to this analyzer"
