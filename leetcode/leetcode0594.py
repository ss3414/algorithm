# ****************************************************************分割线****************************************************************
# todo 0594（Longest Harmonious Subsequence）
# 最长和谐子序列

class Solution:
    def findLHS(self, nums: list) -> int:
        data = {}
        for num in nums:
            if num in data.keys():
                data.update({num: data[num] + 1})
            else:
                data.update({num: 1})
        result = 0
        for key in data.keys():
            if key + 1 in data.keys():
                temp = data[key] + data[key + 1]
                result = max(result, temp)
        return result

# print(Solution().findLHS([1,3,2,2,5,2,3,7]))
print(Solution().findLHS([1, 1, 1, 1]))
