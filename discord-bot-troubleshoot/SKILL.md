---
title: Discord Bot 消息无响应排查
name: discord-bot-troubleshoot
version: 1.0.0
description: >
  排查 Discord Bot 已上线但 @mention/普通消息无响应的系统化流程。
  覆盖日志分析、API 权限检查、Gateway Intents 配置。
---

# Discord Bot 消息无响应排查

## 触发条件
- Bot 显示在线（绿点）
- 斜杠命令（`/skill`）正常
- 但 @mention 普通消息无响应
- 日志中没有任何 `on_message` 或消息处理记录

## 排查步骤

### 1. 确认 Bot 已经连接 Gateway
检查日志中是否有：
```
Shard ID None has connected to Gateway
[Discord] Connected as XXX
```
如果没有，先解决连接问题。

### 2. 检查日志中是否有消息事件
如果日志里只有斜杠命令注册，没有任何消息处理记录，说明 Bot 收不到消息事件。
这通常是 **Message Content Intent 未开启**或**权限不足**。

### 3. 开启 Message Content Intent（最常见原因）
Discord 2022 年起强制要求 Bot 必须开含这个 Intent 才能读取消息内容。
1. 打开 https://discord.com/developers/applications
2. 找到你的应用 → 左侧点 **Bot**
3. 翻到 **Privileged Gateway Intents**
4. 开含三项：
   - [x] Presence Intent
   - [x] Server Members Intent
   - [x] **Message Content Intent** ← 关键
5. 点 Save Changes
6. 重启 Hermes Gateway: `hermes gateway run --replace`

### 4. 检查 Bot 在服务器的角色权限
用 Discord API 检查 Bot 成员权限：
```python
import requests
headers = {"Authorization": f"Bot {TOKEN}"}
r = requests.get(f"https://discord.com/api/v10/guilds/{GUILD_ID}/members/{BOT_ID}", headers=headers)
roles = r.json()["roles"]
```
关键权限字段：
- `READ_MESSAGE_HISTORY` (1 << 13) — 必须有，否则看不到消息
- `VIEW_CHANNEL` (1 << 10) — 必须有
- `SEND_MESSAGES` (1 << 11) — 必须有

如果缺少 READ_MESSAGE_HISTORY，在 Discord 服务器设置 → 角色 → Bot 角色 中开启。

### 5. 检查频道级别权限覆盖
某些频道可能有单独的权限覆盖拒绝了 Bot。
右键频道 → 编辑频道 → 权限 → 确认 Bot 有：
- 查看频道 ✅
- 发送消息 ✅
- 读取消息历史 ✅

## 常见疑问
**Q: 斜杠命令正常，为什么消息不响应？**
A: 斜杠命令走的是交互回调接口，不需要读取消息内容。普通消息需要 Message Content Intent 和读取消息权限。

**Q: 开了 Intent 为什么还不行？**
A: 开了 Intent 后必须重启 Gateway。Hermes 重启后 Discord 会重新协商 Gateway 连接参数。

## 验证
修复后，在频道里 @mention Bot，检查日志是否出现消息处理记录：
```
hermes logs --profile <profile> | grep -i message
```
