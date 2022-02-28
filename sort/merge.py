# ****************************************************************分割线****************************************************************
# todo 归并排序

# 时间复杂度：最坏O(nlogn)，最好O(nlogn)
# 集合容量为n，拆分成logn层（只有logn-1层参与比较），每层比较n次（每层都是完整的集合）
# 分治算法的典型应用，可分为自上而下的递归和自下而上的迭代（所有递归的方法都可以用迭代重写）
# 分治算法：将复杂的问题拆分求解，再将结果汇总

import math

# 递归拆分排序+汇总
def merge(list):
    length = len(list)
    if length <= 1:
        return list
    middle = math.floor(length / 2)
    # 将输入序列拆分成左右序列
    left, right = list[0:middle], list[middle:]
    # 递归拆分排序，最终汇总
    return sort(merge(left), merge(right))

# 排序
def sort(left, right):
    output = []
    # 遍历左右序列并排序，最终剩余一个最大元素
    while left and right:
        if left[0] <= right[0]:
            output.append(left.pop(0))
        else:
            output.append(right.pop(0))
    # 处理剩余的最大元素
    while left:
        output.append(left.pop(0))
    while right:
        output.append(right.pop(0))
    return output

list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(merge(list))
