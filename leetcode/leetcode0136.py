# ****************************************************************分割线****************************************************************
# todo 0136（Single Number）
# 只出现一次的数字

class Solution:
    # 位运算
    def singleNumber(self, nums: list) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result

    # 哈希表（太慢）
    def singleNumber2(self, nums: list) -> int:
        data = {}
        for num in nums:
            if num in data:
                data[num] = data[num] + 1
            else:
                data[num] = 1
        for key, val in data.items():
            if val == 1:
                return key

# print(Solution().singleNumber([4,2,1,1,2]))
print(Solution().singleNumber2([4, 2, 1, 1, 2]))
