# ****************************************************************分割线****************************************************************
# todo 0405（Convert a Number to Hexadecimal）
# 十进制转十六进制

class Solution:
    # 池沼算法（无法处理负数）
    def toHex(self, num: int) -> str:
        stack = [num]
        m = num // 16
        while m > 0:
            num = stack.pop()
            n = num % 16
            stack.append(n)
            num = m
            stack.append(num)
            m = num // 16
        result = ""
        while stack:
            digit = stack.pop()
            if digit > 9:
                digit = chr(digit - 10 + 97)
            result += str(digit)
        return result

    # 位运算
    # num取值范围-2**31~2**31-1，对应十六进制80000000~7fffffff，负数用补码表示
    # 注意num取值不能超过2**31-1，否则溢出就会变成负数
    def toHex2(self, num: int) -> str:
        if num == 0:
            return "0"
        data = "0123456789abcdef"
        result = ""
        for i in range(8):
            n = num & 15  # fixme 负数的位运算
            c = data[n]
            result = c + result
            num >>= 4
        return result.lstrip("0")

# print(Solution().toHex(4095))
print(Solution().toHex2((2 ** 31) - 1))
print(Solution().toHex2(-(2 ** 31)))
print(Solution().toHex2(-1))
