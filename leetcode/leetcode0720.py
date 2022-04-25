# ****************************************************************分割线****************************************************************
# todo 0720（Longest Word in Dictionary）
# 字典中最长的单词

class Solution:
    def longestWord(self, words: list) -> str:
        words.sort()  # 排序后为字典序
        data, result = {""}, ""
        for word in words:
            if word[:-1] in data:
                data.add(word)
                if len(word) > len(result):
                    result = word
        return result

# 如果有答案，输入的数组一定包含单字符单词
print(Solution().longestWord(["a", "ap", "app", "appl", "apple", "apply", "banana"]))
