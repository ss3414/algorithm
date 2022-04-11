# ****************************************************************分割线****************************************************************
# todo 未分类

# 位运算

# 与
# print(1<<2)
# print(12&(1<<2))  # 1<<2二进制0b100，12二进制0b1100，0b100&0b1100=0b100=4

# 异或
# print(1^2)  # 转换为二进制01^10=11，相同为0不同为1，
# print(1^2^1)  # 传递性/对称性，异或两个相同数字还等于原数字
# print(0^1)  # 0异或任何数字还等于原数字

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

# ASCII
# print(ord("a"))
# print(chr(ord("a")+25))

# 列表/字符串索引
# s="abcd"
# print(s[-2:])  # 倒数两位
# print(s[0:4:2])  # [start:end:step]
# print(s[2::])  # 第二到末尾
# print(s[::2])  # 奇数位
# print(s[::-1])  # 逆序

# ************************************************************半分割线******************************

# 二维数组
# grid=[[0]*3]*3
# grid[1][1]=1
# print(grid)  # 浅拷贝导致出错

# grid=[[]]*3
# grid[1]=[0]*3
# grid[1][1]=1
# print(grid)

# grid=[[0 for i in range(2)] for j in range(4)]
# grid[1][1]=1
# print(grid)  # 一次性创建Python二维数组

# ************************************************************半分割线******************************

# 集合
# set1={1,2,3}
# set2={1,2,3,4,5,6}
# print(set1<set2)  # set1是set2子集

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
# test=PriorityQueue()
# test.put(2)
# test.put(1)
# test.put(3)
# while not test.empty():
#     print(test.get())

# 堆
# import heapq
# test=[2,1,3]
# heapq.heapify(test)
# heapq.heappush(test,0)
# while test:
#     print(heapq.heappop(test))
