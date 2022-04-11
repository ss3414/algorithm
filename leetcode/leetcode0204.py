# ****************************************************************分割线****************************************************************
# todo 0204（Count Primes）
# 数质数

class Solution:
    # 埃拉托斯特尼筛法（慢）
    def countPrimes(self, n: int) -> int:
        result = 0
        primes = [True] * n
        for i in range(2, n):
            if not primes[i]:  # 如果不是质数直接跳过
                continue
            result += 1  # 如果是质数加一，并翻转质数的倍数
            j = 2
            while i * j < n:
                primes[i * j] = False
                j += 1
        # print(primes)
        return result

    # 利用Python特性，countPrimes的优化版（快）
    def countPrimes2(self, n: int) -> int:
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):  # 2~√n+1
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
                # print(primes)
        return sum(primes)

# print(Solution().countPrimes(10))
print(Solution().countPrimes2(10))
