# ****************************************************************分割线****************************************************************
# todo 0713（Design HashMap）
# 乘积小于K的子数组

class Solution:
    # 暴力（超时）
    def numSubarrayProductLessThanK(self, nums: list, k: int) -> int:
        def test(nums):
            result = 1
            i = 0
            while i < len(nums):
                result *= nums[i]
                i += 1
            return result

        result = 0
        left = 0
        while left < len(nums):
            right = left + 1
            while right <= len(nums):
                if test(nums[left:right]) < k:
                    print(nums[left:right])
                    result += 1
                else:
                    break
                right += 1
            left += 1
        return result

    # 滑动窗口
    def numSubarrayProductLessThanK2(self, nums: list, k: int) -> int:
        result = 0
        left = 0
        product = 1
        i = 0
        while i < len(nums):
            product *= nums[i]
            # 维护一个积小于K的滑动窗口，每个窗口元素个数和等于结果
            while left <= i and product >= k:
                product //= nums[left]
                left += 1
            result += (i + 1 - left)
            print(nums[left:i + 1])
            i += 1
        return result

# print(Solution().numSubarrayProductLessThanK([10, 5, 2, 6], 100))
print(Solution().numSubarrayProductLessThanK2([10, 5, 20, 6], 100))
