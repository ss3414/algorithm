# ****************************************************************分割线****************************************************************
# todo 1268（Search Suggestions System）
# 搜索推荐系统

import copy

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

    def recursion(self, node, parent):
        if node.children == {}:
            return
        else:
            temp_children = [i for i in node.children]
            temp_children.sort()
            for child in temp_children:
                temp_str = parent + child
                temp_node = node.children[child]
                if len(self.result) >= 3:
                    return
                if temp_node.is_word:
                    self.result.append(temp_str)
                self.recursion(temp_node, temp_str)

    # 推荐
    def suggest(self, prefix: str) -> list:
        node = self.root
        parent = ""
        for i in prefix:
            parent += i
            if i not in node.children:
                return []
            node = node.children[i]
        self.result.clear()
        if node.is_word:
            self.result.append(parent)
        self.recursion(node, parent)
        return self.result

class Solution:
    def suggestedProducts(self, products: list, searchWord: str) -> list:
        obj = Trie()
        for i in products:
            obj.insert(i)
        result = []
        j = 1
        while j <= len(searchWord):
            # print(obj.suggest(searchWord[0:j]))
            result.append(copy.deepcopy(obj.suggest(searchWord[0:j])))
            j += 1
        return result

print(Solution().suggestedProducts(["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse"))
