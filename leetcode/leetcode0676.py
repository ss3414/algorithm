# ****************************************************************分割线****************************************************************
# todo 0676（Implement Magic Dictionary）
# 魔法字典

class MagicDictionary:
    def __init__(self):
        self.data = {}

    def buildDict(self, dictionary: list) -> None:
        for i in dictionary:
            self.data[len(i)] = self.data.get(len(i), []) + [i]
        print(self.data)

    def search(self, searchWord: str) -> bool:
        for i in self.data.get(len(searchWord), []):
            count = 0
            for j in range(len(searchWord)):
                if i[j] != searchWord[j]:
                    count += 1
            if count == 1:
                return True
        return False

obj = MagicDictionary()
obj.buildDict(["hello", "hallo", "leetcode"])
print(obj.search("hello"))
print(obj.search("hhllo"))
print(obj.search("hell"))
print(obj.search("leetcoded"))
