# ****************************************************************分割线****************************************************************
# todo 0485（Max Consecutive Ones）
# 最大连续的1的个数

class Solution:
    def findMaxConsecutiveOnes(self, nums: list) -> int:
        result = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
            elif num == 0:
                result = max(result, count)
                count = 0
        return max(result, count)

print(Solution().findMaxConsecutiveOnes([0, 1, 0, 1, 1, 1]))
