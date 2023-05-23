# ****************************************************************分割线****************************************************************
# todo 鸡尾酒排序

def cocktail(input):
    i = 0
    # 外层循环一次，内层奇偶循环两次
    while i < (len(input) // 2):
        # 奇数轮，从左向右
        j = i
        end = len(input) - i - 1  # 每次循环后，无序区缩小，左右两端已排序
        is_sorted = True
        while j < end:
            if input[j] > input[j + 1]:
                temp = input[j]
                input[j] = input[j + 1]
                input[j + 1] = temp
                is_sorted = False
            j += 1
        if is_sorted:
            break
        print("奇：{input} range:{start}~{end}".format(input=input, start=i, end=end))
        # 偶数轮，从右向左
        j = end
        is_sorted = True
        while j > i:
            if input[j] < input[j - 1]:
                temp = input[j]
                input[j] = input[j - 1]
                input[j - 1] = temp
                is_sorted = False
            j -= 1
        if is_sorted:
            break
        print("偶：{input} range:{start}~{end}".format(input=input, start=end, end=i))
        i += 1
    return input

test = [9, 8, 7, 6, 5, 4, 3, 2, 1]
cocktail(test)
