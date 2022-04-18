# ****************************************************************分割线****************************************************************
# todo 1512（Number of Good Pairs）
# 好数对

class Solution:
    def numIdenticalPairs(self, nums: list) -> int:
        result = 0
        data = {}
        for i in nums:
            if i in data.keys():
                data.update({i: data[i] + 1})
            else:
                data.update({i: 1})
        for key, val in data.items():
            if val > 1:
                result += int(0.5 * val * (val - 1))
        return result

print(Solution().numIdenticalPairs([1, 1, 4, 5, 1, 4]))
