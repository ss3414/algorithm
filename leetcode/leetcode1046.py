# ****************************************************************分割线****************************************************************
# todo 1046（Last Stone Weight）
# 最后一块石头的重量

import heapq

class Solution:
    def lastStoneWeight(self, stones: list) -> int:
        stones = [-i for i in stones]  # 最大堆
        heapq.heapify(stones)
        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            if x != y:
                stones.append(y - x)
            heapq.heapify(stones)
        return 0 if len(stones) == 0 else abs(stones[0])

print(Solution().lastStoneWeight([2, 7, 4, 1, 8, 1]))
