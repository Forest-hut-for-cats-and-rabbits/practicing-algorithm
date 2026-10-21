class String:
# 实现一个算法，确定一个字符串 s 的所有字符是否全都不同。
   @staticmethod
   def string_is_only(s: str) -> bool:
       return len(set(s)) == len(s)

# set集合原生实现
   @staticmethod
   def string_is_only_set(s: str) -> bool:
       seen = set()
       for ch in s:
          if ch in seen:
              return False
          seen.add(ch)
       return True

# 给定两个由小写字母组成的字符串 s1 和 s2，请编写一个程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串
   @staticmethod
   def str_copy_other(s1: str, s2: str) -> bool:
       return sorted(s1) == sorted(s2)

# 编写一种方法，将字符串中的空格全部替换为%20。假定该字符串尾部有足够的空间存放新增字符，并且知道字符串的“真实”长度
   @staticmethod
   def str_format(s: str, l: int) -> str:
       return s[:l].replace(' ', '%20')


# main方法实现
if __name__ == "__main__":
    print(String.str_format("Mr John Smith", 13))
