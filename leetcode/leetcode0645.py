# ****************************************************************分割线****************************************************************
# todo 0645（Set Mismatch）
# 错误的集合

class Solution:
    def findErrorNums(self, nums: list) -> list:
        n = len(nums)
        data = {}
        for i in nums:
            if i in data:
                data[i] += 1
            else:
                data[i] = 1
        result = []
        sum = 0
        for key, val in data.items():
            sum += key
            if val == 2:
                result.append(key)
        miss = int(0.5 * n * (n + 1)) - sum
        result.append(miss)
        return result

print(Solution().findErrorNums([2, 2, 3]))
print(Solution().findErrorNums([2, 3, 3, 4, 6, 5]))
