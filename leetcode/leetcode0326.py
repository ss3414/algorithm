# ****************************************************************分割线****************************************************************
# todo 0326（Power of Three）
# 3的幂

import math

class Solution:
    # 暴力
    def isPowerOfThree(self, n: int) -> bool:
        while n and n % 3 == 0:
            print(n)
            n //= 3
        return n == 1

    # 对数（n是3的幂，判断log3n是否为整数，换底公式log3n=lg3/lgn）
    # 无法AC
    def isPowerOfThree2(self, n: int) -> bool:
        return math.log(n, 3) - int(math.log(n, 3)) == 0

# print(Solution().isPowerOfThree(3**4))
# print(Solution().isPowerOfThree(100))

print(Solution().isPowerOfThree2(3 ** 4))
print(Solution().isPowerOfThree2(100))
