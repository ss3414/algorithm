# ****************************************************************分割线****************************************************************
# todo 0509（Fibonacci Number）
# 斐波那契数列

class Solution:
    # 递归
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)

    # DP
    def fib2(self, n: int) -> int:
        if n == 0:
            return 0
        dp = [None] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        i = 2
        while i < n + 1:
            dp[i] = dp[i - 1] + dp[i - 2]
            i += 1
        return dp[n]

# print(Solution().fib(6))
print(Solution().fib2(6))
