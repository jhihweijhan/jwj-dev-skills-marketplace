# jwj-dev-skills-marketplace

Skill repo for splitting one project into:
- Public child repo: `<project>`
- Private main repo: `<project>-dev`

Includes:
- Standard skill at `skills/split-main-sub-repo`
- Claude marketplace metadata at `.claude-plugin/`

This marketplace is intended to host multiple development-oriented skills over time.

## Install (Claude Code marketplace)
1. `/plugin marketplace add jhihweijhan/jwj-dev-skills-marketplace`
2. `/plugin install split-main-sub-repo-plugin@jwj-dev-skills-marketplace`

## Install (`npx skills`, cross-agent)

List available skills in this repo:

```bash
npx -y skills@latest add jhihweijhan/jwj-dev-skills-marketplace -l
```

Install this skill to a specific agent (example: Codex):

```bash
npx -y skills@latest add jhihweijhan/jwj-dev-skills-marketplace --skill split-main-sub-repo --agent codex -y --copy
```

Install to multiple agents:

```bash
npx -y skills@latest add jhihweijhan/jwj-dev-skills-marketplace --skill split-main-sub-repo --agent claude-code --agent codex --agent cursor -y --copy
```

## Important Clarification

`npx skills@latest` does **not** require Claude marketplace files.

What it needs is a skill repo with valid skill structure, typically:
- `skills/<skill-name>/SKILL.md`
- Valid frontmatter in `SKILL.md` (`name`, `description`)
- Publicly reachable Git source (GitHub owner/repo or URL)

So:
- For `/plugin ...` flow: need `.claude-plugin/marketplace.json`
- For `npx skills ...` flow: marketplace metadata is optional; valid skill structure is the key

## Install (manual / other agents)
Copy this folder to your agent skills path:
- `skills/split-main-sub-repo`

Common paths:
- `~/.claude/skills/`
- `~/.copilot/skills/`
- `.agents/skills/`
