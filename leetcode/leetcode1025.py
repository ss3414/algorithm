# ****************************************************************分割线****************************************************************
# todo 1025（Divisor Game）
# 除数博弈
# 每一回合选出n的因子x，然后用n-x代替n；尽可能使n接近1

class Solution:
    # 池沼算法（如果是奇数减一，如果是偶数取半）
    def divisorGame(self, n: int) -> bool:
        count = 0
        temp = []
        while n > 1:
            temp.append(n)
            if n % 2 == 1:
                n = n - 1
            else:
                n //= 2
            count += 1
        temp.append(n)
        print(temp)
        print(count)

    # fixme DP（如果n是偶数先手必赢，奇数必输）
    def divisorGame2(self, n: int) -> bool:
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

# print(Solution().divisorGame(100))
print(Solution().divisorGame2(9))
