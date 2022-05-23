# ****************************************************************分割线****************************************************************
# todo 0697（Degree of an Array）
# 数组的度

class Solution:
    def findShortestSubArray(self, nums: list) -> int:
        data = {}
        for i in nums:
            if i in data:
                data[i] += 1
            else:
                data[i] = 1
        max_val = max(data.values())
        result = len(nums)
        for key, val in data.items():
            if val == max_val:
                left = nums.index(key)
                nums.reverse()
                right = len(nums) - nums.index(key)
                result = min(result, right - left)
                nums.reverse()
        return result

# print(Solution().findShortestSubArray([1,1,4,5,1,4]))
print(Solution().findShortestSubArray([1, 2, 2, 3, 1]))
