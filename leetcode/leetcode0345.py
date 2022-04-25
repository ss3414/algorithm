# ****************************************************************分割线****************************************************************
# todo 0345（Reverse Vowels of a String）
# 反转元音字母

class Solution:
    def reverseVowels(self, s: str) -> str:
        def test(c):
            if c in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                return True
            return False

        result = [""] * len(s)
        i, j = 0, len(s) - 1
        while i <= j:
            if not test(s[i]):
                result[i] = s[i]
                i += 1
            if not test(s[j]):
                result[j] = s[j]
                j -= 1
            if i <= j and test(s[i]) and test(s[j]):
                result[i] = s[j]
                result[j] = s[i]
                i += 1
                j -= 1
        return "".join(result)

print(Solution().reverseVowels("leetcode"))
