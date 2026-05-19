---
name: claude-code-auth-troubleshoot
description: 排查 Claude Code 认证问题 - 当用户想用 Claude Pro 订阅但系统走 API 计费时使用
trigger: 用户报告 Claude Code 使用 API 而非订阅，或想删除 API key 配置
---

# Claude Code 认证问题排查

## 问题表现
- 用户有 Claude Pro 订阅，但 Claude Code 走 API 计费
- 用户想删除 API key，永久使用订阅

## 排查步骤

### 1. 检查当前认证状态
```bash
claude auth status
```
- `authMethod: oauth_token` → OAuth 订阅
- `authMethod: api_key` → API key
- `apiProvider: firstParty` → 官方
- `apiProvider: thirdParty` → 第三方（Bedrock/Vertex 等）

### 2. 检查环境变量（最常见问题）
```bash
env | grep -i ANTHROPIC
grep -i ANTHROPIC ~/.zshrc ~/.bashrc ~/.bash_profile 2>/dev/null
```

**关键环境变量**（会覆盖 OAuth）：
- `ANTHROPIC_API_KEY` - API 密钥
- `ANTHROPIC_AUTH_TOKEN` - 认证令牌
- `ANTHROPIC_BASE_URL` - API 端点（如 `https://openrouter.ai/api`）

### 3. 检查钥匙串（macOS）
```bash
security find-generic-password -s "claude-code-anthropic-api-key" 2>&1
security find-generic-password -s "CLAUDE_CODE_ANTHROPIC_API_KEY" 2>&1
```

### 4. 检查配置文件
```bash
cat ~/.claude/settings.json
cat ~/Library/Application\ Support/Claude/config.json
```

## 解决方案

### 删除环境变量（最常见）
```bash
# 备份
cp ~/.zshrc ~/.zshrc.backup.$(date +%Y%m%d%H%M%S)

# 删除 ANTHROPIC 相关配置
sed -i '' '/^export ANTHROPIC_BASE_URL=/d; /^export ANTHROPIC_AUTH_TOKEN=/d; /^export ANTHROPIC_API_KEY=/d' ~/.zshrc

# 清除当前 shell 的环境变量
unset ANTHROPIC_API_KEY ANTHROPIC_AUTH_TOKEN ANTHROPIC_BASE_URL
```

### 重新加载配置
```bash
source ~/.zshrc
# 或关闭终端重新打开
```

### 验证结果
```bash
claude auth status
# 应显示 authMethod: oauth_token, apiProvider: firstParty
```

## 常见场景

| 场景 | 原因 | 解决方案 |
|------|------|----------|
| 用了 OpenRouter | ~/.zshrc 里配置了 ANTHROPIC_BASE_URL | 删除环境变量 |
| 之前配置过 API key | 环境变量残留 | 删除环境变量 |
| 想切换回订阅 | API key 优先级高于 OAuth | 删除所有 API 配置 |

## 注意事项
- 环境变量优先级：env > keychain > OAuth
- 删除配置后需要新开终端或 source 配置文件
- 当前 shell session 可能有残留，需要 unset 或重启终端
