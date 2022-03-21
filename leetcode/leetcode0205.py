# ****************************************************************分割线****************************************************************
# todo 0205（Isomorphic Strings）
# 同构字符串

# 哈希表
def test(s: str, t: str):
    s1 = ""
    data = {}
    count = 0
    i = 0
    while i < len(s):
        if data.get(s[i]) is None:
            data.update({s[i]: count})
            count += 1
        s1 = s1 + "{str} ".format(str=str(data.get(s[i])))
        i += 1

    s2 = ""
    data = {}
    count = 0
    i = 0
    while i < len(t):
        if data.get(t[i]) is None:
            data.update({t[i]: count})
            count += 1
        s2 = s2 + "{str} ".format(str=str(data.get(t[i])))
        i += 1

    print("s1:{s1} s2:{s2}".format(s1=s1, s2=s2))
    return s1 == s2

# 字符对应
def test2(s: str, t: str):
    s1, s2 = {}, {}
    i = 0
    while i < len(s):
        # ②若出现字符不对应则不是同构字符串
        if s[i] in s1 and s1[s[i]] != t[i]:
            return False
        if t[i] in s2 and s2[t[i]] != s[i]:
            return False
        # ①把字符按顺序一一对应
        s1[s[i]] = t[i]
        s2[t[i]] = s[i]
        i += 1
    print("s1:{s1} s2:{s2}".format(s1=s1, s2=s2))
    return True

# print(test("foo","bar"))
# print(test("bbbaaaba","aaabbbba"))
# print(test("abcdefghijklmnopqrstuvwxyzva","abcdefghijklmnopqrstuvwxyzck"))

print(test2("abcdefghijklmnopqrstuvwxyzva", "abcdefghijklmnopqrstuvwxyzck"))
