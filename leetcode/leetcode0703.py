# ****************************************************************分割线****************************************************************
# todo 0703（Kth Largest Element in a Stream）
# 数据流中第K大元素

import heapq

class KthLargest:
    def __init__(self, k: int, nums: list):
        self.pool = nums
        self.k = k
        heapq.heapify(self.pool)  # 构建最小堆
        while len(self.pool) > self.k:  # 保留K大个元素
            heapq.heappop(self.pool)

    def add(self, val: int) -> int:
        heapq.heappush(self.pool, val)
        while len(self.pool) > self.k:
            heapq.heappop(self.pool)
        print(self.pool)
        return self.pool[0]

obj = KthLargest(3, [4, 5, 8, 2])
print(obj.add(3))
print(obj.add(5))
print(obj.add(10))
