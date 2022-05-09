# ****************************************************************分割线****************************************************************
# todo 0695（Max Area of Island）
# 最大面积的岛屿

class Solution:
    def maxAreaOfIsland(self, grid: list) -> int:
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
                return 0

            grid[i][j] = 0
            area = 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
            return area

        result = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            if grid[i].count(1) == 0:
                continue
            for j in range(n):
                if grid[i][j] == 1:
                    result = max(result, dfs(i, j))
        return result

grid = [[0, 1, 1, 0], [1, 0, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]]
print(Solution().maxAreaOfIsland(grid))
