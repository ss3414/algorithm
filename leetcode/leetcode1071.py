# ****************************************************************分割线****************************************************************
# todo 1071（Greatest Common Divisor of Strings）
# 字符串最大公因子

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1), len(str2)
        s1, s2 = "", ""
        data1, data2 = [], []
        for i in range(l1):
            s1 += str1[i]
            if l1 % len(s1) == 0:
                if str1 == l1 // len(s1) * s1:
                    data1.append(s1)
        for i in range(l2):
            s2 += str2[i]
            if l2 % len(s2) == 0:
                if str2 == l2 // len(s2) * s2:
                    data2.append(s2)
        result = ""
        for j in data1:
            if j in data2 and len(j) >= len(result):
                result = j
        return result

print(Solution().gcdOfStrings("ABABAB", "ABAB"))
