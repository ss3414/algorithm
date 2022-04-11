# ****************************************************************分割线****************************************************************
# todo 1447（Simplified Fractions）
# 最简分数

class Solution:
    def simplifiedFractions(self, n: int) -> list:
        def gcd(i, j):
            return j if i == 0 else gcd(j % i, i)

        result = []
        while n > 1:
            i, j = n - 1, n
            while i > 0:
                print("{i}/{j}".format(i=i, j=j))
                if gcd(i, j) == 1:
                    result.append("{i}/{j}".format(i=i, j=j))
                i -= 1
            n -= 1
        return result

print(Solution().simplifiedFractions(4))
