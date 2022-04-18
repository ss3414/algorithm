# ****************************************************************分割线****************************************************************
# todo 0386（Lexicographical Numbers）
# 字典序排数

class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.result = []

    def insert(self, word: str) -> None:
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.is_word = True

    def output(self) -> list:
        self.recursion(self.root, "")
        return self.result

    # 递归输出字典树
    def recursion(self, node, parent):
        if node.children == {}:
            return
        else:
            for child in node.children:
                temp = parent + child
                self.result.append(temp)
                self.recursion(node.children[child], temp)

class Solution:
    def lexicalOrder(self, n: int) -> list:
        obj = Trie()
        for i in range(1, n + 1):
            obj.insert(str(i))
        return obj.output()

print(Solution().lexicalOrder(13))
