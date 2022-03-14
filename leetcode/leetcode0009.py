# ****************************************************************分割线****************************************************************
# todo 0009（Palindrome Number）
# 回文数

# 转换成字符串
def test(x):
    if x < 0:
        return False
    digits = list(str(x))
    i = 0
    length = len(digits)
    while i < int(round(length / 2)):
        if digits[i] != digits[length - i - 1]:
            return False
        i += 1
    return True

# 不转换成字符串
def test2(x):
    if x < 0:
        return False
    div = 1
    while x / div >= 10:  # 把div放大到x的最大位数
        div *= 10
    while x > 0:
        left = x // div
        right = x % 10
        print("left:{left} right:{right}".format(left=left, right=right))
        if left != right:
            return False
        x = (x % div) // 10  # 取x中间数，x=12321，中间数=232
        div /= 100  # div缩小两位数
        print("x:{x} div:{div}".format(x=x, div=div))
    return True

# print(test(121))
# print(test(-121))
# print(test(0))
# print(test(1221))

print(test2(12321))
