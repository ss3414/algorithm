# ****************************************************************分割线****************************************************************
# todo 0643（Maximum Average Subarray I）
# 子数组最大平均数

class Solution:
    # 超时
    def findMaxAverage(self, nums: list, k: int) -> float:
        if len(nums) == k:
            return sum(nums) / k
        result = -10 ** 5
        i = 0
        while i + k <= len(nums):
            # print(nums[i:i+k+1])
            result = max(result, sum(nums[i:i + k]) / k)
            i += 1
        return result

    def findMaxAverage2(self, nums: list, k: int) -> float:
        temp = sum(nums[0:k])
        result = temp
        i = k
        while i < len(nums):
            temp += nums[i] - nums[i - k]  # result加上右边再减去左边
            print(temp)
            result = max(result, temp)
            i += 1
        return result / k

# print(Solution().findMaxAverage([1,12,-5,-6,50,3],4))
print(Solution().findMaxAverage2([0, 4, 0, 3, 2], 1))
