# ****************************************************************分割线****************************************************************
# todo 0069（Sqrt(x)）
# x的平方根

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1

        left = 0
        right = x
        middle = x // 2
        while right - left > 1:  # 平方根落在相差为1的区间内
            if middle ** 2 > x:
                right = middle
            elif middle ** 2 <= x:
                left = middle
            middle = (left + right) // 2
            print("left:{left} right:{right} middle:{middle}".format(left=left, right=right, middle=middle))
        return left

print(Solution().mySqrt(9))
print(Solution().mySqrt(1))
