# Skill Installation Sources

Quick reference for installing common community skills that aren't in the official Hermes hub.

## Browser Automation Skills

| Skill | Correct Install Command | Notes |
|-------|------------------------|-------|
| web-access | `hermes skills install https://raw.githubusercontent.com/eze-is/web-access/main/SKILL.md` | RAG-based web content retrieval |
| agent-browser | `npm i -g agent-browser && agent-browser install` | CDP-based browser automation CLI |
| browser-use | `hermes skills install skills.sh/browser-use` | Playwright-based browser automation |

## Installation Format Reference

1. **skills.sh registry**: `hermes skills install skills.sh/<skill-name>`
2. **GitHub direct URL**: `hermes skills install https://raw.githubusercontent.com/<org>/<repo>/main/SKILL.md`
3. **npm packages**: Some skills require `npm i -g <package>` first

## Vercel Skills CLI (Different Ecosystem)

Vercel Labs maintains a separate Skills CLI (`npx skills`) for their agent skills ecosystem. These are NOT Hermes skills — they're a different package manager.

| Skill | Install Command | Notes |
|-------|----------------|-------|
| find-skills | `npx skills add vercel-labs/skills@find-skills -g -y` | Skill discovery helper |
| Other Vercel skills | `npx skills add vercel-labs/agent-skills@<skill-name>` | React, Next.js, design skills |

Key commands:
- `npx skills find [query]` — Search for skills
- `npx skills add <package>` — Install a skill
- `npx skills check` — Check for updates

Browse at: https://skills.sh/

## Troubleshooting

If `hermes skills install <name>` fails:
1. Try `hermes skills search <name>` to find the correct source
2. Check if the skill requires npm/pip installation first
3. Look for the skill on https://skills.sh
4. Search GitHub for `<skill-name> SKILL.md`
5. If it's a Vercel skill, use `npx skills add` instead of `hermes skills install`

## Fetching SKILL.md Content

To get skill details before adding to a showcase/documentation:
```bash
curl -sL "https://raw.githubusercontent.com/<org>/<repo>/main/skills/<skill-name>/SKILL.md"
```

This returns the full SKILL.md content which can be parsed for name, description, and usage instructions.
