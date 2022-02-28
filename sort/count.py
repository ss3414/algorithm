# ****************************************************************分割线****************************************************************
# todo 计数排序

# 时间复杂度：最坏O(n+k)，最好O(n+k)
# 元素必须为整数
# 适合元素多/范围窄的集合

list = [9, 9, 7, 7, 5, 5, 3, 3, 1]

max = list[0]
min = list[0]
for i in list:
    if i >= max:
        max = i
    if i <= min:
        min = i
count = [0] * (max - min + 1)  # 1~9

for i in list:
    count[i - min] += 1  # i - min是元素在count中的位置

output = []
i = 0
while i < len(count):
    if count[i] != 0:
        j = 0
        while j < count[i]:
            output.append(i + min)
            j += 1
    i += 1

print(output)
