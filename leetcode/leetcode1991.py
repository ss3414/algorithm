# ****************************************************************分割线****************************************************************
# todo 1991（Find the Middle Index in Array）
# 数组中心下标
# 同LeetCode0724

class Solution:
    def findMiddleIndex(self, nums: list) -> int:
        sum1 = sum(nums)
        sum2 = 0
        i = 0
        while i < len(nums):
            if sum1 - nums[i] == 2 * sum2:
                return i
            sum2 += nums[i]
            i += 1
        return -1

print(Solution().findMiddleIndex([-1, -1, -1, -1, -1, 0]))
