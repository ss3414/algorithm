# ****************************************************************分割线****************************************************************
# todo 0412（Fizz Buzz）
# 能被3整除返回Fizz，能被5整除返回Buzz，既能被3又能被5返回FizzBuzz

class Solution:
    def fizzBuzz(self, n: int) -> list:
        result = []
        i = 1
        while i <= n:
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0 and i % 5 != 0:
                result.append("Fizz")
            elif i % 3 != 0 and i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
            i += 1
        return result

print(Solution().fizzBuzz(15))
