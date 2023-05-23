# ****************************************************************分割线****************************************************************
# todo 0766（Toeplitz Matrix）
# 对角线矩阵

class Solution:
    def isToeplitzMatrix(self, matrix: list) -> bool:
        row, col = len(matrix[0]), len(matrix)
        temp = matrix[0][0:row - 1]
        for i in range(1, col):
            if temp != matrix[i][1:row]:
                return False
            temp = matrix[i][0:row - 1]
        return True

print(Solution().isToeplitzMatrix([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]))
