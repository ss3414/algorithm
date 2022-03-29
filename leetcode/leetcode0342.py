# ****************************************************************分割线****************************************************************
# todo 0342（Power of Four）
# 4的幂

class Solution:
    # 位运算（一个1和偶数个0）
    def isPowerOfFour(self, n: int) -> bool:
        zero = 0
        one = 0
        while n > 0:
            bit = n & 1
            if bit == 0:
                zero += 1
            else:
                one += 1
            n >>= 1
        return one == 1 and zero % 2 == 0

print(Solution().isPowerOfFour(8))
print(Solution().isPowerOfFour(4 ** 4))
