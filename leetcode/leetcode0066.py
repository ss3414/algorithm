# ****************************************************************分割线****************************************************************
# todo 0066（Plus One）
# 加一

# 加法进位和数组扩容
def test(digits: list):
    i = len(digits) - 1
    while i >= 0:
        digits[i] = digits[i] + 1
        if digits[i] == 10:
            digits[i] = 0
        else:
            break
        # print(digits)
        i -= 1
    if len(digits) > 0 and digits[0] == 0:
        return [1, 0] + digits[1:len(digits)]
    return digits

print(test([1, 2, 3]))
# print(test([9,9,9]))
