# ****************************************************************分割线****************************************************************
# todo 0211（Design Add and Search Words Data Structure）
# 添加与搜索单词

class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.is_word = True

    def search(self, word: str) -> bool:
        return self.search2(self.root, word)

    # 模糊搜索
    def search2(self, node, word):
        i = 0
        while i < len(word):
            if word[i] == ".":
                for child in node.children:
                    if self.search2(node.children[child], word[i + 1:len(word)]):
                        return True
                return False
            if word[i] not in node.children:
                return False
            node = node.children[word[i]]
            i += 1
        return node.is_word

obj = WordDictionary()
obj.addWord("bad")
print(obj.search("bad"))
print(obj.search(".ad"))
print(obj.search("b.."))
