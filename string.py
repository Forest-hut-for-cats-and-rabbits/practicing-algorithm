# 实现一个算法，确定一个字符串 s 的所有字符是否全都不同。
def string_is_only(s:str) -> bool:
    return len(set(s)) == len(s)

if __name__ == "__main__":
    print(string_is_only('wrerew222113'))