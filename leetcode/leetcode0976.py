# ****************************************************************分割线****************************************************************
# todo 0976（Largest Perimeter Triangle）
# 三角形周长

class Solution:
    def largestPerimeter(self, nums: list) -> int:
        nums.sort(reverse=True)
        i = 0
        while i < len(nums) - 2:
            if nums[i] + nums[i + 1] > nums[i + 2] and nums[i + 1] + nums[i + 2] > nums[i] and nums[i] + nums[i + 2] > nums[i + 1]:
                return nums[i] + nums[i + 1] + nums[i + 2]
            i += 1
        return 0

print(Solution().largestPerimeter([1, 2, 1]))
print(Solution().largestPerimeter([3, 2, 3, 4]))
