# ****************************************************************分割线****************************************************************
# todo 堆排序

# 时间复杂度：最坏O(nlogn)，最好O(nlogn)，不稳定
# 利用堆实现的排序

import math

def down(list, parent, length):
    temp = list[parent]
    child = 2 * parent + 1
    while child < length:
        if child + 1 < length and list[child + 1] < list[child]:
            child += 1
        if temp < list[child]:
            break
        list[parent] = list[child]
        parent = child
        child = 2 * child + 1
    list[parent] = temp

def build(list):
    i = math.floor((len(list) - 2) / 2)
    while i >= 0:
        down(list, i, len(list))
        i -= 1

def sort(list):
    i = len(list) - 1
    while i >= 0:
        temp = list[i]
        list[i] = list[0]
        list[0] = temp
        down(list, i, len(list))
        i -= 1

list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
build(list)  # 构建最小堆
sort(list)  # fixme
print(list)
