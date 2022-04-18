# ****************************************************************分割线****************************************************************
# todo 选择排序

# 外层需要循环n-1次，每次至多需要比较n-1次，至多需要移动1个元素

def select(input):
    for i in range(len(input) - 1):  # 外层循环位置
        for j in range(i + 1, len(input)):  # 内层循环要比较的次数
            if input[j] < input[i]:
                temp = input[i]
                input[i] = input[j]
                input[j] = temp
                # print(input)
    return input

test = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(select(test))
