# ****************************************************************分割线****************************************************************
# todo 0503（Next Greater Element II）
# 下一个更大元素II

class Solution:
    def nextGreaterElements(self, nums: list) -> list:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [-1]

        length = len(nums)
        stack = [0]
        result = [-1] * length
        for i in range(1, length):
            while stack and nums[stack[-1]] < nums[i]:
                result[stack.pop()] = nums[i]
            stack.append(i)
        print(result)
        for i in range(length):
            while stack and nums[stack[-1]] < nums[i]:
                result[stack.pop()] = nums[i]
            if not stack:
                break
        return result

print(Solution().nextGreaterElements([1, 1, 4, 5, 1, 4]))
