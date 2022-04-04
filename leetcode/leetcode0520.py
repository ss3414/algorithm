# ****************************************************************分割线****************************************************************
# todo 0520（Detect Capital）
# 检测大写字母

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        l = len(word)
        sum = 0
        for i in word:
            if 90 >= ord(i) >= 65:
                sum += 1
            elif 122 >= ord(i) >= 97:
                sum += 2
        if sum == l or sum == l * 2 or (sum == l * 2 - 1 and 90 >= ord(word[0]) >= 65):
            return True
        return False

# print(Solution().detectCapitalUse("USA"))
print(Solution().detectCapitalUse("Google"))
# print(Solution().detectCapitalUse("leetcode"))
