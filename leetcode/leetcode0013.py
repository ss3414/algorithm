# ****************************************************************分割线****************************************************************
# todo 0013（Roman to Integer）
# 罗马数字转阿拉伯数字

# 罗马数字范围（1~4999）
# I/V/X/L/C/D/M（1/5/10/50/100/500/1000）
# M/MM/MMM（1000~3000）
# D/DC/DCC/DCCC（500~800）
# C/CC/CCC/CD/CM（100~400，900）
# L/LX/LXX/LXXX（50~80）
# X/XX/XXX/XL/XC（10~40，90）
# V/VI/VII/VIII（5~8）
# I/II/III/IV/IX（1~4，9）
def test(s):
    data = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    digits = list(s)
    i = 0
    total = 0
    while i < len(digits):
        value = data[digits[i]]
        # 罗马数字规律，左边的数字大于等于右边则为正，反之为负
        if i == len(digits) - 1 or data[digits[i]] >= data[digits[i + 1]]:
            total += value
        else:
            total -= value
        i += 1
        print(total)
    return total

print(test("MMMCMXCIX"))
