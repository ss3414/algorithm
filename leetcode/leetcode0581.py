# ****************************************************************分割线****************************************************************
# todo 0581（Shortest Unsorted Continuous Subarray）
# 最短未排序子数组

class Solution:
    # 池沼算法
    def findUnsortedSubarray(self, nums: list) -> int:
        length = len(nums)
        left, right = 0, length - 1
        while left <= right and left < length - 1 and right > 0:
            if nums[left + 1] < nums[left] and nums[right - 1] > nums[right]:
                break
            if nums[left + 1] >= nums[left]:
                left += 1
            if nums[right - 1] <= nums[right]:
                right -= 1
        print("{l} {r}".format(l=left, r=right))

print(Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
