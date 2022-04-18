# ****************************************************************分割线****************************************************************
# todo 0648（Replace Words）
# 替换单词

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

    # 判断字典树中字符串是否为word的前缀
    def prefix(self, word: str) -> str:
        node = self.root
        replace = ""
        for i in word:
            if i not in node.children:
                return word
            replace += i
            if node.children[i].is_word:
                return replace
            node = node.children[i]
        return word

class Solution:
    def replaceWords(self, dictionary: list, sentence: str) -> str:
        obj = Trie()
        for i in dictionary:
            obj.insert(i)
        words = sentence.split(" ")
        result = ""
        for word in words:
            result += (" " + obj.prefix(word))
        return result[1::]

print(Solution().replaceWords(["cat", "bat", "rat"], "the cattle was rattled by the battery"))
