# TencentDB Agent Memory Plugin

Four-layer memory system for OpenClaw/Hermes that auto-captures, structures, and profiles conversational knowledge.

## Installation

```bash
# Install with exact version (required)
openclaw plugins install @tencentdb-agent-memory/memory-tencentdb@0.3.4

# If security scan blocks due to symlink issues:
rm -rf ~/.openclaw/npm/node_modules/@openclaw/feishu/node_modules/.openclaw-*
openclaw plugins install @tencentdb-agent-memory/memory-tencentdb@0.3.4

# Restart gateway
openclaw gateway restart
```

## Pitfalls

1. **Exact version required** — `openclaw plugins install @tencentdb-agent-memory/memory-tencentdb` (without version) will fail with "unsupported npm spec". Must use `@0.3.4` or specific version.

2. **Symlink security block** — If feishu plugin has stale temp symlinks, security scan blocks installation. Clean with: `rm -rf ~/.openclaw/npm/node_modules/@openclaw/feishu/node_modules/.openclaw-*`

3. **Config format** — NOT in `plugins.entries`. Use root-level key:
   ```json
   {
     "memory-tencentdb": {
       "enabled": true
     }
   }
   ```

## Architecture

- **L0 Conversation** — Raw dialogue (stored in SQLite)
- **L1 Atom** — Structured facts (extracted via LLM)
- **L2 Scenario** — Scene blocks (aggregated from atoms)
- **L3 Persona** — User profile (distilled from scenarios)

## Data Directory

```
~/.openclaw/memory-tdai/
├── persona.md           # User profile (L3)
├── scenarios/           # Scene blocks (L2)
├── atoms.db             # Atomic memories (L1)
└── conversations/       # Raw dialogue (L0)
```

## Configuration

### Basic (zero-config, SQLite backend)

```json
{
  "memory-tencentdb": {
    "enabled": true
  }
}
```

### Enable short-term compression (Context Offload)

```json
{
  "memory-tencentdb": {
    "enabled": true,
    "config": {
      "offload": {
        "enabled": true
      }
    }
  }
}
```

### Full configuration options

| Field | Default | Description |
|-------|---------|-------------|
| `storeBackend` | `"sqlite"` | Storage backend: `sqlite` or `tcvdb` (Tencent Cloud) |
| `recall.strategy` | `"hybrid"` | Recall: `keyword`, `embedding`, `hybrid` (RRF fusion) |
| `recall.maxResults` | `5` | Items returned per recall |
| `pipeline.everyNConversations` | `5` | L1 extraction trigger interval |
| `extraction.maxMemoriesPerSession` | `20` | Max memories per L1 pass |
| `persona.triggerEveryN` | `50` | Persona generation trigger |
| `offload.enabled` | `false` | Short-term compression |

## Agent Tools

- `tdai_memory_search` — Search memories
- `tdai_conversation_search` — Search conversation history

## Performance

Per Tencent benchmarks:
- Token usage: up to **61.38% reduction**
- Pass rate: **51.52% relative improvement**
- Persona accuracy: **48% → 76%**

## Source

- GitHub: https://github.com/Tencent/TencentDB-Agent-Memory
- npm: `@tencentdb-agent-memory/memory-tencentdb`
- Version: 0.3.4 (as of 2026-05)
