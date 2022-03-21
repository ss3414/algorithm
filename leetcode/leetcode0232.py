# ****************************************************************分割线****************************************************************
# todo 0232（Implement Stack using Queues）
# 用栈实现队列

class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        # 除新入栈元素，其他元素出栈后逆序重新入栈
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        return self.s1.pop()

    def peek(self) -> int:
        if len(self.s1) > 0:
            return self.s1[-1]
        else:
            return None

    def empty(self) -> bool:
        return not self.s1

obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
print(obj.pop())
print(obj.peek())
print(obj.empty())
