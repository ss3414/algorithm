# ****************************************************************分割线****************************************************************
# todo 快排序

# 时间复杂度：最坏O(n^2)，最好O(nlogn)，不稳定
# 冒泡排序的分治递归版

# 递归分区排序
def quick(list, left, right):
    if left < right:
        mark = partition(list, left, right)
        quick(list, left, mark - 1)
        quick(list, mark + 1, right)
    return list

# 分区排序（单边循环）
def partition(list, left, right):
    pivot = left  # 取第一个元素为基准元素
    mark = pivot + 1  # mark指针，小于基准元素的边界
    i = mark
    while i <= right:  # 遍历基准元素右边的序列
        if list[i] < list[pivot]:  # 如果比基准元素小，交换，mark指针前进
            list[i], list[mark] = list[mark], list[i]
            mark += 1
        i += 1
    list[pivot], list[mark - 1] = list[mark - 1], list[pivot]  # 交换基准元素与mark指针
    return mark - 1

list = [5, 4, 3, 2, 1, 9, 8, 7, 6]
# print(quick(list, 0, len(list) - 1))

# 第一次分区排序后
print(partition(list, 0, len(list) - 1))
print(list)
