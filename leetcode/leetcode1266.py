# ****************************************************************分割线****************************************************************
# todo 1266（Minimum Time Visiting All Points）
# 访问所有点的最小时间

class Solution:
    # 凑正方形
    def minTimeToVisitAllPoints(self, points: list) -> int:
        result = 0
        i = 0
        while i < len(points) - 1:
            x1, y1 = points[i][0], points[i][1]
            x2, y2 = points[i + 1][0], points[i + 1][1]
            t1 = abs(x1 - x2)
            t2 = abs(y1 - y2)
            temp = abs(t1 - t2)
            if temp == 0:
                result += t1
            else:
                result += (t1 if t1 > t2 else t2)
            i += 1
        return result

print(Solution().minTimeToVisitAllPoints([[1, 1], [3, 4], [-1, 0]]))
