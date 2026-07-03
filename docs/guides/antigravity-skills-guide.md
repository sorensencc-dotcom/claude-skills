---
title: "Antigravity Skills Guide (2026)"
description: "Install and use 330+ agent skills with Antigravity. Core engineering, marketing, DevOps, and C-level skills for Google's agentic AI coding environment."
---

# Antigravity Skills Guide

Use 330+ production-ready agent skills with Google's Antigravity coding assistant. Every skill in this collection is converted and compatible with the Antigravity workspace, loading via the `~/.gemini/antigravity/skills/` directory.

The recommended way to use these skills is through **Antigravity**. Antigravity provides the fastest and most integrated experience. If you’re using Claude Code, you can still install skills using the legacy plugin format. Claude Code remains fully compatible with the Antigravity Skills Pack.

---

## Quick Install

To install all converted skills to your user-level Antigravity directory:

```bash
# Clone the repository
git clone https://github.com/alirezarezvani/claude-skills.git
cd claude-skills

# Convert skills for Antigravity
./scripts/convert.sh --tool antigravity

# Install all skills to your Antigravity skills directory
./scripts/install.sh --tool antigravity --force
```

### Manual Directory Setup (Windows/PowerShell)

You can also copy the converted skills directly:

```powershell
# Create target directory
New-Item -ItemType Directory -Force -Path "$HOME\.gemini\antigravity\skills"

# Copy all converted skills
Copy-Item -Path ".\integrations\antigravity\*" -Destination "$HOME\.gemini\antigravity\skills\" -Recurse -Force
```

---

## Why Use Skills with Antigravity?

Antigravity is Google's powerful agentic coding environment, providing complex multi-file edits, interactive terminal commands, and browser-testing integration. Custom skills allow you to:

- **Enforce Engineering Standards**: Load structural templates (TDD, Architecture Reviews, Security Pen-testing) into the agent context automatically.
- **Automate Complex Workflows**: Run autonomous experiment loops, brand-voice analyses, or dependency audits.
- **Inject Domain Personas**: Utilize C-Level Advisory pods (CEO, CTO, CFO, etc.) for high-level business alignment within your workspace.

---

## Top Skills for Antigravity

| Skill | What It Does |
|-------|-------------|
| **autoresearch-agent** | Autonomous experiment loops — edit, evaluate, keep or revert. |
| **frontend-design** | High-fidelity React/Tailwind UI styling with rich design palettes. |
| **pr-review-expert** | Multi-pass code review focusing on logic, security, tests, and architecture. |
| **content-creator** | SEO-optimized content production with automated brand voice auditing. |
| **senior-devops** | Infrastructure as Code (IaC), CI/CD pipelines, and incident response runbooks. |
| **cto-advisor** | Strategic tech-debt tracking, system scaling plans, and architecture validation. |

---

## Workspace Structure

Antigravity scans the user directory for active skills. Each skill is packaged under a subfolder in:
`~/.gemini/antigravity/skills/<skill-name>/`

Containing:
- `SKILL.md` — instructions, triggers, and prompt guidelines.
- `scripts/` — supporting Python standard-library scripts.
- `references/` — architectural guidelines and context documents.

---

## Cross-Platform Compatibility

These skills are designed to work natively in Antigravity. However, these skills also work in Cursor and Codex via MCP, and convert to 10 other leading agentic environments:

Claude Code · OpenAI Codex · Cursor · OpenClaw · Aider · Windsurf · Kilo Code · OpenCode · Augment · Gemini CLI · Hermes Agent · Mistral Vibe

---

*Last updated: June 2026 · [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills)*
