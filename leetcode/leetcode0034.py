# ****************************************************************分割线****************************************************************
# todo 0034（Find First and Last Position of Element in Sorted Array）
# 在有序数组中寻找元素前后位置

class Solution:
    # 二分法
    def searchRange(self, nums: list, target: int) -> list:
        result = [-1, -1]
        if target not in nums:
            return result

        # 左插入
        left, right = 0, len(nums)
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] >= target:
                right = middle - 1
            else:
                left = middle + 1
        result[0] = left

        # 右插入
        right = len(nums)
        while left < right:
            middle = (left + right) // 2
            if nums[middle] <= target:
                left = middle + 1
            else:
                right = middle
        result[1] = right - 1
        return result

print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
print(Solution().searchRange([2, 2], 2))
print(Solution().searchRange([0], 0))
