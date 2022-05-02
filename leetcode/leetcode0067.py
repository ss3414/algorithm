# ****************************************************************分割线****************************************************************
# todo 0067（Add Binary）
# 二进制求和

class Solution:
    # 数组
    def addBinary(self, a: str, b: str) -> str:
        sum = list(str(int(a) + int(b)))
        i = len(sum) - 1
        while i > 0:
            if sum[i] == "2":
                sum[i] = "0"
                sum[i - 1] = str(int(sum[i - 1]) + 1)
            if sum[i] == "3":
                sum[i] = "1"
                sum[i - 1] = str(int(sum[i - 1]) + 1)
            # print(sum[i])
            i -= 1
        if sum[0] == "2":
            sum[i] = "0"
            return "1" + "".join(sum)
        if sum[0] == "3":
            sum[i] = "1"
            return "1" + "".join(sum)
        return "".join(sum)

    # fixme 数学
    def addBinary2(self, a: str, b: str) -> str:
        length1, length2 = -len(a), -len(b)
        i, carry, result = -1, 0, ""  # carry是每位数的进位
        while i >= length1 or i >= length2:
            bit1 = int(a[i]) if i >= length1 else 0  # 判断此位是否存在
            bit2 = int(b[i]) if i >= length2 else 0
            sum = bit1 + bit2 + carry
            result = str(sum % 2) + result
            carry = sum // 2
            i -= 1
        return "1" + result if carry else result

print(Solution().addBinary("111", "111"))
print(Solution().addBinary2("111", "111"))
