# ****************************************************************分割线****************************************************************
# todo 0225（Implement Stack using Queues）
# 用队列实现栈

from collections import deque

class MyStack:
    def __init__(self):
        self.data = deque([])

    def push(self, x: int) -> None:
        self.data.append(x)
        # 除新入队元素，将其他元素出队后重新入队
        i = 0
        while i < len(self.data) - 1:
            self.data.append(self.data.popleft())
            i += 1

    def pop(self) -> int:
        return self.data.popleft()

    def top(self):
        if len(self.data) > 0:
            return self.data[0]
        else:
            return None

    def empty(self) -> bool:
        return not len(self.data)

obj = MyStack()
obj.push(1)
print(obj.pop())
print(obj.top())
print(obj.empty())
