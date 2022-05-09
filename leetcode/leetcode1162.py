# ****************************************************************分割线****************************************************************
# todo 1162（As Far from Land as Possible）
# 离岛屿最远的水域

class Solution:
    # 太慢
    def maxDistance(self, grid: list) -> int:
        m, n = len(grid), len(grid[0])
        # 先让所有陆地坐标入队
        queue = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((1, i, j))

        # 先填充陆地坐标四周，再填充距离坐标
        result = -1
        while queue:
            d, oi, oj = queue.pop(0)
            for i, j in [(0, -1), (-1, 0), (1, 0), (0, 1)]:  # 上下左右
                ni, nj = oi + i, oj + j
                if 0 <= ni < m and 0 <= nj < n:
                    if grid[ni][nj] == 0:
                        grid[ni][nj] = d
                        queue.append((d + 1, ni, nj))
                        result = max(result, d)
            print(grid)
        return result

grid = [[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]]
print(Solution().maxDistance(grid))
