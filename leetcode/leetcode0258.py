# ****************************************************************分割线****************************************************************
# todo 0258（Add Digits）
# 数根（各位相加，直到和为个位数）

class Solution:
    # 递归
    def addDigits(self, num: int) -> int:
        div = 10
        while num // div > 10:
            div *= 10
        sum = 0
        while div >= 1:
            digit = num // div
            sum += digit
            num -= digit * div
            div //= 10
        if sum < 10:
            return sum
        return self.addDigits(sum)

    # 规律（从1开始，每个数的数根每隔9循环一次）
    def addDigits2(self, num: int) -> int:
        if num == 0:
            return 0
        # 如果num为9，数根也为9，将num减一再取余再加一
        return (num - 1) % 9 + 1

# print(Solution().addDigits(58))
print(Solution().addDigits2(58))
