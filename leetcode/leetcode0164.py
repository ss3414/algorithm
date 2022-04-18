# ****************************************************************分割线****************************************************************
# todo 0164（Maximum Gap）
# 最大间距

class Solution:
    def maximumGap(self, nums: list) -> int:
        if len(nums) < 2:
            return 0

        max_val = max(nums)
        max_digit = 1
        while max_val // 10 > 0:
            max_digit += 1
            max_val = max_val // 10

        digit = 0
        while digit < max_digit:
            temp = [[] for i in range(10)]
            for num in nums:
                t = (num // 10 ** digit) % 10
                temp[t].append(num)
            nums = []
            for bucket in temp:
                for i in bucket:
                    nums.append(i)
            digit += 1

        max_gap = 0
        i = 0
        while i < len(nums) - 1:
            max_gap = max(max_gap, abs(nums[i] - nums[i + 1]))
            i += 1
        return max_gap

print(Solution().maximumGap([3, 6, 9, 1]))
