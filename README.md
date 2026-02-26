# jwj-dev-skills-marketplace

這個倉庫提供開發向 skills，首個 skill 用於將單一專案拆分為：
- 公開子倉：`<project>`
- 私有主倉：`<project>-dev`

## 倉庫內容
- 標準 skill：`skills/split-main-sub-repo`
- Claude marketplace 設定：`.claude-plugin/`

此 marketplace 後續會持續加入更多開發向 skills。

## 安裝方式一：Claude Code marketplace
1. `/plugin marketplace add jhihweijhan/jwj-dev-skills-marketplace`
2. `/plugin install split-main-sub-repo-plugin@jwj-dev-skills-marketplace`

## 安裝方式二：`npx skills`（跨 agent）

先查看此 repo 有哪些可安裝 skills：

```bash
npx -y skills@latest add jhihweijhan/jwj-dev-skills-marketplace -l
```

安裝指定 skill 到單一 agent（以 Codex 為例）：

```bash
npx -y skills@latest add jhihweijhan/jwj-dev-skills-marketplace --skill split-main-sub-repo --agent codex -y --copy
```

安裝到多個 agent：

```bash
npx -y skills@latest add jhihweijhan/jwj-dev-skills-marketplace --skill split-main-sub-repo --agent claude-code --agent codex --agent cursor -y --copy
```

## 重要說明

`npx skills@latest` **不需要** Claude marketplace 檔案。

`npx skills` 主要要求是 skill 結構合法，通常包含：
- `skills/<skill-name>/SKILL.md`
- `SKILL.md` 內有合法 frontmatter（`name`、`description`）
- 可存取的 Git 來源（GitHub `owner/repo` 或 URL）

因此：
- `/plugin ...` 流程：需要 `.claude-plugin/marketplace.json`
- `npx skills ...` 流程：marketplace 設定非必要，skill 結構才是關鍵

## 手動安裝（其他 agent）
把 `skills/split-main-sub-repo` 複製到你的 agent skills 路徑。

常見路徑：
- `~/.claude/skills/`
- `~/.copilot/skills/`
- `.agents/skills/`
