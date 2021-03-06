# ****************************************************************分割线****************************************************************
# todo 0819（Most Common Word）
# 最常见单词

import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list) -> str:
        paragraph = re.sub("[!?',;.]", " ", paragraph.lower())
        data = {}
        for i in paragraph.split(" "):
            if i in data:
                data[i] = data[i] + 1
            else:
                data[i] = 1
        # print(data)
        banned.append("")
        for ban in banned:
            if ban in data:
                del data[ban]
        return max(data, key=data.get)

print(Solution().mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
# print(Solution().mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"]))
