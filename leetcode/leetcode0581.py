# ****************************************************************分割线****************************************************************
# todo 0581（Shortest Unsorted Continuous Subarray）
# 最短未排序子数组

class Solution:
    def findUnsortedSubarray(self, nums: list) -> int:
        origins = nums + []
        nums.sort()
        l, r = 0, -1
        flag = False
        i = 0
        # 记录第一个和最后一个修改
        while i < len(nums):
            if origins[i] != nums[i] and not flag:
                l = i
                flag = True
            if origins[i] != nums[i] and flag:
                r = i
            i += 1
        return r - l + 1

print(Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
print(Solution().findUnsortedSubarray([6, 4, 2, 8, 9, 15, 10]))
