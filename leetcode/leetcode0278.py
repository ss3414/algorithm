# ****************************************************************分割线****************************************************************
# todo 0278（First Bad Version）
# 第一个错误版本

import math

def isBadVersion(version: int) -> bool:
    if version >= 20:
        return True
    else:
        return False

class Solution:
    def firstBadVersion(self, n: int) -> int:
        end = n
        start = n // 2
        while start != end:
            # print("{b} {e}".format(b=start,e=end))
            if isBadVersion(start):
                end = start
                start = math.ceil(start / 2)
            else:
                start += math.ceil((end - start) / 2)
        return start

    # firstBadVersion简化版
    def firstBadVersion2(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            middle = (left + right) // 2
            print("{l} {m} {r}".format(l=left, m=middle, r=right))
            if isBadVersion(middle):
                right = middle
            else:
                left = middle + 1
        return left

# print(Solution().firstBadVersion(30))
print(Solution().firstBadVersion2(30))
