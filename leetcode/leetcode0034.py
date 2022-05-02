# ****************************************************************分割线****************************************************************
# todo 0034（Find First and Last Position of Element in Sorted Array）
# 在有序数组中寻找元素前后位置

class Solution:
    def searchRange(self, nums: list, target: int) -> list:
        result = [-1, -1]
        if target not in nums:
            return result

        left, right = 0, len(nums)
        while left < right:
            middle = left + (right - left) // 2
            # print("{l} {m} {r}".format(l=left,m=middle,r=right))
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle
        result[0] = right

        right = len(nums)
        while left < right:
            middle = left + (right - left) // 2
            # print("{l} {m} {r}".format(l=left,m=middle,r=right))
            if nums[middle] <= target:
                left = middle + 1
            else:
                right = middle
        result[1] = right - 1
        return result

print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
print(Solution().searchRange([2, 2], 2))
print(Solution().searchRange([0], 0))
