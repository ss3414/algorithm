# ****************************************************************分割线****************************************************************
# todo 0374（Guess Number Higher or Lower）
# 猜数字大小

def guess(num: int) -> int:
    if num > 3:
        return -1
    elif num < 3:
        return 1
    elif num == 3:
        return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            middle = (left + right) // 2
            print("{l} {m} {r}".format(l=left, m=middle, r=right))
            if guess(middle) == -1:
                right = middle
            elif guess(middle) == 1:
                left = middle + 1
            elif guess(middle) == 0:
                return middle
        return left

print(Solution().guessNumber(10))
