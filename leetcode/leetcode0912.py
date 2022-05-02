# ****************************************************************分割线****************************************************************
# todo 0912（Sort an Array）
# 数组排序

class Solution:
    def test(self, left, right):
        output = []
        while left and right:
            if left[0] <= right[0]:
                output.append(left.pop(0))
            else:
                output.append(right.pop(0))
        while left:
            output.append(left.pop(0))
        while right:
            output.append(right.pop(0))
        return output

    def sortArray(self, nums: list) -> list:
        length = len(nums)
        if length <= 1:
            return nums

        middle = length // 2
        left, right = nums[0:middle], nums[middle:]
        return self.test(self.sortArray(left), self.sortArray(right))

print(Solution().sortArray([5, 4, 3, 2, 1]))
