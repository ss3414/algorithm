# ****************************************************************分割线****************************************************************
# todo 0918（Maximum Sum Circular Subarray）
# 环形数组子数组最大和

from collections import deque

class Solution:
    def maxSubarraySumCircular(self, nums: list) -> int:
        if len(nums) == 1:
            return 0

        temp = nums[:-1]
        queue = deque(nums[:-1])
        nums.insert(0, nums[-1])
        for i in nums:
            queue.append(i)
            queue.popleft()
            if sum(queue) > sum(temp):
                temp = list(queue)
        print(temp)
        i, j = 0, len(temp)
        while True:
            if sum(temp[i + 1:j]) > sum(temp):
                i += 1
            elif sum(temp[i:j - 1]) > sum(temp):
                j -= 1
            else:
                break
        return sum(temp[i:j])

print(Solution().maxSubarraySumCircular([1, -2, 3, -2]))
