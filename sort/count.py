# ****************************************************************分割线****************************************************************
# todo 计数排序

def count(input):
    max = input[0]
    min = input[0]
    for i in input:
        if i >= max:
            max = i
        if i <= min:
            min = i
    temp = [0] * (max - min + 1)  # 1~9

    for i in input:
        temp[i - min] += 1  # i - min是元素在temp中的位置

    output = []
    i = 0
    while i < len(temp):
        if temp[i] != 0:
            j = 0
            while j < temp[i]:
                output.append(i + min)
                j += 1
        i += 1
    return output

test = [9, 9, 7, 7, 5, 5, 3, 3, 1]
print(count(test))
