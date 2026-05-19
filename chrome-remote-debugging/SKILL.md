---
name: chrome-remote-debugging
description: Chrome remote debugging setup on macOS for browser automation. Documents limitations, failed approaches, and working alternatives.
version: 1.0.0
author: Hermes Agent
platforms: [macos]
metadata:
  hermes:
    tags: [chrome, browser, debugging, automation, x-twitter]
---

# Chrome 远程调试（macOS）

为浏览器自动化工具提供对已登录 Chrome 会话的 CDP 访问。

## 目标

连接到用户已登录的 Chrome（如已登录 X/Twitter），避免重新登录。

## 已验证的失败方案

### 1. open -a 方式
```bash
open -a "Google Chrome" --args --remote-debugging-port=9222
```
**结果：** 参数未正确传递到主进程。Chrome 启动了但 9222 端口无监听。

### 2. 直接命令行启动（默认 profile）
```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --remote-debugging-port=9222
```
**报错：** `DevTools remote debugging requires a non-default data directory. Specify this using --user-data-dir.`

### 3. 指定默认 profile 路径
```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --remote-debugging-port=9222 \
  --user-data-dir="$HOME/Library/Application Support/Google/Chrome"
```
**结果：** 仍然报同样的错误。Chrome 检测到默认 profile 路径并拒绝。

### 4. 复制 profile 到临时目录
将 Cookies、Login Data 等复制到 `/tmp/chrome-debug-profile`，再用 `--user-data-dir` 指向它。
**结果：** 命令被系统阻止（BLOCKED），且复制过程中文件可能被锁。

## 核心结论

macOS 上 Chrome 对默认 profile 开启远程调试有硬限制。这是安全设计，无法绕过。

## 可行替代方案

### 方案 A：使用 Hermes 内置浏览器工具
- 内置 browser_navigate 工具有独立浏览器引擎
- 首次需用户手动登录目标网站
- 之后可通过 browser 工具操作
- **优点：** 简单、稳定、无需配置
- **缺点：** 需要重新登录，不共享 Chrome cookies

### 方案 B：通过 Cookie 导入登录状态
1. 从 Chrome 导出目标网站的 cookies（使用 EditThisCookie 扩展或手动提取）
2. 在浏览器工具中注入 cookies
3. 刷新页面即可保持登录状态

### 方案 C：使用 x-cli + X API（针对 X/Twitter）
- 需要 X Developer 账号和 API 凭证
- 有费用（基础计划 $100/月）
- 见 `xitter` skill

### 方案 D：Playwright 保持状态
```bash
# 首次登录后保存状态
npx playwright codegen --save-storage=auth.json https://x.com

# 后续使用保存的状态
npx playwright open --load-storage=auth.json https://x.com
```
**注意：** Playwright 的存储与 Chrome profile 不互通。

## 推荐

- **简单场景（偶尔发个推）：** 方案 A，用内置浏览器工具，手动登录一次
- **频繁自动化：** 方案 C（x-cli + API），最稳定
- **需要保持 Chrome 登录状态：** 目前无完美方案

## 相关 Skill
- `xitter`：X/Twitter API 交互（需付费 API 凭证）
