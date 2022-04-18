# ****************************************************************分割线****************************************************************
# todo 0208（Implement Trie (Prefix Tree)）
# 实现字典树/前缀树

# 字典树节点
class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

# 字典树
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for i in word:
            if i not in node.children:
                return False
            node = node.children[i]
        return node.is_word

    # prefix是否为字典树中字符串的前缀
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in prefix:
            if i not in node.children:
                return False
            node = node.children[i]
        return True

obj = Trie()
obj.insert("apple")
print(obj.search("apple"))
print(obj.startsWith("app"))
