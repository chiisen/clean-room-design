# Clean Room Design

淨室設計（Clean Room Design）是一種避免版權爭議的技術移植方法，確保移植者在實現新程式碼時不接觸原始程式碼。

## 目的

本專案建立 Clean Room Design 的完整流程文檔與 AI Agent 協作指南，用於：

- 學習 Clean Room Design 概念
- 理解 AI Agent 的 Session 隔離策略
- 實際進行技術移植專案

## 文檔結構

```
/raw/                           ← 技術文件輸入區
├── bubble-sort-spec.md         ← Level 1 演示：泡沫排序規格
├── clean-room-concepts.md      ← 概念深入：法律背景、適用場景、風險
└── session-isolation-strategy.md ← AI Agent Session 隔離策略

/docs/examples/                 ← 演示範例
└── clean-room-demo.md          ← 泡沫排序完整演示

/AGENTS.md                      ← AI Agent 專案規範（MemPalace + Graphify + Clean Room）
```

## 核心概念

### Clean Room Design 三原則

1. **功能規格先行** - 描述「做什麼」，不描述「怎麼做」
2. **代碼隔離** - 移植者不看原始代碼，只看規格
3. **行為驗證** - 測試輸入/輸出行為一致，不對比代碼結構

### AI Agent Session 分工

| Session | 角色 | 可看原代碼 |
|---------|------|-----------|
| Session A | 規格編寫者 | ✅ |
| Session B | 移植開發者 | ❌ |
| Session C | 測試驗證者 | ❌ |

## 快速開始

### 學習流程

1.閱讀 [`/docs/examples/clean-room-demo.md`](docs/examples/clean-room-demo.md) - 了解基本概念
2. 閱讀 [`/raw/clean-room-concepts.md`](raw/clean-room-concepts.md) - 深入理解適用場景
3. 閱讀 [`/raw/session-isolation-strategy.md`](raw/session-isolation-strategy.md) - AI Agent 協作方式

### 實際專案流程

1. 將原始專案代碼放入 `/raw/source/`
2.開啟 **Session A**，執行規格提取 →輸出 `/raw/specs/*.md`
3. 開啟 **Session B**，根據規格實現新語言版本
4. 開啟 **Session C**，測試驗證行為一致性

## 相關配置

詳見 [`AGENTS.md`](AGENTS.md)：

- MemPalace 記錄策略（Wing 架構、記錄流程）
- Graphify 知識图谱（目錄結構、使用流程）
- Clean Room Session 隔離（角色分工、記錄規則）

---

_本專案為 Clean Room Design 學習與實踐專案，文件持續更新中。_
