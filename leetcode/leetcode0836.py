# ****************************************************************分割线****************************************************************
# todo 0836（Rectangle Overlap）
# 矩形重叠

class Solution:
    def isRectangleOverlap(self, rec1: list, rec2: list) -> bool:
        x1, y1, x2, y2 = rec1[0], rec1[1], rec1[2], rec1[3]
        x3, y3, x4, y4 = rec2[0], rec2[1], rec2[2], rec2[3]
        return x1 < x4 and x3 < x2 and y1 < y4 and y3 < y2

# print(Solution().isRectangleOverlap([0,0,2,2],[1,1,3,3]))
print(Solution().isRectangleOverlap([7, 8, 13, 15], [10, 8, 12, 20]))
