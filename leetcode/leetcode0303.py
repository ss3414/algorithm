# ****************************************************************分割线****************************************************************
# todo 0303（Range Sum Query - Immutable）
# 实现范围求和

# 太慢
class NumArray:
    def __init__(self, nums: list):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        sum = 0
        while left <= right:
            sum += self.nums[left]
            left += 1
        return sum

# 数组初始化后不会变化，初始化时将每项的前n项和计算好
class NumArray2:
    def __init__(self, nums: list):
        self.dp = nums
        i = 1
        while i < len(nums):
            self.dp[i] += self.dp[i - 1]
            i += 1

    def sumRange(self, left: int, right: int) -> int:
        return self.dp[right] if left == 0 else self.dp[right] - self.dp[left - 1]

# obj = NumArray([1,2,3,4,5])
# print(obj.sumRange(1,3))

obj = NumArray2([1, 2, 3, 4, 5])
print(obj.sumRange(1, 3))
