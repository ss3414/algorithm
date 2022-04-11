# ****************************************************************分割线****************************************************************
# todo 0035（Search Insert Position）
# 寻找target在有序数组中的插入位置

import bisect

# 暴力
def test(nums: list, target: int):
    i = 0
    while i < len(nums) - 1:
        if nums[i] <= target <= nums[i + 1]:  # 插入区间
            if target == nums[i]:
                return i  # 左
            else:
                return i + 1  # 右
        i += 1
    if len(nums) > 0 and target <= nums[0]:
        return 0  # 比所有元素小
    else:
        return len(nums)  # 比所有元素大

# test的简化版
def test2(nums: list, target: int):
    i = 0
    while i < len(nums):
        if nums[i] >= target:
            return i
        i += 1
    return len(nums)

# 二分法
def test3(nums: list, target: int):
    low, high = 0, len(nums)  # 给多个变量赋值
    middle = 0
    while low < high:
        middle = (low + high) // 2
        print("low:{low} high:{high} mid:{mid} target:{target} middle:{middle} left:{left} right:{right}".format(
            low=low, high=high, mid=middle, target=target, middle=nums[middle], left=nums[low:middle], right=nums[middle:high]))
        if target > nums[middle]:
            low = middle + 1
        else:
            high = middle
    print("low:{low} high:{high} mid:{mid} target:{target} middle:{middle} left:{left} right:{right}".format(
        low=low, high=high, mid=middle, target=target, middle=nums[middle], left=nums[low:middle], right=nums[middle:high]))
    return low

# bisect/数组二分查找算法（调用bisect，底层等价于test3）
def test4(nums: list, target: int):
    return bisect.bisect_left(nums, target)

# fixme linear/线性回归算法
def test5(nums: list, target: int):
    if not nums:
        return 0
    for i, num in enumerate(nums):
        print("i:{i} num:{num}".format(i=i, num=num))  # 下标/值
        if num >= target:
            return i
    return len(nums)

# print(test([1,3,5,7],3))
# print(test([1,3,5,7],0))
# print(test([1,3,5,7],9))

# print(test3([1,3,5,7],3))
# print(test3([1,3,5,7],0))
# print(test3([1,3,5,7],9))
# print(test4([1,3,5,7],3))

print(test5([1, 3, 5, 7], 3))
