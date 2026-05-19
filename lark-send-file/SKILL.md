---
name: lark-send-file
version: 1.0.0
description: "飞书发送文件和消息的快捷操作，支持群聊和个人"
---

# 飞书发送文件 Skill

## 快速开始

### 发送文件到群聊
```bash
cd /path/to/your/files
lark-cli im +messages-send --chat-id "oc_xxx" --file "./your-file.md" --as bot
```

### 发送文字消息到群聊
```bash
lark-cli im +messages-send --chat-id "oc_xxx" --text "你的消息内容" --as bot
```

### 完整流程（文件+文字）
```bash
# 1. 先切换到文件所在目录
cd /path/to/your/files

# 2. 发送文件
lark-cli im +messages-send --chat-id "oc_xxx" --file "./your-report.md" --as bot

# 3. 发送文字说明（分开两次发送）
lark-cli im +messages-send --chat-id "oc_xxx" --text "这是报告，请查收" --as bot
```

## 重要规则

1. **身份选择**：
   - 发送文件/消息到群聊必须用 `--as bot`
   - 不能用 `--as user`（会报错：this command only supports: bot）

2. **文件路径**：
   - 必须用**相对路径**，不能用绝对路径
   - 先 `cd` 到文件所在目录，再用 `./filename`

3. **参数组合**：
   - `--file` 和 `--text` / `--markdown` **不能同时用**
   - 需要分两次发送：先发文件，再发文字说明

4. **群聊ID格式**：`oc_` 开头，可在飞书群设置中查到，或运行 `lark-cli im +chats-list --as bot` 列出 bot 所在的所有群

## 常见错误处理

| 错误 | 解决方法 |
|------|----------|
| `--as user is not supported` | 改用 `--as bot` |
| `must be a relative path` | 先cd到文件目录，用相对路径 |
| `cannot be used with --text` | 分两次发送 |
