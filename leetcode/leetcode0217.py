# ****************************************************************分割线****************************************************************
# todo 0217（Contains Duplicate）
# 存在重复元素

# 哈希表
def test(nums: list):
    data = {}
    i = 0
    while i < len(nums):
        val = data.get(nums[i])
        if val is None:
            data.update({nums[i]: 1})
        elif val == 1:
            return True
        i += 1
    return False

print(test([2, 3, 3]))
