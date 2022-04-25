# ****************************************************************分割线****************************************************************
# todo 0506（Relative Ranks）
# 相对排名

from queue import PriorityQueue

class Solution:
    # 堆
    def findRelativeRanks(self, score: list) -> list:
        result = [None] * len(score)
        rank = 1
        # Python中优先队列使用堆实现
        orders = PriorityQueue()
        i = 0
        while i < len(score):
            orders.put((-score[i], i))  # 加个负号即最大堆
            i += 1
        while not orders.empty():
            index = orders.get()[1]
            if rank == 1:
                result[index] = "Gold Medal"
            elif rank == 2:
                result[index] = "Silver Medal"
            elif rank == 3:
                result[index] = "Bronze Medal"
            else:
                result[index] = str(rank)
            rank += 1
        return result

print(Solution().findRelativeRanks([2, 4, 8, 6]))
