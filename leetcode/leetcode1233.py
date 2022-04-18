# ****************************************************************分割线****************************************************************
# todo 1233（Remove Sub-Folders from the Filesystem）
# 删除子文件夹

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

    def recursion(self, node, parent):
        if node.children == {}:
            return
        else:
            for child in node.children:
                temp_str = parent + child
                temp_node = node.children[child]
                # 如果碰到单词，结束递归，否则继续
                if temp_node.is_word:
                    self.result.append(temp_str)
                    if "/" in temp_node.children:
                        del temp_node.children["/"]
                self.recursion(temp_node, temp_str)

class Solution:
    def removeSubfolders(self, folder: list) -> list:
        obj = Trie()
        for i in folder:
            obj.insert(i)
        return obj.output()

print(Solution().removeSubfolders(["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]))
# print(Solution().removeSubfolders(["/a/b/c","/a/b/ca","/a/b/c/a","/a/b/d"]))
