# ****************************************************************分割线****************************************************************
# todo 1732（Find the Highest Altitude）
# 最高海拔

class Solution:
    def largestAltitude(self, gain: list) -> int:
        l = len(gain)
        prefix = [0] * (l + 1)
        i = 0
        while i < l:
            prefix[i + 1] = prefix[i] + gain[i]
            i += 1
        return max(prefix)

print(Solution().largestAltitude([-5, 1, 5, 0, -7]))
