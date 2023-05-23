# ****************************************************************分割线****************************************************************
# todo 0905（Sort Array By Parity）
# 数组奇偶排序

class Solution:
    # 太慢
    def sortArrayByParity(self, nums: list) -> list:
        left, right = 0, 0
        while right < len(nums) - 1:
            while nums[left] % 2 == 0 and left < len(nums) - 1:
                left += 1
            right = left
            while nums[right] % 2 == 1 and right < len(nums) - 1:
                right += 1
            # print("l:{l} r:{r}".format(l=left,r=right))
            if nums[left] % 2 == 1 and nums[right] % 2 == 0:
                nums[left], nums[right] = nums[right], nums[left]
        return nums

    def sortArrayByParity2(self, nums: list) -> list:
        i, j = 0, len(nums) - 1
        while i < len(nums):
            if nums[i] % 2 != 0:
                while i < j:
                    if nums[j] % 2 == 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                    else:
                        j -= 1
            i += 1
        return nums

# print(Solution().sortArrayByParity([1,2,3,4,5]))
# print(Solution().sortArrayByParity([2,1]))
# print(Solution().sortArrayByParity([0]))
print(Solution().sortArrayByParity2([1, 2, 3, 4, 5]))
