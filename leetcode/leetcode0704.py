# ****************************************************************分割线****************************************************************
# todo 0704（Binary Search）
# 二分法

class Solution:
    def search(self, nums: list, target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            print("{l} {r}".format(l=left, r=right))
            middle = (left + right) // 2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle
        return -1

# print(Solution().search([-1,0,3,5,9,12],9))
print(Solution().search([-1, 0, 3, 5, 9, 12], 5))
# print(Solution().search([-1,0,3,5,9,12],2))
