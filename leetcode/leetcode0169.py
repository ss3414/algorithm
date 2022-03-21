# ****************************************************************分割线****************************************************************
# todo 0169（Majority Element）
# 求众数

# 哈希表
def test(nums: list):
    data = {}
    i = 0
    while i < len(nums):
        count = data.get(nums[i])
        if count is None:
            data.update({nums[i]: 1})
        else:
            count += 1
            data.update({nums[i]: count})
        i += 1
    for key, value in data.items():
        if value == max(data.values()):
            return key

# 数学极值思想，众数元素占一半以上，最差情况n+1个众数，n个其他数，两两相抵至少有一个众数
def test2(nums: list):
    count = 1
    max_val = nums[0]
    i = 1
    while i < len(nums):
        if max_val == nums[i]:
            count += 1
        else:
            count -= 1
            if count == 0:
                max_val = nums[i + 1]
        i += 1
    return max_val

# print(test([2,3,3]))
print(test2([3, 1, 3, 2, 3]))
