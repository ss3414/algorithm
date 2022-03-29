# ****************************************************************分割线****************************************************************
# todo 1137（N-th Tribonacci Number）
# 三阶斐波那契数列

class Solution:
    # DP
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        result = [0, 1, 1]
        i = 3
        while i <= n:
            result.append(result[i - 1] + result[i - 2] + result[i - 3])
            i += 1
        return result[n]

print(Solution().tribonacci(4))
