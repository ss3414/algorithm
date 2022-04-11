# ****************************************************************分割线****************************************************************
# todo 1979（Find Greatest Common Divisor of Array）
# 最大公约数

class Solution:
    # 暴力（慢）
    def findGCD(self, nums: list) -> int:
        max_val = max(nums)
        min_val = min(nums)
        if max_val % min_val == 0:
            return min_val
        i = min_val // 2
        while max_val % i != 0 or min_val % i != 0:
            i -= 1
        return i

    # 辗转相除法
    def findGCD2(self, nums: list) -> int:
        max_val = max(nums)
        min_val = min(nums)
        while min_val:
            max_val, min_val = min_val, max_val % min_val
            print("{max} {min}".format(max=max_val, min=min_val))
        return max_val

# print(Solution().findGCD([6, 8]))
print(Solution().findGCD2([6, 8]))
