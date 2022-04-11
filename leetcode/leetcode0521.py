# ****************************************************************分割线****************************************************************
# todo 0521（Longest Uncommon Subsequence I）
# 最长不同子串

class Solution:
    # 池沼算法
    def findLUSlength(self, a: str, b: str) -> int:
        if len(a) > len(b):
            a, b = b, a
        la, lb = len(a), len(b)
        i, j = 0, 0
        while i < la and j < lb:
            if a[i] == b[j]:
                i += 1
            j += 1
        if i == la:
            if la == lb:
                return -1
            else:
                return lb - la
        else:
            return lb

    def findLUSlength2(self, a: str, b: str) -> int:
        return -1 if a == b else max(len(a), len(b))

# print(Solution().findLUSlength("aaa","aaa"))
print(Solution().findLUSlength2("abc", "def"))
