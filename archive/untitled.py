# ****************************************************************分割线****************************************************************
# todo Python中的运算/数据结构

# 位运算
# i=2<<1  # 2的二进制10左移一位变成100
# print(i)
# print(bin(i))

# j=2>>1  # 2的二进制10右移一位变成01
# print(j)
# print(bin(j))

# k=-2>>1  # 正数/负数，原码/补码/反码
# print(k)
# print(bin(k))

# ************************************************************半分割线******************************

# 二维数组
# data=[[0]*3]*3
# data[1][1]=1
# print(data)  # 浅拷贝导致出错

# data=[[]]*3
# data[1]=[0]*3
# data[1][1]=1
# print(data)

# data=[[0 for i in range(3)] for j in range(3)]
# data[1][1]=1
# print(data)  # 一次性创建Python二维数组

# ************************************************************半分割线******************************

# 列表充当栈
# stack=[1,2,3]
# stack.append(4)
# print(stack)
# print(stack.pop())

# 列表充当队列
# from collections import deque
# queue=deque([1,2,3])
# queue.append(4)
# print(queue)
# print(queue.popleft())

# 优先队列（堆实现）
# from queue import PriorityQueue
# tests=PriorityQueue()
# tests.put(2)
# tests.put(1)
# tests.put(3)
# while not tests.empty():
#     print(tests.get())

# 堆
# import heapq
# tests=[2,1,3]
# heapq.heapify(tests)
# heapq.heappush(tests,0)
# while tests:
#     print(heapq.heappop(tests))

# ****************************************************************分割线****************************************************************
# todo 工具方法

# 从大到小输出位数
def digit(n):
    div = 1
    while n / div >= 10:  # n的位数
        div *= 10
    digits = []
    while n > 0:
        temp = int(n // div)
        digits.append(temp)
        print("n:{n} temp:{temp}".format(n=n, temp=temp))
        n -= temp * div
        div /= 10
    return digits

# print(digit(234))
