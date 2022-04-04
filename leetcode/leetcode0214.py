# ****************************************************************分割线****************************************************************
# todo 0214（Shortest Palindrome）
# 最短回文字符串
# 如何在原字符串前添加字符，使其成为回文字符串

class Solution:
    # 暴力（超时）
    def shortestPalindrome(self, s: str) -> str:
        l = len(s)
        m = l // 2
        if s[0:m] == s[l - m:l][::-1]:
            return s
        i = m
        index = i
        match = 0
        flag = True
        while i > 0:
            j = 1
            while j <= i:
                if s[i - j:i] == s[i + 1:i + 1 + j][::-1] and i - j == 0 and j > match:  # 必须左边到头都是回文的
                    index = i
                    match = j
                    flag = True
                    print("{i} {j}".format(i=i, j=j))
                    print("{s1} {s2}".format(s1=s[i - j:i], s2=s[i + 1:i + 1 + j]))
                elif s[i - j:i] == s[i:i + j][::-1] and i - j == 0 and j > match:
                    index = i
                    match = j
                    flag = False
                    print("{i} {j}".format(i=i, j=j))
                    print("{s1} {s2}".format(s1=s[i - j:i], s2=s[i:i + j]))
                j += 1
            i -= 1

        # 要添加的字符串
        add = s[1:l][::-1]
        if index - match == 0:  # 必须左边到头都是回文的
            if flag:
                add = s[index + match + 1:l][::-1]
            else:
                add = s[index + match:l][::-1]
        return add + s

# print(Solution().shortestPalindrome("cdcba"))
# print(Solution().shortestPalindrome("cddca"))
# print(Solution().shortestPalindrome("ecdcbae"))
print(Solution().shortestPalindrome("abbabaab"))
