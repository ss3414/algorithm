# ****************************************************************分割线****************************************************************
# todo 0812（Largest Triangle Area）
# 最大三角形面积

class Solution:
    # 三角形面积公式
    def largestTriangleArea(self, points: list) -> float:
        result = 0
        for i in points:
            for j in points:
                for k in points:
                    area = 0.5 * abs((i[0] * j[1] - i[1] * j[0]) + (j[0] * k[1] - j[1] * k[0]) + (k[0] * i[1] - k[1] * i[0]))
                    result = max(result, area)
        return result

print(Solution().largestTriangleArea([[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]))
