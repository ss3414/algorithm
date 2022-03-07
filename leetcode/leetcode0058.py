# ****************************************************************分割线****************************************************************
# todo 0058（Length of Last Word）
# 最后一个单词的长度

def test(s: str):
    # 字符串全为空格，返回0
    if s.isspace():
        return 0

    # 从左边找最后一个" _"，从右边找第一个"_ "
    length = len(s)
    begin = 0
    i = 0
    while i < length - 1:
        if s[i] == " " and s[i + 1] != " ":
            begin = i + 1
        i += 1

    end = length
    if length > 0 and s[length - 1] == " ":
        j = length
        while j > begin:
            if s[j - 1] == " " and s[j - 2] != " ":
                end = j - 1
                break
            j -= 1
    # print("begin:{begin} end:{end}".format(begin=begin,end=end))
    # print(s[begin:end])
    return len(s[begin:end])

# 抹去右边的空格，再从右往左数到第一个空格即可
def test2(s: str):
    length = 0
    right = len(s) - 1
    while right >= 0 and s[right] == " ":
        right -= 1
    while right >= 0 and s[right] != " ":
        right -= 1
        length += 1
    return length

# print(test("Hello"))
# print(test("  fly  me  to  the  moon  "))
# print(test(" "))

print(test2("Hello"))
print(test2("  fly  me  to  the  moon  "))
print(test2(" "))
