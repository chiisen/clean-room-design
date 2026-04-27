# Clean Room Design 完整演示

## 概念說明

Clean Room Design 是一種避免版權爭議的技術移植方法。

核心原則：**移植者永遠不看原始代碼，只看功能規格。**

## 角色分工

| 角色           | 職責                  | 是否可看原始程式碼 |
| -------------- | --------------------- | ---------------- |
| **規格編寫者** | 閱讀 JS，提取功能描述 | ✅ 可以看        |
| **移植開發者** | 根據規格寫 C#         | ❌ 不可以看      |

## 泡沫排序演示

### Phase 1: 規格提取（規格編寫者）

原始 JS 代碼（僅供參考，移植者不看）：

```javascript
function bubbleSort(arr) {
  let n = arr.length;
  for (let i = 0; i < n - 1; i++) {
    for (let j = 0; j < n - i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
      }
    }
  }
  return arr;
}
```

規格編寫者提取功能 → 輸出 `bubble-sort-spec.md`

### Phase 2: 規格文檔化

規格存入 `/raw/bubble-sort-spec.md`，包含：

- 功能描述
- 算法行為
- 輸入/輸出示例
- 邊界條件

### Phase 3: 新語言實現（移植開發者）

移植開發者只看規格，不看 JS：

```csharp
public static void BubbleSort(int[] arr)
{
    if (arr == null || arr.Length <= 1) return;

    bool swapped;
    int n = arr.Length;

    do
    {
        swapped = false;
        for (int i = 0; i < n - 1; i++)
        {
            if (arr[i] > arr[i + 1])
            {
                int temp = arr[i];
                arr[i] = arr[i + 1];
                arr[i + 1] = temp;
                swapped = true;
            }
        }
        n--;
    } while (swapped);
}
```

### Phase 4: 測試驗證

驗證兩版本行為一致：

| 測試輸入      | JS 輸出       | C# 輸出       | 結果 |
| ------------- | ------------- | ------------- | ---- |
| `[5,3,8,4,2]` | `[2,3,4,5,8]` | `[2,3,4,5,8]` | ✅   |
| `[]`          | `[]`          | `[]`          | ✅   |
| `[1]`         | `[1]`         | `[1]`         | ✅   |

## AI Agent 角色

在 AI 協助下：

| 任務       | AI 執行方式                                    |
| ---------- | ---------------------------------------------- |
| 規格提取   | 用戶提供代碼 → AI 提取功能描述（不看代碼細節） |
| 規格文檔化 | AI 存入 `/raw/`                                |
| 新語言實現 | AI 根據規格寫新代碼（不參考原代碼）            |
| 測試驗證   | AI 生成測試用例驗證                            |

---

## 下一步

你有實際要移植的項目嗎？
