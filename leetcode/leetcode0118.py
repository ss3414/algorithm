# ****************************************************************分割线****************************************************************
# todo 0118（Pascal's Triangle）
# 帕斯卡三角/杨辉三角

class Solution:
    def generate(self, numRows: int) -> list:
        result = [[]] * numRows
        result[0] = [1]
        if numRows == 1:
            return result
        result[1] = [1, 1]
        if numRows == 2:
            return result
        level = 3
        while level <= numRows:
            result[level - 1] = [1] * level
            index = 1
            while index < level - 1:  # 从第3层第2个元素开始
                result[level - 1][index] = result[level - 2][index - 1] + result[level - 2][index]
                index += 1
            level += 1
        return result

print(Solution().generate(5))
