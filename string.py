# 实现一个算法，确定一个字符串 s 的所有字符是否全都不同。
def string_is_only(s:str) -> bool:
    return len(set(s)) == len(s)

# set集合原生实现
def string_is_only_set(s:str) -> bool:
    seen = set()
    for ch in s:
        if ch in seen:
            return False
        seen.add(ch)
    return True

# main方法实现
if __name__ == "__main__":
    print(string_is_only_set("djsbdd"))

