# ****************************************************************分割线****************************************************************
# todo 0896（Monotonic Array）
# 单调数组

class Solution:
    def isMonotonic(self, nums: list) -> bool:
        origins = nums + []
        return origins == sorted(nums) or origins == sorted(nums)[::-1]

print(Solution().isMonotonic([1, 2, 3, 4, 5]))
print(Solution().isMonotonic([5, 4, 3, 2, 1]))
print(Solution().isMonotonic([1, 2, 3, 2, 1]))
