# ****************************************************************分割线****************************************************************
# todo 0075（Sort Colors）
# 颜色排序
# 升序从小到大排

class Solution:
    # 优化后的冒泡排序
    def sortColors(self, nums: list) -> None:
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
        print(nums)

    # 选择排序（无法优化，不能因为没有交换断定已排序完）
    def sortColors2(self, nums: list) -> None:
        i = 0
        while i < len(nums) - 1:
            j = i + 1
            while j < len(nums):
                if nums[i] > nums[j]:
                    temp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = temp
                j += 1
            print(nums)
            i += 1

    # 计数排序（适合元素多但范围窄的数组）
    def sortColors3(self, nums: list) -> None:
        counts = [0] * 3
        for num in nums:
            counts[num] += 1
        i, j = 0, 0
        while i < len(counts):
            while counts[i] > 0:
                nums[j] = i
                counts[i] -= 1
                j += 1
            i += 1
        print(nums)

# Solution().sortColors([0,0,1,1,2,2])
# Solution().sortColors2([0,2,1])
Solution().sortColors3([0, 0, 1, 1, 2, 2])
