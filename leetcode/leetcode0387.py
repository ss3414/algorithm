# ****************************************************************分割线****************************************************************
# todo 0387（First Unique Character in a String）
# 第一个非重复字符

class Solution:
    def firstUniqChar(self, s: str) -> int:
        data = {}
        for i in s:
            if i in data:
                data[i] = data[i] + 1
            else:
                data[i] = 1
        for j in s:
            if data[j] == 1:
                return s.index(j)
        return -1

print(Solution().firstUniqChar("leetcode"))
