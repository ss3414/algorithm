# ****************************************************************分割线****************************************************************
# todo 鸡尾酒排序

def cocktail(inputs):
    i = 0
    # 外层循环一次，内层奇偶循环两次
    while i < (len(tests) // 2):
        # 奇数轮，从左向右
        j = i
        end = len(inputs) - i - 1  # 每次循环后，无序区缩小，左右两端已排序
        is_sorted = True
        while j < end:
            if inputs[j] > inputs[j + 1]:
                temp = inputs[j]
                inputs[j] = inputs[j + 1]
                inputs[j + 1] = temp
                is_sorted = False
            j += 1
        if is_sorted:
            break
        print("奇：{inputs} range:{begin}~{end}".format(inputs=inputs, begin=i, end=end))
        # 偶数轮，从右向左
        j = end
        is_sorted = True
        while j > i:
            if inputs[j] < inputs[j - 1]:
                temp = inputs[j]
                inputs[j] = inputs[j - 1]
                inputs[j - 1] = temp
                is_sorted = False
            j -= 1
        if is_sorted:
            break
        print("偶：{inputs} range:{begin}~{end}".format(inputs=inputs, begin=end, end=i))
        i += 1
    return inputs

tests = [9, 8, 7, 6, 5, 4, 3, 2, 1]
cocktail(tests)
