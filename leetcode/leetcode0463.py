# ****************************************************************分割线****************************************************************
# todo 0463（Island Perimeter）
# 岛屿的周长
# 0代表水，1代表岛屿，只有一个岛屿

class Solution:
    # 枚举（从正方形四个边入手）
    def islandPerimeter(self, grid: list) -> int:
        result = 0
        if len(grid) == 0 or len(grid[0]) == 0:
            return result
        row = len(grid)
        col = len(grid[0])
        i = 0
        while i < row:
            j = 0
            while j < col:
                if grid[i][j] == 0:
                    j += 1
                    continue
                if i == 0 or grid[i - 1][j] == 0:  # 左边贴墙或左边是水，周长加一
                    result += 1
                if j == 0 or grid[i][j - 1] == 0:  # 上边
                    result += 1
                if i == row - 1 or grid[i + 1][j] == 0:  # 右边
                    result += 1
                if j == col - 1 or grid[i][j + 1] == 0:  # 下边
                    result += 1
                j += 1
            i += 1
        return result

    def islandPerimeter2(self, grid: list) -> int:
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
                return 0
            grid[i][j] = -1
            result = 4 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
            # 如果左侧或上方为陆地，则减去重复计算的两条边
            if i > 0 and grid[i - 1][j] != 0:
                result -= 2
            if j > 0 and grid[i][j - 1] != 0:
                result -= 2
            print("({i},{j}) {a}".format(i=i, j=j, a=result))
            return result

        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return dfs(i, j)

# grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
# print(Solution().islandPerimeter(grid))
grid = [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
print(Solution().islandPerimeter2(grid))
