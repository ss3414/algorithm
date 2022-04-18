# ****************************************************************分割线****************************************************************
# todo 1480（Running Sum of 1d Array）
# 数组动态和

class Solution:
    def runningSum(self, nums: list) -> list:
        result = nums[0:1]
        i = 1
        while i < len(nums):
            result.append(nums[i] + result[i - 1])
            i += 1
        return result

print(Solution().runningSum([1, 2, 3, 4]))
