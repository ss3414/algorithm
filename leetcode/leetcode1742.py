# ****************************************************************分割线****************************************************************
# todo 1742（Maximum Number of Balls in a Box）
# 盒中小球数量

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        def digit(n):
            div = 1
            while n / div >= 10:
                div *= 10
            digits = []
            while n > 0:
                temp = int(n // div)
                digits.append(temp)
                n -= temp * div
                div /= 10
            return sum(digits)

        data = {}
        for i in range(lowLimit, highLimit + 1):
            j = digit(i)
            if j in data.keys():
                data[j] = data[j] + 1
            else:
                data[j] = 1
        return max(data.values())

print(Solution().countBalls(5, 15))
