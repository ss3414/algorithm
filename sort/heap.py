# ****************************************************************分割线****************************************************************
# todo 堆排序

# 利用堆实现的排序

def down(input, parent, length):
    temp = input[parent]
    child = 2 * parent + 1
    while child < length:
        if child + 1 < length and input[child + 1] < input[child]:
            child += 1
        if temp < input[child]:
            break
        input[parent] = input[child]
        parent = child
        child = 2 * child + 1
    input[parent] = temp

def build(input):
    i = (len(input) - 2) // 2
    while i >= 0:
        down(input, i, len(input))
        i -= 1

# 将堆顶取出放到数组末尾，对截取后的数组重新构建最小堆，再重复此步骤
def sort(input):
    i = len(input) - 1
    while i >= 0:
        temp = input[i]
        input[i] = input[0]
        input[0] = temp
        print("{i}:{h}".format(i=i, h=input))
        down(input, 0, i)
        print("{i}:{h}".format(i=i, h=input))
        i -= 1

test = [5, 4, 3, 2, 1]
build(test)  # 构建最小堆
print(test)
sort(test)
print(test)
