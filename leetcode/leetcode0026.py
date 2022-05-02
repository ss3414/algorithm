# ****************************************************************分割线****************************************************************
# todo 0026（Remove Duplicates from Sorted Array）
# 删除有序数组中的重复数，返回有多少个不相同的数

class Solution:
    # 哈希表
    def removeDuplicates(self, nums: list) -> int:
        data = {}
        i = 0
        while i < len(nums):
            data[nums[i]] = i
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
    def removeDuplicates2(self, nums: list) -> int:
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
        return result

test = [1, 1, 2, 2, 3, 3]  # 输入数组是有序的
print(Solution().removeDuplicates(test))
print(Solution().removeDuplicates2(test))
