# ****************************************************************分割线****************************************************************
# todo 0557（Reverse Words in a String III）
# 反转字符串中的单词III

class Solution:
    def reverseWords(self, s: str) -> str:
        chars = list(s + " ")
        l = len(chars)
        i = 0
        left = l
        flag = True
        while i < l:
            if chars[i] != " " and flag:
                left = i
                flag = False
            if chars[i] == " " and i > left:
                chars[left:i] = reversed(chars[left:i])
                flag = True
            i += 1
        return "".join(chars)[0:l - 1]

print(Solution().reverseWords("Let's take LeetCode contest"))
