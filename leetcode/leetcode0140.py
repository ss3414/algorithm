# ****************************************************************分割线****************************************************************
# todo 0140（Word Break II）
# 单词拆分II

class Solution:
    def wordBreak(self, s: str, wordDict: list) -> list:
        def backtrack(i, sentense):
            if i == l:
                result.append(" ".join(sentense))
            else:
                for j in range(i + 1, l + 1):
                    if s[i:j] in wordDict:
                        sentense.append(s[i:j])
                        print("{i} {j} {s}".format(i=i, j=j, s=sentense))
                        backtrack(j, sentense)  # 通过递归将s一段一段拆分
                        sentense.pop()

        l = len(s)
        result = []
        backtrack(0, [])
        return result

print(Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
