# ****************************************************************分割线****************************************************************
# todo 0155（Min Stack）
# 最小栈
# 设计一个栈能实现push/pop/top，并能在常数时间内返回最小值

class MinStack:
    def __init__(self):
        self.data = []
        self.min = []

    def push(self, val: int) -> None:
        self.data.append(val)
        if len(self.min) == 0 or self.getMin() >= val:
            self.min.append(val)  # self.min在这里是最小堆

    def pop(self) -> None:
        # 如果data出栈，则min中相同元素也出栈
        if len(self.min) > 0 and self.top() == self.getMin():
            self.min.pop()
        self.data.pop()

    def top(self) -> int:
        if len(self.data) > 0:
            temp = self.data.pop()  # 可以用data[-1]代替栈的top()方法
            self.data.append(temp)
            return temp
        else:
            return None

    # 相当于min的top()方法
    def getMin(self) -> int:
        if len(self.min) > 0:
            temp = self.min.pop()
            self.min.append(temp)
            return temp
        else:
            return None

obj = MinStack()
print(obj.top())
print(obj.getMin())
obj.push(1)
obj.push(2)
obj.push(0)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())
