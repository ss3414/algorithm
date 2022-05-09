# ****************************************************************分割线****************************************************************
# todo 0166（Fraction to Recurring Decimal）
# 分数到小数

class Solution:
    # 池沼算法
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator // denominator)

        temp = str(numerator / denominator)
        digits = temp.split(".")
        right = digits[1]  # 小数点后半段
        data = {}
        i = 0
        while i < len(right):
            if right[i] in data:
                return "0.({d})".format(d=right[0:i])
            else:
                data[right[i]] = 1
            i += 1
        return temp

    def fractionToDecimal2(self, numerator: int, denominator: int) -> str:
        sign = ""
        if numerator * denominator < 0:
            sign = "-"

        numerator = abs(numerator)
        denominator = abs(denominator)

        q, r = divmod(numerator, denominator)  # 商/余数
        if r == 0:
            return sign + str(q)

        result = str(q) + "."
        stack = []
        data = []
        print("q:{q} r:{r}".format(q=q, r=r))

        # 通过栈统计循环小数
        while r not in stack:
            stack.append(r)
            temp = r * 10
            q, r = divmod(temp, denominator)
            print("t:{t} d:{d} q:{q} r:{r}".format(t=temp, d=denominator, q=q, r=r))
            data.append(str(q))

        print(stack)
        print(data)
        if r in stack and r != 0:
            index = stack.index(r)
            data.insert(index, "(")
            data.append(")")
        else:
            data.pop()
        return sign + result + "".join(data)

# print(Solution().fractionToDecimal(1, 6))
# print(Solution().fractionToDecimal(4, 333))
# print(Solution().fractionToDecimal2(1, 6))
print(Solution().fractionToDecimal2(4, 333))
