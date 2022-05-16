# ****************************************************************分割线****************************************************************
# todo 0900（RLE Iterator）
# 游程编码
# 根据出现频率编码

class RLEIterator:
    def __init__(self, encoding: list):
        self.encoding = encoding
        self.keys = encoding[::2]
        self.length = sum(self.keys)
        self.index = 0  # 指向self.keys的指针
        self.key = 0

    def next(self, n: int) -> int:
        self.key += n
        if self.key > self.length:
            return -1
        while self.key > sum(self.keys[:self.index + 1]):  # 前缀和
            self.index += 1
        return self.encoding[self.index * 2 + 1]

obj = RLEIterator([3, 8, 0, 9, 2, 5])
print(obj.next(2))
print(obj.next(1))
print(obj.next(1))
print(obj.next(2))
