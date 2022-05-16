# ****************************************************************分割线****************************************************************
# todo 0820（Short Encoding of Words）
# 单词最短编码

class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

    def insert(self, word: str) -> None:
        cursor = self
        for i in word:
            if i not in cursor.children:
                cursor.children[i] = TrieNode()
            cursor = cursor.children[i]
        cursor.is_word = True

class Solution:
    def minimumLengthEncoding(self, words: list) -> int:
        def dfs(root, depth):
            if not root:
                return depth
            if not root.children and root.is_word:
                return depth + 1
            sum = 0
            for i in root.children:
                sum += dfs(root.children[i], depth + 1)
            return sum

        root = TrieNode()
        words = [word[::-1] for word in words]  # 单词逆序存入字典树
        for word in words:
            root.insert(word)

        return dfs(root, 0)

print(Solution().minimumLengthEncoding(["time", "me", "bell"]))
# print(Solution().minimumLengthEncoding(["t"]))
