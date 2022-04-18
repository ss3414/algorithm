# ****************************************************************分割线****************************************************************
# todo 1704（Determine if String Halves Are Alike）
# 字符串对称相似

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        data = "aeiouAEIOU"
        i, j = 0, len(s) - 1
        front, back = 0, 0
        while i < j:
            if s[i] in data:
                front += 1
            if s[j] in data:
                back += 1
            i += 1
            j -= 1
        return front == back

# print(Solution().halvesAreAlike("leetcode"))
print(Solution().halvesAreAlike("textbook"))
