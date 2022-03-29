# ****************************************************************分割线****************************************************************
# todo 0290（Word Pattern）
# 单词规律

class Solution:
    # 太慢
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        data = {}
        i = 0
        while i < len(pattern):
            words[i] += "@"  # 避免key/val重名
            if (pattern[i] in data.keys() and data[pattern[i]] != words[i]) or (words[i] in data.keys() and data[words[i]] != pattern[i]):
                return False
            data.update({pattern[i]: words[i]})
            data.update({words[i]: pattern[i]})
            i += 1
        return True

# print(Solution().wordPattern("abba","dog dog dog dog"))
# print(Solution().wordPattern("aaaa","dog cat cat dog"))
print(Solution().wordPattern("abc", "b c a"))
