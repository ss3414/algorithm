# ****************************************************************分割线****************************************************************
# todo 0202（Happy Number）
# 判断一个数是否为快乐数
# 19
# 1^2+9^2=82
# 8^2+2^2=68
# 6^2+8^2=100
# 1^2+0^2+0^2=1
# 循环直至只剩1时为快乐数

# 按顺序返回n的位数
def digit(n):
    div = 1
    while n / div >= 10:  # n的位数
        div *= 10
    digits = []
    while n > 0:
        temp = int(n // div)
        digits.append(temp)
        n -= temp * div
        div /= 10
    return digits

# 哈希表
def test(n: int):
    digits = digit(n)
    data = {}
    while len(digits) > 0:
        if len(digits) == 1 and digits[0] == 1:
            return True

        n = 0
        i = 0
        while i < len(digits):
            n += digits[i] ** 2
            i += 1

        print("n:{n} digits:{digits}".format(n=n, digits=digits))
        count = data.get(n)
        if count is None:
            data.update({n: 1})
        else:  # 如果n重复出现则说明进入死循环（死循环用是否重复来判断）
            return False

        digits = digit(n)

# print(test(19))
print(test(11))  # 4会重复出现
