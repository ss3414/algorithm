# ****************************************************************分割线****************************************************************
# todo 0804（Unique Morse Code Words）
# 唯一摩斯码

class Solution:
    def uniqueMorseRepresentations(self, words: list) -> int:
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        data = set()
        for word in words:
            temp = ""
            for j in word:
                temp += morse[ord(j) - 97]
            data.add(temp)
        return len(data)

print(Solution().uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
