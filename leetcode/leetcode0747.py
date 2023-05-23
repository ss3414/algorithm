# ****************************************************************分割线****************************************************************
# todo 0747（Largest Number At Least Twice of Others）
# 至少是其他数字的两倍

class Solution:
    def dominantIndex(self, nums: list) -> int:
        max_val = max(nums)
        index = nums.index(max_val)
        nums.sort()
        return index if len(nums) == 1 or max_val >= 2 * nums[-2] else -1

print(Solution().dominantIndex([3, 6, 1, 0]))
print(Solution().dominantIndex([1, 2, 3, 4]))
print(Solution().dominantIndex([1]))
