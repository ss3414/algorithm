# ****************************************************************分割线****************************************************************
# todo 2221（Find Triangular Sum of an Array）
# 数组的三角和

class Solution:
    # 暴力
    def triangularSum(self, nums: list) -> int:
        while len(nums) > 1:
            l = len(nums)
            temp = [None] * (l - 1)
            i = 0
            while i < l - 1:
                temp[i] = (nums[i] + nums[i + 1]) % 10
                i += 1
            nums = temp
        return nums[0]

print(Solution().triangularSum([1, 2, 3, 4, 5]))
