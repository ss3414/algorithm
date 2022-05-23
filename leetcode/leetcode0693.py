# ****************************************************************分割线****************************************************************
# todo 0693（Binary Number with Alternating Bits）
# 二进制数交替位

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary = bin(n)[2::]
        i = 0
        while i < len(binary) - 1:
            if binary[i] == binary[i + 1]:
                return False
            i += 1
        return True

print(Solution().hasAlternatingBits(5))
print(Solution().hasAlternatingBits(7))
