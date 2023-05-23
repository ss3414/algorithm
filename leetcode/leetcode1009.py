# ****************************************************************分割线****************************************************************
# todo 1009（Complement of Base 10 Integer）
# 十进制数的反码

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return int("".join("0" if i == "1" else "1" for i in bin(n)[2:]), 2)

print(Solution().bitwiseComplement(2))
print(Solution().bitwiseComplement(5))
