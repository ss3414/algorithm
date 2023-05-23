# ****************************************************************分割线****************************************************************
# todo 0908（Smallest Range I）
# 最小差值I

class Solution:
    def smallestRangeI(self, nums: list, k: int) -> int:
        result = max(nums) - min(nums)
        return 0 if result <= 2 * k else result - 2 * k

print(Solution().smallestRangeI([1], 0))
print(Solution().smallestRangeI([0, 10], 2))
print(Solution().smallestRangeI([1, 3, 6], 3))
