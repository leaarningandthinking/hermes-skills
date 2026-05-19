#!/usr/bin/env bash

# Smart Remind Script
# Quick reminder setup helper

set -e

print_usage() {
    cat <<'EOF'
Usage: ./remind.sh <time> <message> [options]

Examples:
  ./remind.sh "in 30 minutes" "Call Mom"
  ./remind.sh "tomorrow 9am" "Weekly standup"
  ./remind.sh "2024-02-10 14:00" "Doctor appointment" --repeat weekly

Options:
  --repeat daily|weekly|monthly  Set recurring reminder
  --channel <channel>            Target channel (default: current)
  --list                         List active reminders
  --cancel <id>                  Cancel reminder by ID

EOF
}

if [[ $# -eq 0 ]]; then
    print_usage
    exit 0
fi

TIME="$1"
MESSAGE="$2"
REPEAT=""
ACTION="create"

while [[ $# -gt 2 ]]; do
    case $3 in
        --repeat)
            REPEAT="$4"
            shift 2
            ;;
        --list)
            ACTION="list"
            shift
            ;;
        --cancel)
            ACTION="cancel"
            shift 2
            ;;
        *)
            shift
            ;;
    esac
done

case $ACTION in
    create)
        echo "⏰ Setting reminder: $MESSAGE"
        echo "   Time: $TIME"
        [[ -n "$REPEAT" ]] && echo "   Repeat: $REPEAT"
        echo ""
        echo "The OpenClaw cron system will handle scheduling."
        echo "Use: cron add with appropriate schedule settings"
        ;;
    list)
        echo "📋 Active reminders:"
        echo "Use: cron list"
        ;;
    cancel)
        echo "❌ Canceling reminder"
        echo "Use: cron remove <jobId>"
        ;;
esac
