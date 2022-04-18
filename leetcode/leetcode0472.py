# ****************************************************************分割线****************************************************************
# todo 0472（Concatenated Words）
# 连接词

class TrieNode:
    def __init__(self):
        self.is_word = False
        self.is_prefix = False  # 是否为缀合词
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.data = []

    def insert(self, word: str) -> None:
        node = self.root
        flag = False
        parent = ""
        for i in word:
            parent += i
            if i not in node.children:
                node.children[i] = TrieNode()
            if node.children[i].is_word:
                flag = True
            node = node.children[i]
        node.is_word = True
        node.is_prefix = flag
        if flag:
            self.data.append(parent)

    # 将输入的单词一段一段与字典树比较
    def match(self, word: str) -> bool:
        # print(word)
        node = self.root
        l = len(word)
        i = 0
        while i < l:
            if word[i] not in node.children:
                return False
            temp = node.children[word[i]]
            if temp.is_word:  # fixme 碰到最短前缀就截取了
                if i == (l - 1):
                    return True
                else:
                    return self.match(word[i + 1:])  # 截取后半段
            node = temp
            i += 1

    # 判断缀合词是否符合条件
    def concatenate(self) -> list:
        result = []
        for i in self.data:
            if self.match(i):
                result.append(i)
        return result

class Solution:
    def findAllConcatenatedWordsInADict(self, words: list) -> list:
        obj = Trie()
        for i in words:
            obj.insert(i)
        return obj.concatenate()

print(Solution().findAllConcatenatedWordsInADict(["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]))
# print(Solution().findAllConcatenatedWordsInADict(["cat","cats"]))
