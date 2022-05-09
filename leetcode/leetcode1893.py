# ****************************************************************分割线****************************************************************
# todo 1893（Check if All the Integers in a Range Are Covered）
# 区间覆盖

class Solution:
    # fixme 差分数组
    def isCovered(self, ranges: list, left: int, right: int) -> bool:
        diff = [0] * 51
        for i in ranges:
            diff[i[0]] += 1
            if i[1] + 1 < 51:
                diff[i[1] + 1] -= 1
        j = 2
        while j < 51:
            diff[j] += diff[j - 1]
            j += 1
        for k in range(left, right + 1):
            if diff[k] == 0:
                return False
        return True

# print(Solution().isCovered([[1,2],[3,4],[5,6]],2,5))
print(Solution().isCovered([[1, 20]], 1, 50))
