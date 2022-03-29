# ****************************************************************分割线****************************************************************
# todo 0566（Reshape the Matrix）
# 重塑矩阵

class Solution:
    # fixme 行列式的转换公式
    def matrixReshape(self, mat: list, r: int, c: int) -> list:
        breadth = len(mat[0])
        height = len(mat)
        # 无法转换,直接返回
        if breadth * height != r * c:
            return mat
        result = [[0 for i in range(c)] for j in range(r)]
        x = 0
        while x < r:
            y = 0
            while y < c:
                k = x * c + y
                result[x][y] = mat[int(k // breadth)][k % breadth]
                y += 1
            x += 1
        return result

grid = [[1, 2], [3, 4]]
print(Solution().matrixReshape(grid, 1, 4))
