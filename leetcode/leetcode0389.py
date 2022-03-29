# ****************************************************************分割线****************************************************************
# todo 0389（Find the Difference）
# 字符串找不同
# t由s随机重排并添加一个字符

class Solution:
    # 池沼算法
    def findTheDifference(self, s: str, t: str) -> str:
        if s == "":
            return t
        i = 0
        while i < len(s):
            if s[i] != t[i]:
                return t[i]
            i += 1
        return t[len(s)]

    # 哈希表
    def findTheDifference2(self, s: str, t: str) -> str:
        data = {}
        for i in s:
            if i in data.keys():
                data.update({i: data[i] + 1})
            else:
                data.update({i: 1})
        for i in t:
            if i in data.keys():
                data.update({i: data[i] - 1})
            else:
                data.update({i: 1})
        print(data)
        for key, val in data.items():
            if val == 1 or val == -1:
                return key

    # 异或（位运算）
    def findTheDifference3(self, s: str, t: str) -> str:
        result = 0
        for i in s:
            result ^= ord(i)
            print("{i}:{result}".format(i=i, result=result))
        for j in t:
            result ^= ord(j)
            print("{j}:{result}".format(j=j, result=result))
        return chr(result)

# print(Solution().findTheDifference("abcd","abcde"))
# print(Solution().findTheDifference2("a","aa"))
print(Solution().findTheDifference3("abcd", "bdace"))
