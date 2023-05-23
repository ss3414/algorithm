# ****************************************************************分割线****************************************************************
# todo 0035（Search Insert Position）
# 寻找target在有序数组中的插入位置

import bisect

class Solution:
    # 暴力
    def searchInsert(self, nums: list, target: int) -> int:
        i = 0
        while i < len(nums) - 1:
            if nums[i] <= target <= nums[i + 1]:  # 插入区间
                if target == nums[i]:
                    return i  # 左
                else:
                    return i + 1  # 右
            i += 1
        if len(nums) > 0 and target <= nums[0]:
            return 0  # 比所有元素小
        else:
            return len(nums)  # 比所有元素大

    # 二分法
    def searchInsert2(self, nums: list, target: int) -> int:
        left, right = 0, len(nums)  # 给多个变量赋值
        middle = 0
        while left < right:
            middle = (left + right) // 2
            if target > nums[middle]:
                left = middle + 1
            else:
                right = middle
        return left

    # bisect（调用bisect，底层等价于Solution().searchInsert2）
    def searchInsert3(self, nums: list, target: int) -> int:
        return bisect.bisect_left(nums, target)

    # linear/线性回归
    def searchInsert4(self, nums: list, target: int) -> int:
        if not nums:
            return 0
        for i, num in enumerate(nums):
            print("i:{i} num:{num}".format(i=i, num=num))  # 下标/值
            if num >= target:
                return i
        return len(nums)

# print(Solution().searchInsert([1, 3, 5, 7], 3))
# print(Solution().searchInsert([1, 3, 5, 7], 0))
# print(Solution().searchInsert2([1, 3, 5, 7], 3))
# print(Solution().searchInsert2([1, 3, 5, 7], 0))
# print(Solution().searchInsert3([1, 3, 5, 7], 3))
print(Solution().searchInsert4([1, 3, 5, 7], 3))
