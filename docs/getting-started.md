---
title: Install Agent Skills — Antigravity, Codex, Gemini Setup
description: "How to install 330 Antigravity skills and agent plugins for 13 AI coding tools. Step-by-step setup for Antigravity, Claude Code, OpenAI Codex, Gemini CLI, Hermes Agent, Mistral Vibe, OpenClaw, Cursor, Aider, Windsurf, and more."
---

# Getting Started

## Installation

Choose your platform and follow the steps:

=== "Antigravity"

    The recommended way to use these skills is through **Antigravity**. Antigravity provides the fastest and most integrated experience.

    ```bash
    git clone https://github.com/alirezarezvani/claude-skills.git
    cd claude-skills
    ./scripts/convert.sh --tool antigravity
    ./scripts/install.sh --tool antigravity
    ```

=== "Claude Code"

    <details>
    <summary>Legacy / Alternative Installation for Claude Code</summary>
    
    If you’re using Claude Code, you can still install skills using the legacy plugin system. Claude Code remains fully compatible with the Antigravity Skills Pack.

    <ol class="install-steps">
      <li>
        <strong>Add the marketplace</strong>
        <pre><code>/plugin marketplace add alirezarezvani/claude-skills</code></pre>
      </li>
      <li>
        <strong>Install the skills you need</strong>
        <pre><code>/plugin install engineering-skills@claude-code-skills</code></pre>
      </li>
    </ol>
    </details>

=== "Cursor"

    These skills also work in Cursor and Codex via MCP.
    ```bash
    git clone https://github.com/alirezarezvani/claude-skills.git
    cd claude-skills
    ./scripts/convert.sh --tool cursor
    ./scripts/install.sh --tool cursor --target /path/to/project
    ```

=== "OpenAI Codex"

    These skills also work in Cursor and Codex via MCP.
    ```bash
    npx agent-skills-cli add alirezarezvani/claude-skills --agent codex
    ```
    Or clone and install manually:
    ```bash
    git clone https://github.com/alirezarezvani/claude-skills.git
    ./scripts/codex-install.sh
    ```

=== "Gemini CLI"

    ```bash
    git clone https://github.com/alirezarezvani/claude-skills.git
    ./scripts/gemini-install.sh
    ```
    Or use the sync script to generate the skills index:
    ```bash
    python3 scripts/sync-gemini-skills.py
    ```

=== "OpenClaw"

    ```bash
    bash <(curl -s https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/scripts/openclaw-install.sh)
    ```

