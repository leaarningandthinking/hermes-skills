# Anthropic Financial Services Plugins

Official financial industry plugins from https://github.com/anthropics/financial-services

## Installation

```bash
# Clone the repository
mkdir -p ~/.claude/plugins
cd ~/.claude/plugins && git clone https://github.com/anthropics/financial-services.git anthropics-financial-services

# Create symlinks for specific plugins
cd ~/.claude/plugins
ln -s anthropics-financial-services/plugins/vertical-plugins/equity-research equity-research
ln -s anthropics-financial-services/plugins/vertical-plugins/financial-analysis financial-analysis
ln -s anthropics-financial-services/plugins/agent-plugins/market-researcher market-researcher
ln -s anthropics-financial-services/plugins/agent-plugins/model-builder model-builder
```

## Plugin Categories

### Agent Plugins (10个) - 单任务自动化

| 插件名 | 功能描述 | 技能数 |
|--------|----------|--------|
| earnings-reviewer | 财报电话会议+财报 → 模型更新 → 投资笔记 | - |
| gl-reconciler | 找出账目差异，追溯根因，路由审批 | - |
| kyc-screener | 解析开户文档，运行合规规则引擎 | - |
| market-researcher | 行业/主题 → 行业概览、竞争格局、机会清单 | 5 |
| meeting-prep-agent | 客户会议前的简报包准备 | - |
| model-builder | DCF、LBO、三表模型、同行对比 — 直出 Excel | 6 |
| month-end-closer | 应计、滚转、差异分析说明 | - |
| pitch-agent | 同行对比、先例交易、LBO → 品牌化推介材料 | - |
| statement-auditor | 审核 LP 份额对账单（私募基金） | - |
| valuation-reviewer | 接收 GP 材料，运行估值模板，准备 LP 报告 | - |

### Vertical Plugins (7个) - 行业垂直工具包

| 插件名 | 功能描述 | 技能数 |
|--------|----------|--------|
| equity-research | 股票研究：财报分析、首次覆盖报告 | 9 |
| financial-analysis | 财务建模：DCF、同行对比、LBO、三表模型 | 13 |
| fund-admin | 基金运营：GL对账、差异追溯、NAV核对 | - |
| investment-banking | 投行生产力：客户/市场洞察、材料制作 | - |
| operations | 运营流程：KYC文档解析、合规规则评估 | - |
| private-equity | 私募股权：项目发现、CRM集成、创始人触达 | - |
| wealth-management | 财富管理：客户回顾、财务规划、组合分析 | - |

### Partner-built (2个) - 合作伙伴数据源

| 插件名 | 功能描述 | 要求 |
|--------|----------|------|
| lseg | 债券定价、收益率曲线、外汇套利、期权估值 | LSEG 数据订阅 |
| spglobal | 公司快照、财报预告、交易摘要 | S&P 数据订阅 |

## Recommended for A-Share Research

For Chinese A-share investment research, install these 4 plugins:

1. **equity-research** - 股票研究全流程（财报分析、覆盖报告）
2. **financial-analysis** - 通用财务建模（DCF、同行对比、三表模型）
3. **market-researcher** - 行业研究、竞争格局分析
4. **model-builder** - 模型构建（DCF、LBO、三表）

## Skills Included

### equity-research (9 skills)
- catalyst-calendar - 催化剂日历
- earnings-analysis - 财报分析
- earnings-preview - 财报预告
- idea-generation - 想法生成
- initiating-coverage - 首次覆盖报告
- model-update - 模型更新
- morning-note - 早报笔记
- sector-overview - 行业概览
- thesis-tracker - 投资论点跟踪

### financial-analysis (13 skills)
- 3-statement-model - 三表模型
- audit-xls - Excel审计
- clean-data-xls - Excel数据清洗
- competitive-analysis - 竞争分析
- comps-analysis - 同行对比
- dcf-model - DCF估值模型
- deck-refresh - 材料刷新
- ib-check-deck - 投行材料质检
- lbo-model - LBO模型
- ppt-template-creator - PPT模板创建
- pptx-author - PPT制作
- skill-creator - 技能创建
- xlsx-author - Excel制作

### market-researcher (5 skills)
- competitive-analysis - 竞争分析
- comps-analysis - 同行对比
- idea-generation - 想法生成
- pptx-author - PPT制作
- sector-overview - 行业概览

### model-builder (6 skills)
- 3-statement-model - 三表模型
- audit-xls - Excel审计
- comps-analysis - 同行对比
- dcf-model - DCF估值模型
- lbo-model - LBO模型
- xlsx-author - Excel制作

## Data Source Requirements

These skills are designed for institutional data sources:
- **SEC EDGAR** - US stock filings (10-K, 10-Q)
- **Bloomberg/FactSet** - Market data, analyst estimates
- **S&P Global/LSEG** - Partner data (requires subscription)

### Free Data Source Alternative

Use the unified data adapter at:
```
~/.claude/plugins/financial-data-adapter/scripts/financial_data_fetcher.py
```

This provides:
- **A-shares**: AKShare (Sina interface, stable)
- **US stocks**: Yahoo Finance (yfinance)
- **HK stocks**: AKShare

## Usage

```bash
# Load single plugin
claude --plugin-dir ~/.claude/plugins/equity-research

# Load multiple plugins
claude --plugin-dir ~/.claude/plugins/equity-research --plugin-dir ~/.claude/plugins/financial-analysis

# In session, invoke skills
/earnings-analysis
/dcf-model
/sector-overview
```

## Important Notes

1. **Data source mismatch**: These skills assume Bloomberg/FactSet data. For free data sources, modify the data fetching sections to use `financial_data_fetcher.py`.

2. **A-share financial statements**: A-share accounting differs from US GAAP. Financial statement parsing may need adjustment.

3. **Analyst estimates**: Free data sources lack consensus estimates. Some skills may have limited functionality.

4. **Proxy issues**: Oriental Wealth (东方财富) APIs may be blocked by proxies. Use Sina interfaces when possible.
