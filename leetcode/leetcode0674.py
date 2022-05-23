# ****************************************************************分割线****************************************************************
# todo 0674（Longest Continuous Increasing Subsequence）
# 最长递增子数组

class Solution:
    def findLengthOfLCIS(self, nums: list) -> int:
        i = 0
        count = 1
        result = 0
        while i < len(nums) - 1:
            if nums[i + 1] > nums[i]:
                count += 1
            else:
                result = max(result, count)
                count = 1
            i += 1
        result = max(result, count)
        return result

print(Solution().findLengthOfLCIS([1, 3, 5, 7]))
# print(Solution().findLengthOfLCIS([1,7,9,3,5]))
# print(Solution().findLengthOfLCIS([2,2,2,2,2]))
