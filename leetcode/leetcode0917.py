# ****************************************************************分割线****************************************************************
# todo 0917（Reverse Only Letters）
# 只逆序字母

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        stack = []
        s = list(s)
        for i in s:
            if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
                stack.append(i)
        j = 0
        while j < len(s):
            if 65 <= ord(s[j]) <= 90 or 97 <= ord(s[j]) <= 122:
                s[j] = stack.pop()
            j += 1
        return "".join(s)

print(Solution().reverseOnlyLetters("a-b"))
