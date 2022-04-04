# ****************************************************************分割线****************************************************************
# todo 0070（Climbing Stairs）
# 爬楼梯

# 池沼算法（无法计算排列组合）
def test(n: int):
    count = 0
    i = 0
    while i <= n:
        j = 0
        while j <= n:
            if i + j == n:
                print("i:{i} j:{j}".format(i=i, j=j))
                count += 1
            j += 2
        i += 1
    return count

# 难点在于怎么把题目抽象成斐波那契数列
# 1层楼梯，1种可能性（1）
# 2层楼梯，2种可能性（11+2）
# 3层楼梯，3种可能性（111+21+12）；3层楼梯相当于在2层基础上加一层，在1层基础上加两层；
# 在2层的所有可能性后面加1+在1层可能性后面加2=3层的所有可能性
def test2(n: int):
    if n <= 1:
        return 1

    # 斐波那契数列，前两项为1和2
    dp = [0] * n
    dp[0] = 1
    dp[1] = 2
    i = 2
    while i < n:
        dp[i] = dp[i - 1] + dp[i - 2]
        print("{i1}={i2}+{i3}".format(i1=dp[i], i2=dp[i - 1], i3=dp[i - 2]))
        i += 1
    return dp[i - 1]

# 记忆化搜索（递归+记忆数组）
def test3(n: int, memo: list):
    print("n:{n} memo:{memo}".format(n=n, memo=memo))
    if n <= 1:
        return 1
    if memo[n] is not None:  # 记忆数组，避免重复计算
        return memo[n]
    memo[n] = test3(n - 1, memo) + test3(n - 2, memo)
    return memo[n]

# print(test(4))

print(test2(4))

n = 4
memo = [0] * (n + 1)
# print(test3(n, memo))
