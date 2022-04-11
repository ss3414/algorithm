# ****************************************************************分割线****************************************************************
# todo 1037（Valid Boomerang）
# 有效的回旋镖
# 三个坐标点不在一条直线上

class Solution:
    # 直线斜率
    def isBoomerang(self, points: list) -> bool:
        x1, y1 = points[0][0], points[0][1]
        x2, y2 = points[1][0], points[1][1]
        x3, y3 = points[2][0], points[2][1]
        return not (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1)

print(Solution().isBoomerang([[1, 1], [2, 3], [3, 2]]))
