# practicing-algorithm

算法练习代码，主要用 Python 实现《程序员面试金典》和 LeetCode 的题目。

## 目录

| 文件 | 题目 | 说明 |
| --- | --- | --- |
| `string.py` | 1.1 判定字符是否唯一 | 判断字符串 `s` 的所有字符是否全都不同 |

## 环境

- Python 3
- 依赖见虚拟环境 `.venv`（已被 `.gitignore` 忽略，需自行创建）

```bash
python -m venv .venv
```

## 运行

```bash
python string.py
```

## 解题思路

### 判定字符是否唯一

利用 Python 内置的 `set` 去重：若去重后的字符数与原字符串长度相等，说明没有重复字符。

```python
def string_is_only(s: str) -> bool:
    return len(set(s)) == len(s)
```

- 时间复杂度 O(n)
- 空间复杂度 O(n)
- 空串视为满足条件（返回 `True`）
