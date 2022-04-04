# ****************************************************************分割线****************************************************************
# todo 0504（Base 7）
# 七进制

class Solution:
    # 栈
    def convertToBase7(self, num: int) -> str:
        result = ""
        if num < 0:
            result += "-"

        num = abs(num)
        stack = [num]
        m = num // 7
        while m > 0:
            num = stack.pop()
            n = num % 7
            stack.append(n)
            num = m
            stack.append(num)
            m = num // 7
        while stack:
            result += str(stack.pop())
        return result

    # 数学
    def convertToBase72(self, num: int) -> str:
        n, result = abs(num), ""
        while n:
            result = str(n % 7) + result
            print(result)
            n //= 7
        return "-" * (num < 0) + result or "0"

# print(Solution().convertToBase7(-7))
print(Solution().convertToBase72(-70))
