# ****************************************************************分割线****************************************************************
# todo 1221（Split a String in Balanced Strings）
# 分割平衡字符串

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        def test(c):
            if c == "L":
                return 1
            if c == "R":
                return -1

        count = 0
        temp = test(s[0])
        i = 1
        while i < len(s):
            temp += test(s[i])
            if temp == 0:
                count += 1
            i += 1
        return count

print(Solution().balancedStringSplit("RLRRLLRLRL"))
