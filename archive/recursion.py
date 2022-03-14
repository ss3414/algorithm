# ****************************************************************分割线****************************************************************
# todo 递归

# 递归求斐波那契数列前10项
# 斐波那契数列：从第3项开始，每一项等于前两项之和
# ① 1 f(1)
# ② 1 f(2)
# ③ 2 f(3)=f(2)+f(1)
# ④ 3 f(4)=f(3)+f(2)
# 递归的核心：自己调用自己
# 缺点：从第3项开始，每一项会把求过的结果再求一遍，浪费时间

# 递归
def recursion(i):
    if i < 3:
        return 1
    else:
        return recursion(i - 1) + recursion(i - 2)

# 动态规划（凡是递归都能用动态规划改写）
def dp(i):
    if i < 3:
        return 1

    elements = [0] * i
    elements[0] = 1
    elements[1] = 1
    j = 2
    while j < i:
        elements[j] = elements[j - 1] + elements[j - 2]
        j += 1
        print(elements)
    return elements[i - 1]

print(recursion(10))
# print(dp(10))
