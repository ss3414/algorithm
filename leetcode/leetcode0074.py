# ****************************************************************分割线****************************************************************
# todo 0074（Search a 2D Matrix）
# 矩阵中搜索

class Solution:
    # 太慢
    def searchMatrix(self, matrix: list, target: int) -> bool:
        for row in matrix:
            if row[-1] >= target:
                return target in row
        return False

print(Solution().searchMatrix([[1], [3]], 1))
