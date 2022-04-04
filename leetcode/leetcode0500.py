# ****************************************************************分割线****************************************************************
# todo 0500（Keyboard Row）
# 键盘行

class Solution:
    def findWords(self, words: list) -> list:
        result = []
        data = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        for word in words:
            one = two = three = 0
            for i in word.lower():
                if data[0].count(i):
                    one = 1
                if data[1].count(i):
                    two = 1
                if data[2].count(i):
                    three = 1
                if one + two + three > 1:
                    break
            if one + two + three == 1:
                result.append(word)
        return result

print(Solution().findWords(["Hello", "Alaska", "Dad", "Peace"]))
