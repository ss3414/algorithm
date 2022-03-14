# ****************************************************************分割线****************************************************************
# todo 队列

# 循环队列
class CircularQueue:
    elements = []  # 数组存储队列
    front = 0  # 队头
    rear = 0  # 队尾

    def __init__(self, length):
        self.elements = [None] * length

    # 入队（队尾入队）
    def en_queue(self, element):
        if (self.rear + 1) % len(self.elements) == self.front:
            print("队列已满")
            return
        self.elements[self.rear] = element
        self.rear = (self.rear + 1) % len(self.elements)

    # 出队（队头出队）
    def de_queue(self):
        if self.rear == self.front:
            print("队列已空")
            return
        self.elements[self.front] = None
        self.front = (self.front + 1) % len(self.elements)

    def output(self):
        i = self.front
        str = ""
        while i != self.rear:
            str += "{data}->".format(data=self.elements[i])
            i = (i + 1) % len(self.elements)
        print(str)

test_queue = CircularQueue(10)
test_queue.en_queue(1)
test_queue.en_queue(2)
test_queue.en_queue(3)
test_queue.de_queue()
test_queue.en_queue(4)
test_queue.output()
print(test_queue.elements)
