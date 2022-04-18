# ****************************************************************分割线****************************************************************
# todo 桶排序

def bucket(input):
    max = input[0]
    min = input[0]
    for i in input:
        if i >= max:
            max = i
        if i <= min:
            min = i
    d = (max - min) / (len(input) - 1)  # 桶之间的差

    # 初始化桶，桶的数量等于元素个数，桶相当于等差数列
    bucket = [[] for i in input]

    # 将元素放入桶中
    for i in input:
        index = int((i - min) / d)  # 元素对应第几个桶（减去最小值再除以差）
        bucket[index].append(i)
    print(bucket)

    # 对每个桶内的元素再排序
    for i in bucket:
        i.sort()

    output = []
    for i in bucket:
        for j in i:
            output.append(j)
    return output

test = [100, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(bucket(test))
