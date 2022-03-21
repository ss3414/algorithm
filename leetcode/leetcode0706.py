# ****************************************************************分割线****************************************************************
# todo 0706（Design HashMap）
# 设计HashMap

class MyHashMap:
    data = None

    def __init__(self):
        # 使用二维数组减少空间复杂度
        # 二维数组横坐标0~1000，纵坐标0~999，(1000,0)存储极值1000*1000
        self.data = [[]] * 1001

    def put(self, key: int, value: int) -> None:
        hashkey = key // 1000  # 千位数为hashkey
        self.resize(hashkey)
        self.data[hashkey][key % 1000] = value

    def get(self, key: int) -> int:
        hashkey = key // 1000
        self.resize(hashkey)
        return self.data[hashkey][key % 1000]

    def remove(self, key: int) -> None:
        hashkey = key // 1000
        self.resize(hashkey)
        self.data[hashkey][key % 1000] = -1

    # 扩容
    def resize(self, hashkey: int) -> None:
        if len(self.data[hashkey]) == 0:
            self.data[hashkey] = [-1] * 1000

obj = MyHashMap()
obj.remove(14)
obj.get(4)
obj.put(7, 3)
obj.put(11, 1)
obj.put(12, 1)
obj.get(7)
obj.put(1, 19)
obj.put(0, 3)
obj.put(1, 8)
obj.put(2, 6)
