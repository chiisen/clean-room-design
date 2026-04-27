# Clean Room Design - AI Agent 專案規範

## 🧠 MemPalace 記錄策略

### Wing 架構

```
wing: wing_clean_room_design
├── room: documents/      ← 定案後的技術文件全文 (Drawer)
├── room: decisions/      ← 定案後的決策記錄 (Drawer)
├── room: concepts/       ← 定案後的概念定義 (Drawer)
├── room: references/     ← 定案後的外部參考連結 (Drawer)
├── room: specs/          ← Clean Room 功能規格 (Session A)
├── room: implementations/← Clean Room 新實現記錄 (Session B)
└── room: test-results/   ← Clean Room 測試驗證 (Session C)
```

### 記錄流程

| 階段 | 方式 | 工具 |
|------|------|------|
| **討論階段** | Diary + Knowledge Graph | `mempalace_diary_write` + `mempalace_kg_add` |
| **定案後** | Drawer (verbatim) | `mempalace_add_drawer` |

### 行為規則

1. **每次會話結束**：使用 `mempalace_diary_write` 記錄 AAAK 摘要
2. **暫定概念關係**：使用 `mempalace_kg_add` 記錄
3. **推翻舊想法**：使用 `mempalace_kg_invalidate` 更新
4. **定案文件**：使用 `mempalace_add_drawer` 存入 wing_clean_room_design

### AAAK Entity Codes (專案專用)

| Code | Entity |
|------|--------|
| CRD | clean-room-design (本專案) |
| MP | mempalace |
| DOC | documents |
| DEC | decisions |

### 啟動協定

會話開始時呼叫 `mempalace_mempalace_kg_query(entity="clean-room-design")` 查詢既有記錄。

## 🔒 Clean Room Design Session 隔离

### 角色分工

| Session | 角色 | 可看原代码 | 输入 | 输出 |
|---------|------|-----------|------|------|
| **Session A** | 规格编写者 | ✅ | 原代码仓库 | `/raw/specs/*.md` |
| **Session B** | 移植开发者 | ❌ | `/raw/specs/*.md` | 新语言实现 |
| **Session C** | 测试验证者 | ❌ | 测试用例 | 验证报告 |

### 记录规则

| 阶段 | 可记录 | 不可记录 |
|------|--------|----------|
| **规格阶段** | 功能描述、输入/输出格式、边界条件 | 具体代码片段、变量命名、算法结构 |
| **实现阶段** | 实现决策、新代码结构 | 对原代码的对比分析 |
| **验证阶段** | 测试结果、行为差异 | 代码结构差异分析 |

### MemPalace 污染检查

Session A 结束前，审查 MemPalace 记录，使用 `mempalace_kg_invalidate` 清除代码细节记录。

## 🔮 Graphify 知識图谱

### 目錄結構

```
/raw/                    ← 技術文件輸入區 (docs, PDFs, images)
/graphify-out/           ← 輰出的知識图谱
├── graph.html           ← 可視化图谱 (瀏覽器開啟)
├── GRAPH_REPORT.md      ← 审计報告
├── graph.json           ← 原始图谱數據
└── obsidian/            ← Obsidian vault (可选)
```

### 使用流程

| 操作 | 指令 |
|------|------|
| **初始化图谱** | `/graphify ./raw` |
| **增量更新** | `/graphify ./raw --update` |
| **查询概念** | `/graphify query "關鍵字"` |
| **解释节点** | `/graphify explain "概念名"` |
| **寻找路径** | `/graphify path "概念A" "概念B"` |

### 行為規則

1. **新增文件**：放入 `/raw` 後執行 `/graphify ./raw --update`
2. **查询前**：優先使用 `/graphify query` 檢查图谱是否已有相關概念
3. **會話結束**：若有新增文件，自動執行增量更新

## 其他專案規範

_待討論定案後補充_