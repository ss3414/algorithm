# ****************************************************************分割线****************************************************************
# todo 0190（Reverse Bits）
# 逆序二进制位

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        i = 0
        while i < 32:
            if n & 1 == 1:  # 和01"与"
                result = (result << 1) + 1
            else:
                result <<= 1
            print(bin(result))
            n >>= 1
            i += 1
        return result

print(Solution().reverseBits(0b00000010100101000001111010011100))
