# jwj-dev-skills-marketplace

Language: English | [繁體中文](README.md)

This repository hosts development-focused skills.
The first skill helps split a single project into:
- Public child repo: `<project>`
- Private main repo: `<project>-dev`

## Repository Contents
- Standard skill: `skills/split-main-sub-repo`
- Claude marketplace metadata: `.claude-plugin/`

This marketplace is designed to grow with more development-oriented skills.

## Option 1: Install via Claude Code marketplace
1. `/plugin marketplace add jhihweijhan/jwj-dev-skills-marketplace`
2. `/plugin install split-main-sub-repo-plugin@jwj-dev-skills-marketplace`

## Option 2: Install via `npx skills` (cross-agent)

List available skills in this repo:

```bash
npx -y skills@latest add jhihweijhan/jwj-dev-skills-marketplace -l
```

Install a specific skill to one agent (example: Codex):

```bash
npx -y skills@latest add jhihweijhan/jwj-dev-skills-marketplace --skill split-main-sub-repo --agent codex -y --copy
```

Install to multiple agents:

```bash
npx -y skills@latest add jhihweijhan/jwj-dev-skills-marketplace --skill split-main-sub-repo --agent claude-code --agent codex --agent cursor -y --copy
```

## Important Clarification

`npx skills@latest` does **not** require Claude marketplace metadata.

For `npx skills`, the key requirement is a valid skill structure, typically:
- `skills/<skill-name>/SKILL.md`
- Valid frontmatter in `SKILL.md` (`name`, `description`)
- A reachable Git source (GitHub owner/repo or URL)

So:
- `/plugin ...` flow requires `.claude-plugin/marketplace.json`
- `npx skills ...` flow does not require marketplace metadata, only valid skill structure

## Manual Install (other agents)
Copy `skills/split-main-sub-repo` into your agent skill directory.

Common paths:
- `~/.claude/skills/`
- `~/.copilot/skills/`
- `.agents/skills/`
