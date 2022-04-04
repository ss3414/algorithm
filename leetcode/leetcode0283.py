# ****************************************************************分割线****************************************************************
# todo 0283（Move Zeroes）
# 移动零

class Solution:
    # 冒泡（超时）
    def moveZeroes(self, nums: list) -> None:
        flag = True
        i = 0
        while i < len(nums) - 1:
            j = 0
            while j < len(nums) - 1:
                if nums[j] == 0:
                    nums[j] = nums[j + 1]
                    nums[j + 1] = 0
                    flag = False
                # print(nums)
                j += 1
            if flag:
                break
            i += 1

    # 快慢指针
    def moveZeroes2(self, nums: list) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
            if nums[slow] != 0:
                slow += 1
            print("{s} {f} {n}".format(s=slow, f=fast, n=nums))

# print(Solution().moveZeroes([0,1,0,2,0,3]))
# print(Solution().moveZeroes([0,0,0,1,2,3]))

print(Solution().moveZeroes2([0, 1, 0, 2, 0, 3]))
# print(Solution().moveZeroes2([0,0,0,1,2,3]))
