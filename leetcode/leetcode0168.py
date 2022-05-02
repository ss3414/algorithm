# ****************************************************************分割线****************************************************************
# todo 0168（Excel Sheet Column Title）
# Excel列的名称
# A代表1，AA代表26+1，AAA代表1*26^2+1*26^1+1*26^0

class Solution:
    # 池沼算法
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        digits = []
        while columnNumber > 26:
            r = columnNumber % 26
            digits.append(r)
            columnNumber = columnNumber // 26
        digits.append(columnNumber)
        # print(digits)
        while digits:
            result += chr(64 + digits.pop())
        return result

    # 池沼算法（52可以用B或AZ表计，但B又等于2）
    def convertToTitle2(self, columnNumber: int) -> str:
        result = ""
        digit = 1
        temp = columnNumber
        while temp // 26 != 0:
            temp = temp // 26
            digit += 1
        while digit > 0:
            q = columnNumber // 26 ** (digit - 1)
            result += chr(64 + q)
            columnNumber = columnNumber - q * 26 ** (digit - 1)
            digit -= 1
        return result

    # fixme 数学
    def convertToTitle3(self, columnNumber: int) -> str:
        result = ""
        while columnNumber:
            # print(columnNumber)
            if columnNumber % 26 == 0:
                result += "Z"
                columnNumber -= 26
            else:
                result += chr(columnNumber % 26 - 1 + 65)
                columnNumber -= (columnNumber % 26)
            columnNumber //= 26
        return result[::-1]

# print(Solution().convertToTitle(800))
# print(Solution().convertToTitle2(52))
print(Solution().convertToTitle3(52))
