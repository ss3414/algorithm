# ****************************************************************分割线****************************************************************
# todo 0219（Contains Duplicate II）
# 存在重复元素II
# 找重复元素，且重复元素坐标差的绝对值<=k

# 哈希表
def test(nums: list, k: int):
    data = {}
    i = 0
    while i < len(nums):
        index = data.get(nums[i])
        if index is not None and abs(index - i) <= k:
            return True
        data.update({nums[i]: i})
        i += 1
    return False

# print(test([1,2,3,1],3))
print(test([1, 2, 3, 1], 1))
