# ****************************************************************分割线****************************************************************
# todo 1413（Minimum Value to Get Positive Step by Step Sum）
# 逐步求和

class Solution:
    def minStartValue(self, nums: list) -> int:
        nums.insert(0, 0)
        result = nums[0] + nums[1]
        i = 2
        while i < len(nums):
            print("{r} {s}".format(r=result, s=sum(nums[0:i + 1])))
            result = min(result, sum(nums[0:i + 1]))
            i += 1
        if result >= 1:
            return 1
        else:
            return 1 - result

    # 前缀和
    def minStartValue2(self, nums: list) -> int:
        l = len(nums)
        prefix = [0] * (l + 1)
        i = 0
        while i < l:
            prefix[i + 1] = prefix[i] + nums[i]
            i += 1
        result = min(prefix[1::])
        if result >= 1:
            return 1
        else:
            return 1 - result

print(Solution().minStartValue([2, 3, 5, -5, 1]))
# print(Solution().minStartValue([-3,6,2,5,8,6]))
print(Solution().minStartValue2([-3, 6, 2, 5, 8, 6]))
