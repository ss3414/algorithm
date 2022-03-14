# ****************************************************************分割线****************************************************************
# todo Python中的数据结构

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

# ****************************************************************分割线****************************************************************
# todo 工具方法

# 从大到小输出位数
def digit(sum=234):
    div = 1
    while sum / div >= 10:  # sum的位数
        div *= 10
    while sum > 0:
        temp = int(sum // div)
        print("sum:{sum} temp:{temp}".format(sum=sum, temp=temp))
        sum -= temp * div
        div /= 10

# digit()
