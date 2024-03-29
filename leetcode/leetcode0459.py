# ****************************************************************分割线****************************************************************
# todo 0459（Repeated Substring Pattern）
# 重复的子串

class Solution:
    # 池沼算法
    def repeatedSubstringPattern(self, s: str) -> bool:
        sub = s[0]
        i = 1
        while i < len(s):
            l = len(sub)
            print("{str1} {str2}".format(str1=s[0:l], str2=s[l:2 * l]))
            if s[0:l] != s[l:2 * l]:
                sub += s[i]
            i += 1

        l = len(sub)
        if len(s) == l or len(s) % l != 0:
            return False
        start = 0
        while start + 2 * l <= len(s):
            if s[start:start + l] != s[(start + l):(start + 2 * l)]:
                return False
            start += l
        return True

    def repeatedSubstringPattern2(self, s: str) -> bool:
        l = len(s)
        i = l // 2  # 子串至少重复两次，至多1/2原字符串长度
        while i >= 1:
            if l % i == 0:  # 如果i能被l整除，测试j个i是否等于原字符串
                j = l // i
                temp = ""
                while j > 0:
                    temp += s[0:i]
                    j -= 1
                if temp == s:
                    return True
            i -= 1
        return False

# print(Solution().repeatedSubstringPattern("abaaabaa"))
# print(Solution().repeatedSubstringPattern("abcde"))
# print(Solution().repeatedSubstringPattern("abaababaab"))
print(Solution().repeatedSubstringPattern2("abaababaab"))
