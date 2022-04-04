# ****************************************************************分割线****************************************************************
# todo 0492（Construct the Rectangle）
# 构建矩形

import math

class Solution:
    # 暴力（超时）
    def constructRectangle(self, area: int) -> list:
        if (area // 2) ** 2 == area:
            return [area // 2, area // 2]
        result = [area, 1]
        l = area
        while l > 0:
            w = 1
            while w < area:
                if l * w == area and l > w and l - w < result[0] - result[1]:
                    result[0] = l
                    result[1] = w
                w += 1
            l -= 1
        return result

    def constructRectangle2(self, area: int) -> list:
        i = int(math.sqrt(area))
        while i > 0:
            if area % i == 0:
                return [area // i, i]
            i -= 1

# print(Solution().constructRectangle(120))
print(Solution().constructRectangle2(120))
