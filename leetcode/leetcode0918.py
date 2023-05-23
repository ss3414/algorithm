# ****************************************************************分割线****************************************************************
# todo 0918（Maximum Sum Circular Subarray）
# 环形数组最大子数组的和

class Solution:
    # 最大子数组两种情况：第一种数组中的一段，第二种一头一尾（即用数组总和减去最小子数组），返回最大值
    # 如果数组元素全是负数，需要特别处理
    def maxSubarraySumCircular(self, nums: list) -> int:
        sum = 0
        min_val, max_val = float("infinity"), float("-infinity")
        temp_min, temp_max = 0, 0
        for i in nums:
            temp_min = min(temp_min + i, i)
            min_val = min(min_val, temp_min)
            temp_max = max(temp_max + i, i)
            max_val = max(max_val, temp_max)
            sum += i
        return max_val if sum - min_val == 0 else max(max_val, sum - min_val)

print(Solution().maxSubarraySumCircular([1, -2, 3, -2]))
print(Solution().maxSubarraySumCircular([5, -3, 5]))
print(Solution().maxSubarraySumCircular([-3, -2, -3]))
