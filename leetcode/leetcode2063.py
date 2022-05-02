# ****************************************************************分割线****************************************************************
# todo 2063（Vowels of All Substrings）
# 统计子串中的元音字母数量
# 子串必须连续

class Solution:
    def __init__(self, data={}):
        self.data = data

    # 池沼算法（组合出的随机子串和真子串以及真子串本身可能重复）
    def countVowels(self, word: str) -> int:
        def test(char):
            return char.count("a") + char.count("e") + char.count("i") + char.count("o") + char.count("u")

        def dfs(word: str, i: int, son: str):
            if i == len(word):
                if word.count(son) > 0:
                    self.data[son] = 1
                return
            dfs(word, i + 1, son + word[i])
            dfs(word, i + 1, son)

        if len(word) == 1:
            return test(word[0])
        dfs(word, 0, "")
        result = 0
        for key in self.data.keys():
            result += test(key)
        return result

print(Solution().countVowels("noosabasboosa"))
