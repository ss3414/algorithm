# ****************************************************************分割线****************************************************************
# todo 0209（Minimum Size Subarray Sum）
# 长度最小子数组

class Solution:
    # 滑动窗口
    def minSubArrayLen(self, target: int, nums: list) -> int:
        length = len(nums)
        result = length + 1
        left = 0
        right = 0
        sum = 0
        while right < length:
            # sum<target时，right向右移动
            while sum < target and right < length:
                sum += nums[right]
                right += 1
            # sum>=target时，left向右移动
            while sum >= target:
                print(nums[left:right])
                result = min(result, right - left)
                sum -= nums[left]
                left += 1
        return 0 if result == length + 1 else result  # 没有符合条件的子数组

# print(Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(Solution().minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