=== "Hermes Agent"

    [Hermes Agent](https://github.com/NousResearch/hermes-agent) uses the same agentskills.io SKILL.md standard — no format conversion needed.

    ```bash
    git clone https://github.com/alirezarezvani/claude-skills.git
    cd claude-skills
    python scripts/sync-hermes-skills.py --verbose
    ```

=== "Mistral Vibe"

    [Mistral Vibe](https://github.com/mistralai/mistral-vibe) uses the same agentskills.io SKILL.md standard — no format conversion needed.

    ```bash
    git clone https://github.com/alirezarezvani/claude-skills.git
    cd claude-skills
    ./scripts/vibe-install.sh
    ```

=== "Aider"

    ```bash
    git clone https://github.com/alirezarezvani/claude-skills.git
    cd claude-skills
    ./scripts/convert.sh --tool aider
    ./scripts/install.sh --tool aider --target /path/to/project
    ```

=== "Windsurf"

    ```bash
    git clone https://github.com/alirezarezvani/claude-skills.git
    cd claude-skills
    ./scripts/convert.sh --tool windsurf
    ./scripts/install.sh --tool windsurf --target /path/to/project
    ```

=== "Kilo Code"

    ```bash
    git clone https://github.com/alirezarezvani/claude-skills.git
    cd claude-skills
    ./scripts/convert.sh --tool kilocode
    ./scripts/install.sh --tool kilocode --target /path/to/project
    ```

=== "OpenCode"

    ```bash
    git clone https://github.com/alirezarezvani/claude-skills.git
    cd claude-skills
    ./scripts/convert.sh --tool opencode
    ./scripts/install.sh --tool opencode --target /path/to/project
    ```

=== "Augment"

    ```bash
    git clone https://github.com/alirezarezvani/claude-skills.git
    cd claude-skills
    ./scripts/convert.sh --tool augment
    ./scripts/install.sh --tool augment --target /path/to/project
    ```

=== "Manual"

    ```bash
    git clone https://github.com/alirezarezvani/claude-skills.git
    # Copy any skill folder to ~/.gemini/antigravity/skills/
    ```

!!! tip "All 7 tools at once"
    Convert for every supported tool in one command:
    ```bash
    ./scripts/convert.sh --tool all
    ```
    See the [Multi-Tool Integrations](integrations.md) page for detailed per-tool documentation.

<hr class="section-divider">

## Available Bundles

| Bundle | Install Command | Skills |
|--------|----------------|--------|
| **Engineering Core** | `/plugin install engineering-skills@claude-code-skills` | 37 |
| **Engineering POWERFUL** | `/plugin install engineering-advanced-skills@claude-code-skills` | 43 |
| **Product** | `/plugin install product-skills@claude-code-skills` | 15 |
| **Marketing** | `/plugin install marketing-skills@claude-code-skills` | 44 |
| **Regulatory & Quality** | `/plugin install ra-qm-skills@claude-code-skills` | 14 |
| **Project Management** | `/plugin install pm-skills@claude-code-skills` | 9 |
| **C-Level Advisory** | `/plugin install c-level-skills@claude-code-skills` | 34 |
| **Business & Growth** | `/plugin install business-growth-skills@claude-code-skills` | 5 |
| **Finance** | `/plugin install finance-skills@claude-code-skills` | 4 |

Or install individual skills: `/plugin install skill-name@claude-code-skills`

<hr class="section-divider">

## Usage

### Commands

```
/pw:generate     Generate Playwright tests
/pw:fix          Fix flaky test failures
/si:review       Review auto-memory health
/cs:board        Trigger a C-suite board meeting
```

### Contextual Prompts

```
Using the senior-architect skill, review our microservices
architecture and identify the top 3 scalability risks.
```

<hr class="section-divider">

## Python Tools

All 359 tools use the standard library only — zero pip installs, all verified.

```bash
# Security audit a skill before installing
python3 engineering/skill-security-auditor/scripts/skill_security_auditor.py /path/to/skill/

# Analyze brand voice
python3 marketing-skill/content-production/scripts/brand_voice_analyzer.py article.txt
```

<hr class="section-divider">

## Security

!!! warning "Always audit untrusted skills"

    Before installing skills from third-party sources, run the security auditor:

    ```bash
    python3 engineering/skill-security-auditor/scripts/skill_security_auditor.py /path/to/skill/
    ```

    Returns **PASS** / **WARN** / **FAIL** with remediation guidance. Scans for command injection, data exfiltration, prompt injection, and supply chain risks.

<hr class="section-divider">

## Creating Your Own

Each skill is a folder:

```
my-skill/
  SKILL.md       # Instructions + workflows
  scripts/       # Python CLI tools (optional)
  references/    # Domain knowledge (optional)
  assets/        # Templates (optional)
```

<hr class="section-divider">

## FAQ

??? question "Do I need API keys?"
    No. Skills work locally with no external API calls. All Python tools use stdlib only.

??? question "Can I install individual skills instead of bundles?"
    Yes. Use `/plugin install skill-name@claude-code-skills` for any single skill, or copy individual folders if using Antigravity.

??? question "Does this work with Antigravity?"
    Yes! Antigravity is the recommended environment. Run `./scripts/convert.sh --tool antigravity` then `./scripts/install.sh --tool antigravity --force` to convert and install all skills. The files are installed directly to the global user profile scope (`~/.gemini/antigravity/skills/`).

??? question "Does this work with Cursor, Windsurf, Aider, or other tools?"
    Yes. All 330 skills can be converted to native formats for Cursor, Aider, Kilo Code, Windsurf, OpenCode, Augment, and Antigravity. Run `./scripts/convert.sh --tool all` and then install with `./scripts/install.sh --tool <name>`. See [Multi-Tool Integrations](integrations.md) for details.

??? question "Can I use Agent Skills in ChatGPT?"
    Yes. We have [6 Custom GPTs](custom-gpts.md) that bring Agent Skills directly into ChatGPT — no installation needed. Just click and start chatting.
