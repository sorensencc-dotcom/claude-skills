# Antigravity Skills & Plugins — Agent Skills for Every Coding Tool

**313 production-ready Antigravity skills, plugins, and agent skills for 12 AI coding tools.**

The most comprehensive open-source library of agent plugins — built first and foremost for **Antigravity**. It also works seamlessly with OpenAI Codex, Gemini CLI, Cursor, and 7 more coding agents. Reusable expertise packages covering engineering, DevOps, marketing (incl. v2.7.3 AEO — Answer Engine Optimization for LLM citation), security (PreToolUse hooks), compliance, C-level advisory (incl. founder-mode CFO/CMO/CRO/CPO/COO/CHRO/CISO/GC/CDO/CAIO/CCO/VPE personas + 21 /cs:* slash commands), productivity (capture/email/reflect), and a complete research stack (litreview/grants/dossier/patent/syllabus/pulse/notebooklm + hybrid router).

**Works with:** Antigravity · Claude Code · OpenAI Codex · Gemini CLI · OpenClaw · Hermes Agent[^hermes] · Mistral Vibe[^vibe] · Cursor · Aider · Windsurf · Kilo Code · OpenCode · Augment

[^hermes]: Hermes Agent is **BYO-sync tier**: the repo ships a pre-generated `.hermes/skills/claude-skills/` tree (305 skills across 12 domains as of v2.7.3), but you run `python scripts/sync-hermes-skills.py` once locally to install into `~/.hermes/skills/`. Uses the same agentskills.io SKILL.md standard — no format conversion.
[^vibe]: Mistral Vibe is also **BYO-sync tier**: the repo ships a pre-generated `.vibe/skills/claude-skills/` tree (306 skills across 14 domains), run `./scripts/vibe-install.sh` once locally to install into `~/.vibe/skills/`. Same agentskills.io SKILL.md standard — no format conversion. Docs: <https://docs.mistral.ai/mistral-vibe/agents-skills>.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Skills](https://img.shields.io/badge/Skills-330-brightgreen?style=for-the-badge)](#skills-overview)
[![Agents](https://img.shields.io/badge/Agents-49+-blue?style=for-the-badge)](#agents)
[![Personas](https://img.shields.io/badge/Personas-7-purple?style=for-the-badge)](#personas)
[![Commands](https://img.shields.io/badge/Commands-79+-orange?style=for-the-badge)](#commands)
[![Stars](https://img.shields.io/github/stars/alirezarezvani/claude-skills?style=for-the-badge)](https://github.com/alirezarezvani/claude-skills/stargazers)
[![SkillCheck Validated](https://img.shields.io/badge/SkillCheck-Validated-4c1?style=for-the-badge)](https://getskillcheck.com)

> **5,200+ GitHub stars** — the most comprehensive open-source Antigravity skills & agent plugins library (formerly Claude Code Skills).

---

## What Are Antigravity Skills & Agent Plugins?

Antigravity skills (also called agent skills or coding agent plugins) are modular instruction packages that give AI coding agents domain expertise they don't have out of the box. Each skill includes:

- **SKILL.md** — structured instructions, workflows, and decision frameworks
- **Python tools** — ~402 CLI scripts (all stdlib-only, zero pip installs)
- **Reference docs** — templates, checklists, and domain-specific knowledge

**One repo, twelve platforms.** The recommended way to use these skills is through Antigravity. Antigravity provides the fastest and most integrated experience. However, it still works natively as Antigravity plugins, Codex agent skills, Gemini CLI skills, Hermes Agent skills, Mistral Vibe skills, and converts to 7 more tools via `scripts/convert.sh`. All ~402 Python tools run anywhere Python runs.

### Skills vs Agents vs Personas

| | Skills | Agents | Personas |
|---|---|---|---|
| **Purpose** | How to execute a task | What task to do | Who is thinking |
| **Scope** | Single domain | Single domain | Cross-domain |
| **Voice** | Neutral | Professional | Personality-driven |
| **Example** | "Follow these steps for SEO" | "Run a security audit" | "Think like a startup CTO" |

All three work together. See [Orchestration](#orchestration) for how to combine them.

---

## Quick Install

### 1. Antigravity (Recommended)

```bash
# Clone the repository
git clone https://github.com/alirezarezvani/claude-skills.git
cd claude-skills

# Convert and install skills
./scripts/convert.sh --tool antigravity
./scripts/install.sh --tool antigravity --force
```

Skills install to `~/.gemini/antigravity/skills/`.

### 2. Claude Code (Legacy Installation)

<details>
<summary>View instructions for Claude Code</summary>

If you’re using Claude Code, you can still install skills using the legacy plugin system. Claude Code remains fully compatible with the Antigravity Skills Pack.

```bash
# Add the marketplace
/plugin marketplace add alirezarezvani/claude-skills

# Install by domain
/plugin install engineering-skills@claude-code-skills          # 24 core engineering
/plugin install engineering-advanced-skills@claude-code-skills  # 25 POWERFUL-tier
/plugin install product-skills@claude-code-skills               # 12 product skills
```
</details>

### 3. Cursor

These skills also work in Cursor via MCP.

```bash
# Clone the repository
git clone https://github.com/alirezarezvani/claude-skills.git
cd claude-skills

# Convert and install skills
./scripts/convert.sh --tool cursor
./scripts/install.sh --tool cursor --target /path/to/project
```

### 4. OpenAI Codex

These skills also work in Codex via MCP.

```bash
npx agent-skills-cli add alirezarezvani/claude-skills --agent codex
# Or: git clone + ./scripts/codex-install.sh
```

### 5. Gemini CLI

```bash
# Clone the repository
git clone https://github.com/alirezarezvani/claude-skills.git
cd claude-skills

# Run the setup script
./scripts/gemini-install.sh
```

---

## Multi-Tool Support (New)

**Convert all 156 skills to 7 AI coding tools** with a single script:

| Tool | Format | Install |
|------|--------|---------|
| **Antigravity** | `~/.gemini/antigravity/skills/` | `./scripts/install.sh --tool antigravity` |
| **Cursor** | `.mdc` rules | `./scripts/install.sh --tool cursor --target .` |
| **Aider** | `CONVENTIONS.md` | `./scripts/install.sh --tool aider --target .` |
| **Kilo Code** | `.kilocode/rules/` | `./scripts/install.sh --tool kilocode --target .` |
| **Windsurf** | `.windsurf/skills/` | `./scripts/install.sh --tool windsurf --target .` |
| **OpenCode** | `.opencode/skills/` | `./scripts/install.sh --tool opencode --target .` |
| **Augment** | `.augment/rules/` | `./scripts/install.sh --tool augment --target .` |
| **Hermes Agent** | `~/.hermes/skills/` | `python scripts/sync-hermes-skills.py --verbose` |
| **Mistral Vibe** | `~/.vibe/skills/` | `./scripts/vibe-install.sh` |

**How it works:**

```bash
# 1. Convert all skills to all tools (takes ~15 seconds)
./scripts/convert.sh --tool all

# 2. Install into your project (with confirmation)
./scripts/install.sh --tool cursor --target /path/to/project

# Or use --force to skip confirmation:
./scripts/install.sh --tool aider --target . --force
```

---

## Skills Overview

**313 skills across 12 domains:**

| Domain | Skills | Highlights | Details |
|--------|--------|------------|---------|
| **🔧 Engineering — Core** | 32 | Architecture, frontend, backend, fullstack, QA, DevOps, SecOps, AI/ML, data, Playwright, self-improving agent, security suite (6), a11y audit | [engineering-team/](engineering-team/) |
| **🎭 Playwright Pro** | 9+3 | Test generation, flaky fix, Cypress/Selenium migration, TestRail, BrowserStack, 55 templates | [engineering-team/playwright-pro](engineering-team/playwright-pro/) |
| **🧠 Self-Improving Agent** | 5+2 | Auto-memory curation, pattern promotion, skill extraction, memory health | [engineering-team/self-improving-agent](engineering-team/self-improving-agent/) |
| **⚡ Engineering — POWERFUL** | 45 | Agent designer, RAG architect, database designer, CI/CD builder, security auditor, MCP builder, AgentHub, Helm charts, Terraform, self-eval, llm-wiki, tc-tracker, **reliability portfolio** (feature-flags-architect, kubernetes-operator, chaos-engineering, slo-architect), ship-gate, **security-guidance** (✨v2.7.3 — PreToolUse hook catching 12 anti-patterns), **Matt Pocock skills** (write-a-skill, caveman, grill-me, handoff, grill-with-docs) | [engineering/](engineering/) |
| **🎯 Product** | 13 | Product manager, agile PO, strategist, UX researcher, UI design, landing pages, SaaS scaffolder, analytics, experiment designer, discovery, roadmap communicator, code-to-prd, apple-hig-expert | [product-team/](product-team/) |
| **📣 Marketing** | 45 | 8 pods: Content (8), SEO + AEO (6 incl. ✨v2.7.3 `aeo` — E-E-A-T audit, citation tracking across 5 LLMs), CRO (6), Channels (6), Growth (4), Intelligence (4), Sales (2) + context foundation + orchestration router. 58 Python tools. | [marketing-skill/](marketing-skill/) |
| **🚀 Productivity** ✨v2.8.4 | 6 | `capture` (brain-dump-to-action), `email` pair (inbox-setup + inbox-triage with 7-file KB contract), `reflect` (light-prompt journal), **`handoff`** (Matt Pocock-inspired: first-run setup, redaction linter, SessionStart + SessionEnd hooks, fidelity self-check, `--refresh`), **`andreessen`** (✨v2.8.4 — market-first decision & productivity mode: market > team > product, PMF-first, 3x5-card + Anti-Todo, fixed anti-sycophancy operating prompt). Path-B from megaprompts 05-08 + Matt Pocock + Andreessen derivation. | [productivity/](productivity/) |
| **📋 Project Management** | 9 | Senior PM, scrum master, Jira, Confluence, Atlassian admin, templates + bundled Atlassian Remote MCP | [project-management/](project-management/) |
| **🏥 Regulatory & QM** | 14 | ISO 13485, MDR 2017/745, FDA, ISO 27001, GDPR, SOC 2, CAPA, risk management | [ra-qm-team/](ra-qm-team/) |
| **💼 C-Level Advisory** | 28 | Full C-suite (10 roles) + orchestration + board meetings + culture & collaboration | [c-level-advisor/](c-level-advisor/) |
| **📈 Business & Growth** | 5 | Customer success, sales engineer, revenue ops, contracts & proposals, BizDev toolkit | [business-growth/](business-growth/) |
| **💰 Finance** | 3 | Financial analyst (DCF, budgeting, forecasting), SaaS metrics coach, business investment advisor | [finance/](finance/) |

---

## 🔒 Skill Security Auditor

New in v2.0.0 — audit any skill for security risks before installation:

```bash
python3 engineering/skill-security-auditor/scripts/skill_security_auditor.py /path/to/skill/
```

Scans for: command injection, code execution, data exfiltration, prompt injection, dependency supply chain risks, privilege escalation. Returns **PASS / WARN / FAIL** with remediation guidance.

**Zero dependencies.** Works anywhere Python runs.

---

## Python Analysis Tools

~402 CLI tools ship with the skills (all verified, stdlib-only):

```bash
# SaaS health check
python3 finance/saas-metrics-coach/scripts/metrics_calculator.py --mrr 80000 --customers 200 --churned 3 --json

# Brand voice analysis
python3 marketing-skill/content-production/scripts/brand_voice_analyzer.py article.txt

# Tech debt scoring
python3 c-level-advisor/cto-advisor/scripts/tech_debt_analyzer.py /path/to/codebase
```

---

## FAQ

**How do I install plugins?**
Antigravity is the recommended environment. Run `./scripts/convert.sh --tool antigravity` then `./scripts/install.sh --tool antigravity --force` to convert and install all skills. The files are installed directly to the global user profile scope (`~/.gemini/antigravity/skills/`).

**Does this still work with Claude Code?**
Yes, Claude Code remains fully compatible via the legacy plugin system. Add the marketplace with `/plugin marketplace add alirezarezvani/claude-skills`, then install any skill bundle with `/plugin install <name>@claude-code-skills`.

**Do these skills work with OpenAI Codex / Cursor / Windsurf / Aider / Mistral Vibe?**
Yes. Skills work natively with 13 tools: Antigravity, Claude Code, OpenAI Codex, Gemini CLI, OpenClaw, Hermes Agent, Mistral Vibe, Cursor, Aider, Windsurf, Kilo Code, OpenCode, and Augment.

**Will updating break my installation?**
No. We follow semantic versioning and maintain backward compatibility within patch releases. Existing script arguments, plugin source paths, and SKILL.md structures are never changed in patch versions. See the [CHANGELOG](CHANGELOG.md) for details on each release.

---

## License

MIT — see [LICENSE](LICENSE) for details.

---

**Built by [Alireza Rezvani](https://alirezarezvani.com)** · [Medium](https://alirezarezvani.medium.com) · [Twitter](https://twitter.com/nginitycloud)
