# ****************************************************************分割线****************************************************************
# todo 0641（Design Circular Deque）
# 设计循环双端队列

class MyCircularDeque:
    def __init__(self, k: int):
        self.data = [None] * k
        self.length = k
        self.front = -1
        self.rear = -1

    # 入栈
    def insertFront(self, value: int) -> bool:
        if self.data.count(None) == 0:
            return False
        else:
            if self.front == 0:
                self.front = self.length - 1
            else:
                self.front -= 1
            if self.data.count(None) == self.length:
                self.front = self.rear = 0
            self.data[self.front] = value
            return True

    # 入队
    def insertLast(self, value: int) -> bool:
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

    # 出队
    def deleteFront(self) -> bool:
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

    # 出栈
    def deleteLast(self) -> bool:
        if self.data.count(None) == self.length:
            return False
        else:
            self.data[self.rear] = None
            if self.rear == 0:
                self.rear = self.length - 1
            else:
                self.rear -= 1
            if self.data.count(None) == self.length:
                self.front = self.rear = -1
            return True

    # 队头
    def getFront(self) -> int:
        if self.front == -1:
            return -1
        else:
            return self.data[self.front]

    # 栈顶
    def getRear(self) -> int:
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

obj = MyCircularDeque(3)
print(obj.insertFront(2))
print(obj.insertLast(4))
print(obj.insertFront(6))
print(obj.output())
# print(obj.getRear())
# print(obj.deleteLast())
# print(obj.getRear())
# print(obj.deleteLast())
# print(obj.getRear())
# print(obj.deleteLast())
print(obj.getFront())
print(obj.deleteFront())
print(obj.getFront())
print(obj.deleteFront())
print(obj.getFront())
print(obj.deleteFront())
