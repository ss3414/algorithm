# ****************************************************************分割线****************************************************************
# todo 1018（Binary Prefix Divisible By 5）
# 可被5整除的二进制前缀

class Solution:
    def prefixesDivBy5(self, nums: list) -> list:
        total, result = 0, []
        for num in nums:
            total <<= 1
            total += num
            result.append(total % 5 == 0)
        return result

print(Solution().prefixesDivBy5([1, 0, 1]))
print(Solution().prefixesDivBy5([1, 1, 1]))
