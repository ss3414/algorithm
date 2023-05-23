# ****************************************************************分割线****************************************************************
# todo 1078（Occurrences After Bigram）
# Bigram分词

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> list:
        result = []
        words = text.split(" ")
        i = 0
        while i < len(words) - 2:
            if words[i] == first and words[i + 1] == second:
                result.append(words[i + 2])
            i += 1
        return result

print(Solution().findOcurrences("a good a good", "a", "good"))
print(Solution().findOcurrences("alice is a good girl she is a good student", "a", "good"))
