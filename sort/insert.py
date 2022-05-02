# ****************************************************************分割线****************************************************************
# todo 插入排序

def insert(input):
    i = 1
    while i < len(input):
        temp = input[i]  # 要插入的元素
        j = i
        while j > 0 and input[j - 1] > temp:  # 循环有序，把比插入元素大的元素挤到后面
            input[j] = input[j - 1]
            j -= 1
            print("{i} {input}".format(i=i, input=input))
        input[j] = temp  # 插入
        print("{i} {input}".format(i=i, input=input))
        i += 1
    return input

test = [8, 9, 7, 6]
print(insert(test))
