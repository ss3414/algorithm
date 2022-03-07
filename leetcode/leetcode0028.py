# ****************************************************************分割线****************************************************************
# todo 0028（Implement strStr()）
# 取字符串中第一个符合条件子串下标，Java中indexOf()方法

# 池沼算法
def test(haystack: str, needle: str):
    if needle == "":
        return 0  # 子串为空

    index = -1  # 没找到
    i = 0
    j = 0
    # 两个字符串下标前进
    while i < len(haystack):
        if haystack[i] == needle[j]:
            print("haystack:{i} needle:{j}".format(i=haystack[0:i + 1], j=needle[0:j + 1]))
            if j == len(needle) - 1:
                index = i - j  # 找到
                break
            j += 1
        i += 1
    return index

def test2(haystack: str, needle: str):
    i = 0
    while i < len(haystack) - len(needle) + 1:  # 这里加1是为了应对两字符串都为空的情况，即使都为空也算找到
        if haystack[i:i + len(needle)] == needle:
            # print("i:{i} haystack:{haystack}".format(i=i,haystack=haystack[i:i+len(needle)]))
            return i  # 找到
        i += 1
    return -1  # 没找到

print(test("mississippi", "issipi"))
# print(test("",""))
# print(test("a",""))
# print(test("","b"))

# print(test2("",""))
# print(test2("a",""))
# print(test2("","b"))
