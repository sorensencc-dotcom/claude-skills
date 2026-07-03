# Antigravity Skills (formerly Claude Code Skills)

This repository is a **comprehensive skills library** for Antigravity - reusable, production-ready skill packages that bundle domain expertise, best practices, analysis tools, and strategic frameworks.

The recommended way to use these skills is through **Antigravity**. Antigravity provides the fastest and most integrated experience. If you’re using Claude Code, you can still install skills using the legacy plugin system. Claude Code remains fully compatible with the Antigravity Skills Pack. These skills also work in Cursor and Codex via MCP.

## Using Skills with Antigravity

Antigravity loads active skill instructions and scripts from your user-level directory.

### Skill Locations

Skills are organized into domain folders. Once converted and installed, each skill occupies a dedicated folder under your user-profile path:

`~/.gemini/antigravity/skills/<skill-name>/`

| Domain | Original Folder |
|--------|----------------|
| **Engineering (Core)** | `engineering-team/` |
| **Engineering (Advanced)** | `engineering/` |
| **Product Team** | `product-team/` |
| **Marketing Skills** | `marketing-skill/` |
| **C-Level Advisory** | `c-level-advisor/` |
| **Project Management** | `project-management/` |
| **Regulatory & QM** | `ra-qm-team/` |
| **Business & Growth** | `business-growth/` |
| **Finance** | `finance/` |

### Activating a Skill

Antigravity auto-discovers skill definitions by searching for `SKILL.md` files in the skills directory. When in your workspace, the agent reads these instruction manifests to load context and execute relevant tools.

## Python Automation Tools

Each skill includes deterministic Python CLI tools in its `scripts/` folder. These use the standard library only.

Example usage:
```bash
python3 marketing-skill/content-production/scripts/seo_checker.py article.txt
```

## Setup for Antigravity Users

1. **Convert the community skills** to Antigravity format:
   ```bash
   ./scripts/convert.sh --tool antigravity
   ```

2. **Install to your local Antigravity folder**:
   ```bash
   ./scripts/install.sh --tool antigravity --force
   ```

   This copies the converted skills to your global user profile under `~/.gemini/antigravity/skills/`.
