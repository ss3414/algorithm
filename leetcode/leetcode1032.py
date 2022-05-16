# ****************************************************************分割线****************************************************************
# todo 1032（Stream of Characters）
# 字符流

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

    def search(self, word: str) -> bool:
        cursor = self
        for i in word:
            if cursor.is_word:
                return True
            if i not in cursor.children:
                return False
            cursor = cursor.children[i]
        return cursor.is_word

class StreamChecker:
    def __init__(self, words: list):
        self.root = TrieNode()
        self.string = ""
        for word in words:
            self.root.insert(word[::-1])

    def query(self, letter: str) -> bool:
        # 逆序储存，逆序查询
        self.string = letter + self.string
        return self.root.search(self.string)

obj = StreamChecker(["bc", "cd", "bcde"])
print(obj.query("a"))
print(obj.query("b"))
print(obj.query("c"))
print(obj.query("d"))
print(obj.query("e"))
