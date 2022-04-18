# ****************************************************************分割线****************************************************************
# todo 0724（Find Pivot Index）
# 数组中心下标

class Solution:
    # 池沼算法
    def pivotIndex(self, nums: list) -> int:
        # 最左侧/最右侧
        if sum(nums[1::]) == 0:
            return 0
        if sum(nums[:-1:]) == 0:
            return len(nums) - 1

        i, j = 0, (len(nums) - 1)
        d = nums[i] - nums[j]
        while d != 0 and i < j:
            if d > 0:
                j -= 1
                d -= nums[j]
            if d < 0:
                i += 1
                d += nums[i]
            print("{i} {j}".format(i=i, j=j))
            if d == 0 and i + 2 == j:
                return i + 1
        return -1

    def pivotIndex2(self, nums: list) -> int:
        sum1 = sum(nums)
        sum2 = 0
        i = 0
        while i < len(nums):
            print("{i} {j}".format(i=sum1 - nums[i], j=2 * sum2))
            if sum1 - nums[i] == 2 * sum2:  # 左+中+右，左=右
                return i
            sum2 += nums[i]
            i += 1
        return -1

# print(Solution().pivotIndex([-1,-1,-1,-1,-1,0]))
print(Solution().pivotIndex2([1, 7, 3, 6, 5, 6]))
