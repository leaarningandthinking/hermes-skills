---
name: xfyun-astron-coding-plan
description: 配置讯飞星辰 Astron Coding Plan 到 AI 编程工具（Qwen Code、Claude Code 等）
trigger: 当用户需要配置讯飞星火/xfyun/astron API 到编程工具时
---

# 讯飞星辰 Astron Coding Plan 配置指南

## 关键信息

| 参数 | 值 |
|------|-----|
| OpenAI 协议 Base URL | `https://maas-coding-api.cn-huabei-1.xf-yun.com/v2` |
| Anthropic 协议 Base URL | `https://maas-coding-api.cn-huabei-1.xf-yun.com/anthropic` |
| 模型 ID | `astron-code-latest` |

## 重要提示

**优先使用 Anthropic 协议！** 讯飞的 OpenAI 兼容接口存在格式兼容问题：
- 错误：`message[0].content[1] has invalid field(s): type`
- 原因：讯飞 OpenAI 协议不支持标准 OpenAI 消息格式的某些字段（如 content type 字段）
- 解决：使用 Anthropic 协议，讯飞官方文档也推荐此方案

## Qwen Code 配置

配置文件路径：`~/.qwen/settings.json`

```json
{
  "env": {
    "XFYUN_ANTHROPIC_API_KEY": "你的API Key"
  },
  "modelProviders": {
    "anthropic": [
      {
        "id": "astron-code-latest",
        "name": "Astron Code (讯飞星火)",
        "description": "讯飞星火 Astron Code 模型 - Anthropic 协议",
        "envKey": "XFYUN_ANTHROPIC_API_KEY",
        "baseUrl": "https://maas-coding-api.cn-huabei-1.xf-yun.com/anthropic",
        "generationConfig": {
          "timeout": 600000,
          "maxRetries": 3,
          "contextWindowSize": 92160,
          "samplingParams": {
            "temperature": 0.7,
            "max_tokens": 32768
          }
        }
      }
    ]
  }
}
```

## Claude Code 配置

配置文件路径：`~/.claude/settings.json`

```json
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "你的API Key",
    "ANTHROPIC_BASE_URL": "https://maas-coding-api.cn-huabei-1.xf-yun.com/anthropic",
    "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": 1,
    "API_TIMEOUT_MS": 600000,
    "ANTHROPIC_MODEL": "astron-code-latest",
    "ANTHROPIC_SMALL_FAST_MODEL": "astron-code-latest"
  },
  "permissions": {
    "allow": [],
    "deny": []
  }
}
```

## API Key 获取

1. 访问 [讯飞星辰 MaaS 平台套餐订阅页面](https://maas.xfyun.cn/packageSubscription)
2. 购买套餐后复制 Coding Plan **专属 API Key**
3. 每个套餐对应一个独立 API Key

## 套餐说明

| 套餐 | 价格 | 限制 |
|------|------|------|
| 无忧版 | ¥3.9/月首购 | 请求次数不限 |
| 专业版 | ¥39/月 | 每5小时约1200次请求 |
| 高效版 | ¥199/月 | 每5小时约6000次请求 |

## 常见错误

| 错误 | 原因 | 解决 |
|------|------|------|
| `message[0].content[1] has invalid field(s): type` | OpenAI 协议格式不兼容 | 改用 Anthropic 协议 |
| 401 无效身份验证 | API Key 或 URL 错误 | 检查 Key 来源和 Base URL |
| 429 请求超限 | 套餐额度用尽 | 等待刷新或升级套餐 |

## 官方文档

- [Astron Coding Plan 使用文档](https://www.xfyun.cn/doc/spark/CodingPlan.html)
- [套餐订阅页面](https://maas.xfyun.cn/packageSubscription)
