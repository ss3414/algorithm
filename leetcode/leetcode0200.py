# ****************************************************************分割线****************************************************************
# todo 0200（Number of Islands）
# 岛屿的数量

class Solution:
    def numIslands(self, grid: list) -> int:
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != "1":
                return 0

            grid[i][j] = "0"
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
            return 1

        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            if grid[i].count("1") == 0:
                continue
            for j in range(n):
                if grid[i][j] == "1":
                    count += dfs(i, j)
        return count

grid = [["1", "0", "0", "0"], ["0", "1", "0", "0"], ["0", "0", "1", "0"], ["0", "0", "0", "1"]]
print(Solution().numIslands(grid))
