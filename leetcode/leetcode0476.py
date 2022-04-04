# ****************************************************************分割线****************************************************************
# todo 0476（Number Complement）
# 数字的补数

class Solution:
    def findComplement(self, num: int) -> int:
        i = 1
        while i <= num:  # 比num的二进制大一位再减一
            i = i << 1
        print("{i}^{n}={r}".format(i=bin(i - 1), n=bin(num), r=bin((i - 1) ^ num)))
        return (i - 1) ^ num

print(Solution().findComplement(5))
