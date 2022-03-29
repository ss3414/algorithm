# ****************************************************************分割线****************************************************************
# todo 0171（Excel Sheet Column Number）
# Excel列转换成数字

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        digit = len(columnTitle)
        for i in columnTitle:
            result += (ord(i) - 64) * 26 ** (digit - 1)
            digit -= 1
        return result

print(Solution().titleToNumber("AZ"))
