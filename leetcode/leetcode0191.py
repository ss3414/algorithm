# ****************************************************************分割线****************************************************************
# todo 0191（Number of 1 Bits）
# 二进制数中1的个数（汉明重量）

class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n > 0:
            if n & 1 == 1:
                result += 1
            n >>= 1
        return result

print(Solution().hammingWeight(0b00000010100101000001111010011100))
