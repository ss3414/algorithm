# ****************************************************************分割线****************************************************************
# todo 0409（Longest Palindrome）
# 构造最长回文字符串

class Solution:
    def longestPalindrome(self, s: str) -> int:
        data = {}
        for i in s:
            if i in data.keys():
                data[i] = data[i] + 1
            else:
                data[i] = 1
        sum = 1
        for key, val in data.items():
            if val % 2 == 0:
                sum += val
            else:
                sum += (val - 1)  # 奇数字符减一也能构成回文
        if sum > len(s):
            return sum - 1  # 若全为偶数字符，sum减一
        else:
            return sum

print(Solution().longestPalindrome("abccccdd"))
