# ****************************************************************分割线****************************************************************
# todo 堆

# 一种完全二叉树，任意父节点的值大于或小于子节点的值
# 数组实现，父节点下标parent，左子节点2*parent+1，右子节点2*parent+2

import math

# 下沉
def down(input_list, parent, length):
    temp = input_list[parent]
    child = 2 * parent + 1
    # 整个比较过程是子节点二叉树的比较，而非单纯三个节点比较
    while child < length:
        # 如果有右节点且右节点小于左节点，定位到左节点
        if child + 1 < length and input_list[child + 1] < input_list[child]:
            child += 1
        # 如果父节点小于等于子节点，不用比较直接跳出
        if temp <= input_list[child]:
            break
        # 如果没有跳出，则父节点大于子节点，子节点的值覆盖父节点
        input_list[parent] = input_list[child]
        # 子节点成为新的父节点，生成新的子节点
        parent = child
        child = 2 * child + 1
    # 父节点的值覆盖最终的子节点
    input_list[parent] = temp

# 构建堆
def build(input_list):
    # 传入堆所有节点的坐标（数组实现的二叉树/堆的节点集中在数组前半段）
    i = math.floor((len(input_list) - 2) / 2)
    while i >= 0:
        down(input_list, i, len(input_list))
        i -= 1

# 上浮（按照堆的定义，上浮新插入元素/挪到数组前面）
def up(input_list):
    child = len(input_list) - 1  # 最后一个子节点
    parent = math.floor((child - 1) / 2)  # 最后一个子节点的根节点
    temp = input_list[child]
    # 如果父节点大于子节点，父节点的值覆盖子节点
    while child > 0 and temp < input_list[parent]:
        input_list[child] = input_list[parent]
        # 父节点成为新的子节点，生成新的父节点
        child = parent
        parent = math.floor((parent - 1) / 2)
    input_list[child] = temp

# 构建最小堆
# test_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]  # 数组不能存在空元素
# build(test_list)
# print(test_list)

# 上浮
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]
up(test_list)
print(test_list)
