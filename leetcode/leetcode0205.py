# ****************************************************************分割线****************************************************************
# todo 0205（Isomorphic Strings）
# 同构字符串

class Solution:
    # 哈希表
    def isIsomorphic(self, s: str, t: str) -> bool:
        s1 = ""
        data = {}
        count = 0
        i = 0
        while i < len(s):
            if data.get(s[i]) is None:
                data[s[i]] = count
                count += 1
            s1 = s1 + "{str} ".format(str=str(data.get(s[i])))
            i += 1

        s2 = ""
        data = {}
        count = 0
        i = 0
        while i < len(t):
            if data.get(t[i]) is None:
                data[t[i]] = count
                count += 1
            s2 = s2 + "{str} ".format(str=str(data.get(t[i])))
            i += 1

        print("s1:{s1} s2:{s2}".format(s1=s1, s2=s2))
        return s1 == s2

    # 字符对应
    def isIsomorphic2(self, s: str, t: str) -> bool:
        s1, s2 = {}, {}
        i = 0
        while i < len(s):
            # ②如果出现字符不对应则不是同构字符串
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

print(Solution().isIsomorphic("foo", "bar"))
print(Solution().isIsomorphic("bbbaaaba", "aaabbbba"))
print(Solution().isIsomorphic("abcdefghijklmnopqrstuvwxyzva", "abcdefghijklmnopqrstuvwxyzck"))
print(Solution().isIsomorphic2("abcdefghijklmnopqrstuvwxyzva", "abcdefghijklmnopqrstuvwxyzck"))
