# ****************************************************************分割线****************************************************************
# todo 堆

# 堆
# 一种完全二叉树，任意父节点的值大于或小于子节点的值
# 数组实现，父节点下标parent，左子节点2*parent+1，右子节点2*parent+2

import math

# 上浮（把根节点挤到最前面）
def up(list):
    child = len(list) - 1
    parent = math.floor((child - 1) / 2)  # 左子节点2*parent+1
    temp = list[child]
    while child > 0 and temp < list[parent]:  # 大于（最大堆）/小于（最小堆）
        list[child] = list[parent]
        child = parent
        parent = math.floor((parent - 1) / 2)
    list[child] = temp

# 下沉
def down(list, parent, length):
    temp = list[parent]
    child = 2 * parent + 1
    while child < length:
        if child + 1 < length and list[child + 1] < list[child]:  # 大于（最大堆）/小于（最小堆）
            child += 1
        if temp < list[child]:  # 大于等于（最大堆）/小于（最小堆）
            break
        list[parent] = list[child]
        parent = child
        child = 2 * child + 1
    list[parent] = temp

# 构建堆
def build(list):
    i = math.floor((len(list) - 2) / 2)
    while i >= 0:
        down(list, i, len(list))
        i -= 1

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # 1~10有序排列本身就是一个最小堆
list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# up(list)
build(list)
print(list)
