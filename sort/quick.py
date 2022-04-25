# ****************************************************************分割线****************************************************************
# todo 快排序

# 递归分区排序
def quick(input, left, right):
    if left < right:
        mark = partition(input, left, right)
        quick(input, left, mark - 1)
        quick(input, mark + 1, right)
    return input

# 分区排序（单边循环）
def partition(input, left, right):
    pivot = left  # 取第一个元素为基准元素
    mark = pivot + 1  # mark指针，小于基准元素的边界
    i = mark
    while i <= right:  # 遍历基准元素右边的序列
        if input[i] < input[pivot]:  # 如果比基准元素小，交换，mark指针前进
            input[i], input[mark] = input[mark], input[i]
            mark += 1
        i += 1
    print("{p} {i}".format(p=input[pivot],i=input))
    input[pivot], input[mark - 1] = input[mark - 1], input[pivot]  # 交换基准元素与mark指针
    return mark - 1

test = [1, 2, 3, 4, 5, 9, 8, 7, 6]
print(quick(test, 0, len(test) - 1))

# 第一次分区排序后
# print(partition(test, 0, len(test) - 1))
