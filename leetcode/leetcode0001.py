# ****************************************************************分割线****************************************************************
# todo 0001（Two Sum）
# 给定一个数组一个target，求数组中和等于target的两数坐标

# 暴力（超时）
def test(nums: list, target: int) -> list:
    i = 0
    while i < len(nums):
        j = 0
        while j < len(nums):
            if i == j:
                j += 1
                continue
            if nums[i] + nums[j] == target:
                return [i, j]
            j += 1
        i += 1
    return []

# 把数组值/下标存到哈希表中，时间复杂度2*(n-1)=O(n)
def test2(nums: list, target: int) -> list:
    i = 0
    data = {}
    while i < len(nums):
        data.update({nums[i]: i})  # 值/下标，数组中可以有重复的值
        i += 1
    j = 0
    while j < len(nums):
        k = target - nums[j]
        if k in data and data.get(k) != j:
            return [data.get(k), j]
        j += 1
    return []

tests = [2, 7, 11, 15]
target = 9
# print(test(tests, target))

print(test2(tests, target))
