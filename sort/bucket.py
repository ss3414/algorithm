# ****************************************************************分割线****************************************************************
# todo 桶排序

# 时间复杂度：最坏O(n+k)，最好O(n+k)
# 最坏：所有元素分配到同一个桶中
# 最好：元素均匀分配到每一个桶中
# 计数排序的改进版

list = [9, 9, 7, 7, 5, 5, 3, 3, 1]

max = list[0]
min = list[0]
for i in list:
    if i >= max:
        max = i
    if i <= min:
        min = i
d = max - min

# 初始化桶，桶的数量等于元素个数
bucket = []
for i in list:
    bucket.append([])  # 最小值1，最大值9，差值为8/9的等差数列（1，1+8/9，2+7/9）

# 将元素放入桶中
for i in list:
    index = (i - min) // (d // (len(bucket) - 1))  # 元素对应第几个桶
    bucket[index].append(i)

# 对每个桶内的元素再排序
for i in bucket:
    i.sort()

output = []
for i in bucket:
    for j in i:
        output.append(j)

print(output)
