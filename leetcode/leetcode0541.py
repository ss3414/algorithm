# ****************************************************************分割线****************************************************************
# todo 0541（Reverse String II）
# 反转字符串II

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for i in range(0, len(s), 2 * k):
            s[i:i + k] = reversed(s[i:i + k])
        return "".join(s)

print(Solution().reverseStr("leetcode", 2))
