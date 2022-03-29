# ****************************************************************分割线****************************************************************
# todo 0415（Add Strings）
# 字符串相加

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = ""
        l1, l2 = len(num1) - 1, len(num2) - 1
        carry = "0"  # 进位
        while l1 >= 0 or l2 >= 0:
            x = num1[l1] if l1 > -1 else "0"
            y = num2[l2] if l2 > -1 else "0"
            temp = ord(x) + ord(y) + ord(carry)
            # print("{x}+{y}+{c}={t}".format(x=ord(x),y=ord(y),c=ord(carry),t=temp))
            carry = "0"
            # ASCII码0~9对应48~57，0+0~18+0对应144~162，大于153代表有进位，temp多减去一个10
            if temp > 153:
                carry = "1"
                temp -= 10
            temp -= (48 * 2)
            result += chr(temp)
            # print("{t} {r}".format(t=temp,r=result))
            l1 -= 1
            l2 -= 1
        if carry != "0":
            result += carry
        return result[::-1]

# print(Solution().addStrings("12","123"))
print(Solution().addStrings("1", "9"))
