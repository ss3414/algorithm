# ****************************************************************分割线****************************************************************
# todo 0598（Range Addition II）
# 区间求和II

class Solution:
    def maxCount(self, m: int, n: int, ops: list) -> int:
        area = [m, n]
        i = 0
        while i < len(ops):
            x1 = area[0]
            x2 = ops[i][0]
            y1 = area[1]
            y2 = ops[i][1]
            area[0] = x1 if x1 <= x2 else x2
            area[1] = y1 if y1 <= y2 else y2
            i += 1
        # print(area)
        return area[0] * area[1]

# print(Solution().maxCount(3,3,[[1,1],[1,3],[3,1]]))
print(Solution().maxCount(3, 3, [[2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3]]))
