# ****************************************************************分割线****************************************************************
# todo 0026（Remove Duplicates from Sorted Array）
# 删除有序数组中的重复数，返回有多少个不相同的数

# 哈希表
def test(nums: list):
    data = {}
    i = 0
    while i < len(nums):
        data.update({nums[i]: i})
        i += 1
    j = 0
    for k in data:
        nums[j] = k
        j += 1
    while j < len(nums):
        nums[j] = None
        j += 1
    # del nums[len(data):len(nums)]
    # print(nums)
    return len(data)

# 数组元素两两比较，不相同则result加一
def test2(nums: list):
    result = 1  # 至少有1个不相同的数
    i = 0
    while i < len(nums) - 1:
        if nums[i] != nums[i + 1]:
            nums[result] = nums[i + 1]
            result += 1
        i += 1
    j = result
    while j < len(nums):
        nums[j] = None
        j += 1
    print(nums)
    return result

test = [1, 1, 2, 2, 3, 3]  # 输入数组是有序的
# print(test(test))

print(test2(test))
