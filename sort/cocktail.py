# ****************************************************************分割线****************************************************************
# todo 鸡尾酒排序

import math

def cocktail(input_list):
    i = 0
    # 外层循环一次，内层奇偶循环两次
    while i < math.floor(len(test_list) / 2):
        # 奇数轮，从左向右
        j = i
        end = len(input_list) - i - 1  # 每次循环后，无序区缩小，左右两端已排序
        is_sorted = True
        while j < end:
            if input_list[j] > input_list[j + 1]:
                temp = input_list[j]
                input_list[j] = input_list[j + 1]
                input_list[j + 1] = temp
                is_sorted = False
            j += 1
        if is_sorted:
            break
        print("奇：{input_list} range:{begin}~{end}".format(input_list=input_list, begin=i, end=end))
        # 偶数轮，从右向左
        j = end
        is_sorted = True
        while j > i:
            if input_list[j] < input_list[j - 1]:
                temp = input_list[j]
                input_list[j] = input_list[j - 1]
                input_list[j - 1] = temp
                is_sorted = False
            j -= 1
        if is_sorted:
            break
        print("偶：{input_list} range:{begin}~{end}".format(input_list=input_list, begin=end, end=i))
        i += 1
    return input_list

test_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
cocktail(test_list)
