# ****************************************************************分割线****************************************************************
# todo 0231（Power of Two）
# 2的幂

class Solution:
    # 暴力（超时）
    def isPowerOfTwo(self, n: int) -> bool:
        while n != 1:
            if n % 2 == 1:
                return False
            n //= 2
        return True

    # 位运算（1/2/4的二进制分别为1/10/100，2的幂二进制只有一个1）
    def isPowerOfTwo2(self, n: int) -> bool:
        count = 0
        while n > 0:
            print(n & 1)  # 按位与再右移
            count += (n & 1)
            n >>= 1
        return count == 1

# print(Solution().isPowerOfTwo(100))
# print(Solution().isPowerOfTwo(-1))
print(Solution().isPowerOfTwo2(4))
