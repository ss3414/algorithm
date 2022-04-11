# ****************************************************************分割线****************************************************************
# todo 1232（Check If It Is a Straight Line）
# 缀点成线

class Solution:
    # 直线斜率
    def checkStraightLine(self, coordinates: list) -> bool:
        x1, y1 = coordinates[0][0], coordinates[0][1]
        x2, y2 = coordinates[1][0], coordinates[1][1]
        i = 2
        while i < len(coordinates):
            x3, y3 = coordinates[i][0], coordinates[i][1]
            if (y2 - y1) * (x3 - x1) != (x2 - x1) * (y3 - y1):
                return False
            i += 1
        return True

print(Solution().checkStraightLine([[1, 2], [2, 3], [3, 4]]))
