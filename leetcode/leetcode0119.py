# ****************************************************************分割线****************************************************************
# todo 0119（Pascal's Triangle II）
# 帕斯卡三角/杨辉三角II

class Solution:
    def getRow(self, rowIndex: int) -> list:
        result = [[]] * (rowIndex + 1)
        result[0] = [1]
        if rowIndex == 0:
            return result[rowIndex]
        result[1] = [1, 1]
        if rowIndex == 1:
            return result[rowIndex]
        level = 3
        while level <= (rowIndex + 1):
            result[level - 1] = [1] * level
            index = 1
            while index < level - 1:
                result[level - 1][index] = result[level - 2][index - 1] + result[level - 2][index]
                index += 1
            level += 1
        return result[rowIndex]

print(Solution().getRow(4))
