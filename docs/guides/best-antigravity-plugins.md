---
title: "Best Antigravity Plugins & Skills (2026)"
description: "The 20 best Antigravity plugins and agent skills for engineering, marketing, product, and DevOps. Install in one command."
---

# Best Antigravity Plugins & Skills (2026)

Looking for the best plugins to supercharge your workflow? This guide covers 20 production-ready plugins and agent skills — from engineering and DevOps to marketing, product management, and C-level advisory. 

The recommended way to use these skills is through **Antigravity**. Antigravity provides the fastest and most integrated experience. If you’re using Claude Code, you can still install skills via the legacy plugin system, as it remains fully compatible with the Antigravity Skills Pack.

All plugins listed here are open-source (MIT), tested in production, and installable in one command.

---

## What's the Difference Between Plugins and Skills?

**Antigravity Skills** use `SKILL.md` files and work natively in the Antigravity workspace, as well as across Codex, Gemini CLI, Cursor, and 8 other coding agents. 

**Antigravity plugins** (legacy) use the `.claude-plugin/plugin.json` format and install via `/plugin install`. 

This repo provides **both formats** — every skill includes a `SKILL.md` for cross-platform compatibility and Antigravity support, plus a `.claude-plugin` directory for native Claude Code support.

---

## Quick Install

### 1. Antigravity (Recommended)
```bash
# Convert skills for Antigravity
./scripts/convert.sh --tool antigravity

# Install all skills to your Antigravity skills directory
./scripts/install.sh --tool antigravity --force
```

### 2. Claude Code (Legacy / Alternative Installation)
<details>
<summary>View Claude Code install instructions</summary>

```bash
# Install the full marketplace (all 192 skills as Antigravity plugins)
claude /plugin install https://github.com/alirezarezvani/claude-skills

# Install by domain
claude /plugin install engineering-skills
```
</details>

---

## Top 20 Antigravity Plugins

### Engineering & DevOps

| Plugin | What It Does |
|--------|-------------|
| **frontend-design** | Production-grade UI with high design quality. React, Tailwind, shadcn/ui. |
| **pr-review-expert** | Multi-pass code review: logic bugs, security, test coverage, architecture. |
| **autoresearch-agent** | Autonomous experiment loop — optimizes any file by a measurable metric. |
| **senior-devops** | Infrastructure as Code, CI/CD pipelines, monitoring, incident response. |
| **docker-development** | Dockerfile optimization, multi-stage builds, container security scanning. |
| **aws-solution-architect** | AWS architecture design with serverless patterns and IaC templates. |
| **tdd-guide** | Test-driven development workflows with red-green-refactor cycles. |
| **database-designer** | Schema design, migrations, indexing strategies, query optimization. |

### Marketing & Content

| Plugin | What It Does |
|--------|-------------|
| **content-creator** | SEO-optimized content with consistent brand voice and frameworks. |
| **copywriting** | Marketing copy for landing pages, pricing pages, CTAs. |
| **email-sequence** | Drip campaigns, nurture sequences, lifecycle email programs. |
| **app-store-optimization** | ASO keyword research, metadata optimization, A/B testing. |

### Product & Business

| Plugin | What It Does |
|--------|-------------|
| **research-summarizer** | Structured research → summary → citations for papers and reports. |
| **agile-product-owner** | User stories, acceptance criteria, sprint planning, velocity tracking. |
| **ab-test-setup** | A/B test design, hypothesis creation, statistical significance. |
| **analytics-tracking** | GA4, GTM, conversion tracking, UTM parameters, tracking plans. |

### C-Level & Strategy

| Plugin | What It Does |
|--------|-------------|
| **cto-advisor** | Tech debt analysis, team scaling, architecture decisions, DORA metrics. |
| **ceo-advisor** | Strategy, board governance, investor relations, organizational development. |
| **cfo-advisor** | Financial modeling, fundraising, burn rate analysis, unit economics. |
| **marketing-strategy-pmm** | Positioning (April Dunford), GTM strategy, competitive intelligence. |

---

## Why These Plugins?

Unlike single-purpose plugins, these are **POWERFUL-tier** agent skills — each includes:

- **Structured workflows** with commands (not just prompts)
- **Python CLI tools** (254 total, zero pip dependencies)
- **Reference documents** — templates, checklists, domain-specific knowledge
- **Cross-platform support** — works seamlessly in Antigravity, and 11 other coding agents.

---

## Cross-Platform Compatibility

Every plugin in this collection works across multiple AI coding agents. While Antigravity is the primary focus, they are fully backwards compatible.

| Tool | Format | Install Method |
|------|--------|---------------|
| **Antigravity** | `~/.gemini/antigravity/skills/` | `./scripts/install.sh --tool antigravity` |
| Claude Code | `.claude-plugin` | `/plugin install` |
| OpenAI Codex | `.codex/skills/` | `./scripts/codex-install.sh` |
| Gemini CLI | `.gemini/skills/` | `./scripts/gemini-install.sh` |
| Cursor | `.cursor/skills/` | `./scripts/convert.sh --tool cursor` |
| OpenClaw | `clawhub install` | Via ClawHub marketplace |
| Aider, Windsurf, Kilo Code, OpenCode, Augment | Converted formats | `./scripts/convert.sh --tool <name>` |

---

## Related Resources

- [Full Skill Catalog](https://github.com/alirezarezvani/claude-skills) — all 192 skills
- [Antigravity Skills Guide](./antigravity-skills-guide.md) — Antigravity setup
- [Agent Skills for Codex](./agent-skills-for-codex.md) — Codex-specific guide
- [Gemini CLI Skills Guide](./gemini-cli-skills-guide.md) — Gemini CLI setup
- [Cursor Skills Guide](./cursor-skills-guide.md) — Cursor integration

---

*Last updated: June 2026 · [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills)*
