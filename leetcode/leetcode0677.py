# ****************************************************************分割线****************************************************************
# todo 0677（Map Sum Pairs）
# 键值映射

class MapSum:
    def __init__(self):
        self.data = {}

    def insert(self, key: str, val: int) -> None:
        self.data[key] = val

    def sum(self, prefix: str) -> int:
        return sum(self.data[i] for i in self.data if i.startswith(prefix))

obj = MapSum()
obj.insert("apple", 3)
obj.insert("app", 2)
print(obj.sum("ap"))
