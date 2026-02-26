---
name: split-main-sub-repo
description: 拆分單一專案為公開子倉與私有主倉並建立 submodule 開發入口。當使用者提到要把 AI 開發資料與公開程式碼分離、建立 project 與 project-dev 雙倉、或要求從主倉入口管理子倉時使用。執行時必須先逐題詢問細節（命名、可見性、排除清單、遠端）再實作。
---

# Split Main Sub Repo

## 目標
將現有專案拆分為：
- 公開子倉：`<project>`（不含 AI/私有開發資料）
- 私有主倉：`<project>-dev`（保留 AI 開發資料，並以 submodule 引入子倉）

## 互動規則
1. 先問問題再動手，且一次只問一題。
2. 先展示預設值，再問「要補充或修改嗎」。
3. 未拿到明確答案前，不執行 destructive 操作。

## 固定預設
- 命名規則固定：子倉 `<project>`、主倉 `<project>-dev`
- 先套用嚴格排除清單（含 `CLAUDE.md`），再詢問使用者是否補充/修改。

### 嚴格排除清單（預設）
- `.claude/`
- `.serena/`
- `.beads/`
- `skills/`
- `AGENTS.md`
- `CLAUDE.md`
- `docs/plans/`
- `tmp/`
- `sandbox/`
- `*.bin`
- `*.key`
- `*.pem`
- `.env*`

## 執行流程
### 1) 收集細節（逐題）
依序確認：
1. 專案基底名稱（不含 `-dev`）
2. GitHub owner/org
3. 主倉可見性是否為 private、子倉可見性是否為 public
4. 排除清單要不要補充或刪減
5. 是否要同步改本機資料夾名稱

### 2) 盤點與備份
1. 檢查工作樹是否乾淨；若不乾淨，先詢問如何處理。
2. 產生「保留於主倉」與「放入子倉」兩份清單並讓使用者確認。
3. 必要時建立備份分支或 tag。

### 3) 建立公開子倉
1. 依排除清單建立乾淨內容。
2. 確認不包含 AI/私有資料。
3. 初始化 git、設定 remote、提交初版並推送。

### 4) 建立私有主倉
1. 保留完整開發資料。
2. 將公開子倉加入為 submodule（路徑名與子倉名一致）。
3. 更新 `.gitmodules`、主倉 README、開發流程文件。

### 5) 驗證
至少執行：
1. `git status --short`（主倉/子倉都乾淨）
2. `git submodule status`（主倉）
3. `git remote -v`（主倉/子倉 URL 正確）
4. 搜尋排除項是否還留在公開子倉

### 6) 回報
回報必須包含：
1. 主倉/子倉 repo URL
2. 最新 commit SHA
3. 實際套用的排除清單
4. 尚未完成的項目（若有）

## 可用資源
- 預設排除清單：`references/default-excludes.txt`
- 排除清單組裝工具：`scripts/merge_excludes.py`
