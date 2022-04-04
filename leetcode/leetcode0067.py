# ****************************************************************分割线****************************************************************
# todo 0067（Add Binary）
# 二进制求和

# 数组
def test(a: str, b: str):
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
def test2(a: str, b: str):
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

# print(test("111", "111"))
print(test2("111", "111"))
