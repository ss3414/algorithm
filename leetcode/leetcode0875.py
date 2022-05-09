# ****************************************************************分割线****************************************************************
# todo 0875（Koko Eating Bananas）
# 可可爱吃香蕉

import math

class Solution:
    # 枚举
    def minEatingSpeed(self, piles: list, h: int) -> int:
        def possible(l):
            t = 0
            for pile in piles:
                t += math.ceil(pile / l)
            return t <= h

        l, r = 1, max(piles)  # 解空间
        while l <= r:
            print("l:{l} p:{p}".format(l=l, p=possible(l)))
            if possible(l):
                return l
            l += 1
        return r

    # 二分法
    # 解空间为[1,max(piles)]，是一个有序序列，piles.length<=h，最极端情况需要以max(piles)的速度吃香蕉
    def minEatingSpeed2(self, piles: list, h: int) -> int:
        def possible(mid):
            t = 0
            for pile in piles:
                t += math.ceil(pile / mid)
            return t <= h

        l, r = 1, max(piles)  # 解空间
        while l <= r:
            mid = (l + r) // 2
            print("l:{l} m:{m} r:{r} p:{p}".format(l=l, r=r, m=mid, p=possible(mid)))
            if possible(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l  # 最左插入，能满足条件的最小（最左）解

# print(Solution().minEatingSpeed([3,6,7,11], 8))
print(Solution().minEatingSpeed2([3, 6, 7, 11], 8))
