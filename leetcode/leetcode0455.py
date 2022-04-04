# ****************************************************************分割线****************************************************************
# todo 0455（Assign Cookies）
# 分饼干

class Solution:
    def findContentChildren(self, g: list, s: list) -> int:
        g, s = sorted(g), sorted(s)
        i, j = 0, 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1
            j += 1
        return i

print(Solution().findContentChildren([3, 2, 1], [2, 1, 2]))
