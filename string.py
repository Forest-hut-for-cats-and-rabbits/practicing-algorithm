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

# 给定两个由小写字母组成的字符串 s1 和 s2，请编写一个程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串
def str_copy_other(s1:str,s2:str) -> bool:
    return sorted(s1) == sorted(s2)


# main方法实现
if __name__ == "__main__":
    print(string_is_only_set("djsbdd"))
    print(str_copy_other("deeqw","wdeeq"))

