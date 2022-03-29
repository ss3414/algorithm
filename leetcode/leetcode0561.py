# ****************************************************************分割线****************************************************************
# todo 0561（Array Partition I）
# 数组拆分

class Solution:
    # 冒泡（超时）
    def arrayPairSum(self, nums: list) -> int:
        flag = True
        i = 0
        while i < len(nums) - 1:
            j = 0
            while j < len(nums) - 1:
                if nums[j] > nums[j + 1]:
                    temp = nums[j + 1]
                    nums[j + 1] = nums[j]
                    nums[j] = temp
                    flag = False
                j += 1
            if flag:
                break
            i += 1
        sum = 0
        k = 0
        while k < len(nums):
            sum += nums[k]
            k += 2
        return sum

    # 凑数
    def arrayPairSum2(self, nums: list) -> int:
        return sum(sorted(nums)[::2])

# print(Solution().arrayPairSum([6,2,6,5,1,2]))
print(Solution().arrayPairSum2([6, 2, 6, 5, 1, 2]))
