# ****************************************************************分割线****************************************************************
# todo 0392（Is Subsequence）
# 判断子串

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        if t == "":
            return False
        i, j = len(s) - 1, len(t) - 1
        while j >= 0:
            if s[i] == t[j]:
                i -= 1
            if i == -1:
                return True
            j -= 1
        return i == -1

# print(Solution().isSubsequence("ab", "abcde"))
print(Solution().isSubsequence("ab", "baab"))
