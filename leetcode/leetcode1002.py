# ****************************************************************分割线****************************************************************
# todo 1002（Find Common Characters）
# 寻找共同字符

class Solution:
    def commonChars(self, words: list) -> list:
        result = []
        for i in words[0]:
            if all([i in word for word in words]):
                for j in range(len(words)):
                    words[j] = words[j].replace(i, "", 1)
                result.append(i)
        return result

print(Solution().commonChars(["bella", "label", "roller"]))
