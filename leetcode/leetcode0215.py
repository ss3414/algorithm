# ****************************************************************分割线****************************************************************
# todo 0215（Kth Largest Element in an Array）
# 数组中第K大个元素

import heapq

class Solution:
    # 最大堆
    def findKthLargest(self, nums: list, k: int) -> int:
        data = [-i for i in nums]
        heapq.heapify(data)
        for i in range(1, k):
            heapq.heappop(data)
        return -data[0]

print(Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
