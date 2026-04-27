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

## 🔒 Clean Room Design Session 隔離

### 角色分工

| Session | 角色 | 可看原程式碼 | 輸入 | 輸出 |
|---------|------|-----------|------|------|
| **Session A** | 規格編寫者 | ✅ | 原程式碼倉庫 | `/raw/specs/*.md` |
| **Session B** | 移植開發者 | ❌ | `/raw/specs/*.md` | 新語言實現 |
| **Session C** | 測試驗證者 | ❌ | 測試用例 | 驗證報告 |

### 記錄規則

| 階段 | 可記錄 | 不可記錄 |
|------|--------|----------|
| **規格階段** | 功能描述、輸入/輸出格式、邊界條件 | 具體程式碼片段、變數命名、算法結構 |
| **實現階段** | 實現決策、新程式碼結構 | 對原程式碼的對比分析 |
| **驗證階段** | 測試結果、行為差異 | 程式碼結構差異分析 |

### MemPalace 汙染檢查

Session A 結束前，審查 MemPalace 記錄，使用 `mempalace_kg_invalidate` 清除程式碼細節記錄。

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