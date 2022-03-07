# ****************************************************************分割线****************************************************************
# todo 希尔排序

# 时间复杂度：最坏O(n(logn)^2)，最好O(n(logn)^2)，不稳定
# 插入排序的改进版

list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
gap = 1
while gap < len(list) / 3:
    gap = gap * 3 + 1
print(gap)  # fixme