# ****************************************************************分割线****************************************************************
# todo 0367（Valid Perfect Square）
# 有效的完全平方数

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True

        left = 0
        right = num
        middle = num // 2
        while right - left > 1:
            if middle ** 2 > num:
                right = middle
            elif middle ** 2 <= num:
                left = middle
            middle = (left + right) // 2
            print("left:{left} right:{right} middle:{middle}".format(left=left, right=right, middle=middle))
        return num == left ** 2 or num == right ** 2

# print(Solution().isPerfectSquare(16))
print(Solution().isPerfectSquare(14))
