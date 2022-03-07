# ****************************************************************分割线****************************************************************
# todo 0014（Longest Common Prefix）
# 寻找最长相同前缀，若没有返回""

# 字符串两两比较
def test(strs):
    i = 0
    prefix = strs[0]
    while i < len(strs) - 1:
        j = 0
        temp = ""
        while j < len(prefix) and j < len(strs[i + 1]):
            if prefix[j] == strs[i + 1][j]:
                temp = prefix[0:(j + 1)]
                print(temp)
            else:
                break
            j += 1
        prefix = temp
        i += 1
    return prefix

# fixme 把字符串数组当做二维字符数组
def test2(strs):
    i = 0
    while i < len(strs[0]):
        j = 1
        while j < len(strs):
            if i < len(strs[j]) and strs[0][0:i] != strs[j][0:i]:
                return strs[0][0:i - 1]
            elif i == len(strs[j]):
                return strs[0][0:i]
            j += 1
        i += 1
    return strs[0]  # 循环跑完仍未发现更长前缀，strs[0]就是最长前缀

# print(test(["flow","flower","flight"]))
# print(test(["ab","a"]))

# print(test2(["flow","flower","flight"]))
# print(test2(["ab","a"]))
print(test2(["a", "b"]))
