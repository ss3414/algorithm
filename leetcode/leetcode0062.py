# ****************************************************************分割线****************************************************************
# todo 0062（Unique Paths）
# 不同路径

import math

class Solution:
    # 排列组合
    # 右移m-1步，下移n-1步，共需要m-1+n-1=m+n-2步，即C(m+n-2,m-1)或C(m+n-2,n-1)
    # C(m+n-2,m-1)=C(m+n-2,n-1)=(m+n-2)!/(m+n-2-m+1)!*(m-1)!=(m+n-2)!/(n-1)!*(m-1)!
    def uniquePaths(self, m, n):
        return math.factorial(m + n - 2) // (math.factorial(m - 1) * math.factorial(n - 1))

print(Solution().uniquePaths(3, 7))
