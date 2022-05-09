# ****************************************************************分割线****************************************************************
# todo 0307（Range Sum Query - Mutable）
# 区间和搜索（数组可变）

# 线段树
# 输入：1,2,3
#    6
#  3   3
# 1 2
# 输出：6,3,3,1,2
#
# 输入：1,2,3,4
#   10
#  3   7
# 1 2 3 4
# 输出：10,3,7,1,2,3,4

class NumArray:
    def __init__(self, nums: list):
        self.n = len(nums)
        self.tree = [None] * (4 * self.n)
        self.build(nums, 0, 0, self.n - 1)
        print(self.tree)

    def build(self, nums: list, position: int, left: int, right: int):
        if left == right:
            self.tree[position] = nums[left]
            print(self.tree)
            return

        middle = (left + right) // 2
        self.build(nums, 2 * position + 1, left, middle)
        self.build(nums, 2 * position + 2, middle + 1, right)
        self.tree[position] = self.tree[2 * position + 1] + self.tree[2 * position + 2]

    def updateUtil(self, position: int, left: int, right: int, index: int, val: int):
        if index < left or index > right:
            return
        if left == right:
            if left == index:
                self.tree[position] = val
            return

        middle = (left + right) // 2
        self.updateUtil(2 * position + 1, left, middle, index, val)
        self.updateUtil(2 * position + 2, middle + 1, right, index, val)
        self.tree[position] = self.tree[2 * position + 1] + self.tree[2 * position + 2]

    # 替换输入数组指定位置的元素
    def update(self, index: int, val: int):
        self.updateUtil(0, 0, self.n - 1, index, val)

    def rangeUtil(self, qlow: int, qhigh: int, low: int, high: int, position: int) -> int:
        if qlow <= low and qhigh >= high:
            return self.tree[position]
        if qlow > high or qhigh < low:
            return 0

        middle = low + (high - low) // 2
        return self.rangeUtil(qlow, qhigh, low, middle, 2 * position + 1) + self.rangeUtil(qlow, qhigh, middle + 1, high, 2 * position + 2)

    # 求输入数组指定区间的和
    def sumRange(self, left: int, right: int) -> int:
        return self.rangeUtil(left, right, 0, self.n - 1, 0)

obj = NumArray([1, 2, 3, 4])
print(obj.sumRange(0, 2))
obj.update(1, 3)
print(obj.sumRange(0, 2))
