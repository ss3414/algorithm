# ****************************************************************分割线****************************************************************
# todo 0922（Sort Array By Parity II）
# 数组奇偶排序II

class Solution:
    def sortArrayByParityII(self, nums: list) -> list:
        odd, even = [], []
        i = 0
        while i < len(nums):
            if i % 2 == 1 and nums[i] % 2 != 1:
                odd.append(i)
            if i % 2 == 0 and nums[i] % 2 != 0:
                even.append(i)
            i += 1
        while odd and even:
            l, r = odd.pop(), even.pop()
            nums[l], nums[r] = nums[r], nums[l]
        return nums

# print(Solution().sortArrayByParityII([1,2,3,4]))
print(Solution().sortArrayByParityII([648, 831, 560, 986, 192, 424, 997, 829, 897, 843]))
