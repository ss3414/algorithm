# ****************************************************************分割线****************************************************************
# todo 0287（Find the Duplicate Number）
# 寻找重复数

class Solution:
    def findDuplicate(self, nums: list) -> int:
        left, right = 1, len(nums)
        while left < right:
            middle = (left + right) // 2
            count = 0
            for i in nums:
                if i <= middle:
                    count += 1
            if count > middle:
                right = middle
            else:
                left = middle + 1
        return right

print(Solution().findDuplicate([2, 2, 2, 2, 2]))
