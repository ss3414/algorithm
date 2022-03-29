# ****************************************************************分割线****************************************************************
# todo 0344（Reverse String）
# 反转字符串

class Solution:
    def reverseString(self, s: list) -> None:
        l = len(s)
        m = l
        if l % 2 == 1:
            m = l // 2
        else:
            m = (l // 2) - 1
        i = 0
        while i <= m:
            temp = s[l - i - 1]
            s[l - i - 1] = s[i]
            s[i] = temp
            i += 1
        # print(s)

print(Solution().reverseString(["h", "e", "l", "l", "o"]))
# print(Solution().reverseString(["w","o","r","d"]))
