# ****************************************************************分割线****************************************************************
# todo 堆

# 一种完全二叉树，任意父节点的值大于或小于子节点的值
# 数组实现，父节点下标parent，左子节点2*parent+1，右子节点2*parent+2

# 下沉
def down(input, parent, length):
    temp = input[parent]
    child = 2 * parent + 1
    # 整个比较过程是子节点二叉树的比较，而非单纯三个节点比较
    while child < length:
        # 如果有右节点且右节点小于左节点，定位到左节点
        if child + 1 < length and input[child + 1] < input[child]:
            child += 1
        # 如果父节点小于等于子节点，不用比较直接跳出
        if temp <= input[child]:
            break
        # 如果没有跳出，则父节点大于子节点，子节点的值覆盖父节点
        input[parent] = input[child]
        # 子节点成为新的父节点，生成新的子节点
        parent = child
        child = 2 * child + 1
    # 父节点的值覆盖最终的子节点
    input[parent] = temp

# 构建堆
def build(input):
    # 传入堆所有节点的坐标（数组实现的二叉树/堆的节点集中在数组前半段）
    i = (len(input) - 2) // 2
    while i >= 0:
        down(input, i, len(input))
        i -= 1

# 上浮（按照堆的定义，上浮新插入元素/挪到数组前面）
def up(input):
    child = len(input) - 1  # 最后一个子节点
    parent = (child - 1) // 2  # 最后一个子节点的根节点
    temp = input[child]
    # 如果父节点大于子节点，父节点的值覆盖子节点
    while child > 0 and temp < input[parent]:
        input[child] = input[parent]
        # 父节点成为新的子节点，生成新的父节点
        child = parent
        parent = (parent - 1) // 2
    input[child] = temp

# 构建最小堆
test = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]  # 数组不能存在空元素
build(test)
print(test)

# 上浮
# test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]
# up(test)
# print(test)
