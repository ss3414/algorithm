# ****************************************************************分割线****************************************************************
# todo 0961（N-Repeated Element in Size 2N Array）
# 重复N次的元素

class Solution:
    def repeatedNTimes(self, nums: list) -> int:
        data = {}
        for i in nums:
            if i in data:
                return i
            else:
                data[i] = 1

print(Solution().repeatedNTimes([1, 2, 3, 3]))
