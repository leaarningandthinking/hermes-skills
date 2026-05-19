---
name: website-competitive-analysis
description: Competitive analysis of websites and web projects. Combines external research (browser, search) with internal code review to avoid false assumptions and provide accurate, actionable recommendations.
version: 1.0.0
---

# Website Competitive Analysis

## When to Use

- User asks to compare their website against competitors
- User wants improvement/optimization suggestions for a web project
- Need to analyze SEO, content strategy, or technical architecture of live sites

## Workflow

### Phase 1: External Research

1. **Identify competitors** — Get URLs from user or search for them
2. **Browse each site** — Use `browser_navigate` + `browser_snapshot` to capture structure, content, features
3. **Search for SEO/traffic intel** — `web_search` with `site:` operators to gauge visibility
4. **Document external findings** — Note positioning, content gaps, design patterns

### Phase 2: Verify Against Actual Code (CRITICAL)

**Before giving final recommendations, always ask for the project code path.**

External observation is frequently wrong:
- Data shown on page may be dynamically updated (e.g., GitHub Stars auto-fetched)
- Features may exist but not be visible in snapshot (e.g., hidden API endpoints, backend integrations)
- SEO tags may be present but not obvious from rendered view
- Content may be hardcoded vs. dynamically generated

5. **Read the actual codebase** — `read_file`, `search_files`, `terminal(find)` to understand:
   - Build/deployment pipeline (GitHub Actions, CI/CD)
   - Data sources and automation scripts
   - Static vs dynamic content generation
   - Actual feature implementations vs. UI placeholders

### Phase 3: Corrected Analysis

6. **Reconcile external vs internal findings** — Explicitly call out what was wrong in initial assumptions
7. **Prioritize by impact/cost** — P0 (zero cost), P1 (low cost), P2 (needs investment)
8. **Differentiation strategy** — Identify what the user has that competitors don't, and vice versa

## Common Pitfalls to Avoid

| Pitfall | Example from Experience |
|---------|------------------------|
| Assuming static data is fake | GitHub Stars were auto-updated via GitHub Actions every 3 days |
| Missing hidden features | WeChat QR float, Q&A API backend, sharing features not visible in initial snapshot |
| Overlooking automation | Cron jobs, data sync scripts, meta update workflows |
| Judging SEO without seeing code | Sitemap, structured data, canonical tags exist but aren't visible on page |
| Recommending features that already exist | Search, subscriptions, community入口 may already be implemented |
| **Missing architecture-level gaps** | Single-page docs vs Docusaurus multi-page (113 articles) is an IA problem, not a content problem |
| **Missing self-hosted vs third-party infra** | Competitor used `res1.own-domain.cn` CDN; user used `ghfast.top` third-party mirror — affects reliability perception |
| **Landing page ≠ docs page parity** | User had region-tabs (GitHub/mirror switcher) on index.html but not on docs.html — patterns fail to propagate |
| **Bugs only visible in code review** | Hamburger menu ID mismatch (`hamburger` vs `sidebarToggle`) and missing CSS classes found by reading source, not browsing |

## Tactics for Documentation Sites Specifically

When comparing documentation pages (common for open-source projects):

1. **Check the install commands first** — These are the highest-traffic, highest-abandonment pages. Are they using domestic mirrors? Do they have copy buttons?
2. **Look for terminology systems** — Good docs sites explain terms inline (tooltips, glossary links). This is a major differentiator for developer tools.
3. **Verify single-page vs multi-page architecture** — Single-page HTML can be fine, but if competitors have 100+ pages with search, you're at a discoverability disadvantage.
4. **Check if landing-page UI patterns propagated to docs** — Often the homepage gets polished but the docs page is forgotten.

## Output Format

1. Competitor comparison matrix
2. User's actual strengths (code-verified)
3. Real weaknesses (not assumed ones)
4. Prioritized recommendations with cost estimates
5. One-line strategic positioning advice
