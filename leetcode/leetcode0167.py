# ****************************************************************分割线****************************************************************
# todo 0167（Two Sum II - Input Array Is Sorted）
# 两数之和II

class Solution:
    def twoSum(self, numbers: list, target: int) -> list:
        left, right = 0, len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]
            elif sum > target:
                right -= 1
            elif sum < target:
                left += 1

print(Solution().twoSum([2, 7, 11, 15], 9))
