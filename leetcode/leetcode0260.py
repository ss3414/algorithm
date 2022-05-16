# ****************************************************************分割线****************************************************************
# todo 0260（Single Number III）
# 只出现一次的数字III

class Solution:
    def singleNumber(self, nums: list) -> list:
        diff = nums[0]
        i = 1
        while i < len(nums):
            diff ^= nums[i]
            i += 1
        diff &= -diff  # 将原数组拆分的变量（找到第1位不是0的）
        print("{d} {b}".format(d=diff, b=bin(diff)))
        result = [0, 0]
        for j in nums:
            if j & diff:
                result[0] ^= j
            else:
                result[1] ^= j
        return result

# 所有数按位与，得到3^5，011^101=110
# 110&-110=10，可以用10把011和101区分开，其他数成对出现不会影响结果
print(Solution().singleNumber([1, 2, 1, 3, 2, 5]))
