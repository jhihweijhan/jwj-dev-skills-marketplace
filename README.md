# split-main-sub-repo-skill

Skill repo for splitting one project into:
- Public child repo: `<project>`
- Private main repo: `<project>-dev`

Includes:
- Standard skill at `skills/split-main-sub-repo`
- Claude marketplace metadata at `.claude-plugin/`

This marketplace is intended to host multiple development-oriented skills over time.

## Install (Claude Code marketplace)
1. `/plugin marketplace add jhihweijhan/split-main-sub-repo-skill`
2. `/plugin install split-main-sub-repo-plugin@jwj-dev-skills-marketplace`

## Install (manual / other agents)
Copy this folder to your agent skills path:
- `skills/split-main-sub-repo`

Common paths:
- `~/.claude/skills/`
- `~/.copilot/skills/`
- `.agents/skills/`
