# ****************************************************************分割线****************************************************************
# todo 0977（Squares of a Sorted Array）
# 有序数组的平方

class Solution:
    def sortedSquares(self, nums: list) -> list:
        result = [i * i for i in nums]
        return sorted(result)

print(Solution().sortedSquares([-4, -1, 0, 3, 10]))
