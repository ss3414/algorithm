# ****************************************************************分割线****************************************************************
# todo 0622（Design Circular Queue）
# 设计循环队列

class MyCircularQueue:
    def __init__(self, k: int):
        self.data = [None] * k
        self.length = k
        self.front = -1
        self.rear = -1

    def enQueue(self, value: int) -> bool:
        if self.data.count(None) == 0:
            return False
        else:
            if self.data.count(None) == self.length:
                self.front = 0
            if self.rear < self.length - 1:
                self.rear += 1
            else:
                self.rear = 0
            self.data[self.rear] = value
            return True

    def deQueue(self) -> bool:
        if self.data.count(None) == self.length:
            return False
        else:
            self.data[self.front] = None
            if self.front < self.length - 1:
                self.front += 1
            else:
                self.front = 0
            if self.data.count(None) == self.length:
                self.front = self.rear = -1
            return True

    def Front(self) -> int:
        if self.front == -1:
            return -1
        else:
            return self.data[self.front]

    def Rear(self) -> int:
        if self.rear == -1:
            return -1
        else:
            return self.data[self.rear]

    def isEmpty(self) -> bool:
        return self.data.count(None) == self.length

    def isFull(self) -> bool:
        return self.data.count(None) == 0

    def output(self):
        print("{f} {r} {d}".format(f=self.front, r=self.rear, d=self.data))

obj = MyCircularQueue(6)
print(obj.enQueue(6))
print(obj.Rear())
print(obj.Rear())
print(obj.deQueue())
print(obj.enQueue(5))
print(obj.Rear())
print(obj.deQueue())
print(obj.output())
print(obj.Front())
print(obj.deQueue())
