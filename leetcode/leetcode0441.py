# ****************************************************************分割线****************************************************************
# todo 0441（Arranging Coins）
# 排列硬币

class Solution:
    # 暴力
    def arrangeCoins(self, n: int) -> int:
        i = 1
        while n >= i:
            n -= i
            i += 1
            # print("{n} {i}".format(n=n,i=i))
        return i - 1

    # 二分法+等差数列前n项和
    def arrangeCoins2(self, n: int) -> int:
        if n <= 1:
            return n

        left, right = 1, n
        while left < right:
            middle = (left + right) // 2
            if middle * (middle + 1) // 2 <= n:
                left = middle + 1
            else:
                right = middle
        return left - 1

# print(Solution().arrangeCoins(1))
print(Solution().arrangeCoins2(10))
