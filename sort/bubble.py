# ****************************************************************分割线****************************************************************
# todo 冒泡排序

# 时间复杂度：最坏O(n^2)，最好O(n)
# 外层需要循环n-1次
# 内层至多需要比较n-1次，至多需要交换n-1对元素（比较/交换都占用时间）
# 时间复杂度T(n)=O((n-1)*2(n-1))=O(2n^2-4n+2)=O(2n^2)=O(n^2)

# 初始版
def bubble(inputs):
    i = 0
    while i < len(inputs) - 1:  # 外层循环要比较的次数
        j = 0
        while j < len(inputs) - 1:  # 内层循环要比较的次数
            if inputs[j] > inputs[j + 1]:
                temp = inputs[j]
                inputs[j] = inputs[j + 1]
                inputs[j + 1] = temp
            j += 1
        i += 1
        print(inputs)
    return inputs

# 优化版
# ①is_sorted跳出优化已排序完成继续排序
# ②sort_border边界优化后半段已排序完成继续排序
def bubble2(inputs):
    i = 0
    last_exchange = 0  # 最后一次交换的位置
    sort_border = len(inputs) - 1  # 无序区的边界，每次只需要比较到这
    print("{inputs} index:{index}".format(inputs=inputs, index=sort_border))
    while i < len(inputs) - 1:
        j = 0
        is_sorted = True
        while j < sort_border:
            if inputs[j] > inputs[j + 1]:
                temp = inputs[j]
                inputs[j] = inputs[j + 1]
                inputs[j + 1] = temp
                is_sorted = False
                last_exchange = j
            j += 1
        # 如果没有交换元素，则排序已完成，跳出外层循环
        if is_sorted:
            print("break")
            break
        sort_border = last_exchange
        print("{inputs} index:{index}".format(inputs=inputs, index=sort_border))
        i += 1
    return inputs

# tests = [9, 8, 7, 6, 5, 4, 3, 2, 1]
# bubble(tests)

tests = [6, 5, 4, 3, 1, 2, 7, 8, 9]
bubble2(tests)
