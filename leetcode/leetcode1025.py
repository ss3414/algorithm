# ****************************************************************分割线****************************************************************
# todo 1025（Divisor Game）
# 除数博弈
# 每一回合选出n的因子x，然后用n-x代替n；尽可能使n接近1

class Solution:
    # fixme DP（如果n是偶数先手必赢，奇数必输）
    def divisorGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        i = 2
        while i <= n:
            for j in range(1, i):
                if i % j != 0:
                    continue
                if not dp[i - j]:
                    dp[i] = True
                    break
            i += 1
        print(dp)
        return dp[n]

print(Solution().divisorGame(9))
