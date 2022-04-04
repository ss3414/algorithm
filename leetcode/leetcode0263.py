# ****************************************************************分割线****************************************************************
# todo 0263（Ugly Number）
# 丑数
# 可以由因子2/3/5构成的数

class Solution:
    def isUgly(self, n: int) -> bool:
        while n >= 2:
            if n % 2 == 0:
                n //= 2
            elif n % 3 == 0:
                n //= 3
            elif n % 5 == 0:
                n //= 5
            else:
                return False
        return n == 1

print(Solution().isUgly(30))
