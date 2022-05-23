# ****************************************************************分割线****************************************************************
# todo 0680（Valid Palindrome II）
# 验证回文字符串II

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def test(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return test(l + 1, r) or test(l, r - 1)
            l += 1
            r -= 1
        return True

print(Solution().validPalindrome("aaabbcaaa"))
