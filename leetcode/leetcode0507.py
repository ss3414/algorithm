# ****************************************************************分割线****************************************************************
# todo 0507（Perfect Number）
# 完美数

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sum = 1
        i = 2
        while i * i <= num:
            if num % i == 0:
                # 把num不相同的因子加起来
                sum += i + (0 if num // i == 0 else num // i)
            i += 1
        return sum == num and num != 1

# print(Solution().checkPerfectNumber(28))
print(Solution().checkPerfectNumber(1))
