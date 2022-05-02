# ****************************************************************分割线****************************************************************
# todo 归并排序

def merge(input):
    length = len(input)
    if length <= 1:
        return input
    middle = length // 2
    # 将输入序列拆分成左右序列
    left, right = input[0:middle], input[middle:]
    # 递归拆分排序，最终汇总
    return sort(merge(left), merge(right))

def sort(left, right):
    output = []
    # 遍历左右序列并排序，最终剩余一个最大元素
    print("l:{l} r:{r}".format(l=left, r=right))
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

test = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(merge(test))
