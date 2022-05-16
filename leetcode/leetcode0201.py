# ****************************************************************分割线****************************************************************
# todo 0201（Bitwise AND of Numbers Range）
# 范围内数字按位与

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        count = 0
        while m != n:
            print("{m} {n} {c}".format(m=bin(m), n=bin(n), c=count))
            m >>= 1
            n >>= 1
            count += 1
        # m与n相等时m就是公共部分
        print("{m} {n} {c}".format(m=bin(m), n=bin(n), c=count))
        result = m << count
        return result

# 26~30对应二进制：11010 11011 11100 11101 11110
# 26~30按位与：11000（左边"11"公共部分）
print(Solution().rangeBitwiseAnd2(26, 30))
