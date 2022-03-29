# ****************************************************************分割线****************************************************************
# todo 0463（Island Perimeter）
# 岛屿的周长
# 0代表水，1代表岛屿，只有一个岛屿

class Solution:
    # 池沼算法
    def islandPerimeter(self, grid: list) -> int:
        # 长宽
        row = len(grid)
        col = len(grid[0])
        island = 0  # 岛屿面积（周长=岛屿面积*4-岛屿相连处*2）
        link = 0  # 岛屿相连处
        i = 0
        while i < row:
            island += sum(grid[i])
            link += max(0, (sum(grid[i]) - 1))  # 横纵减一不能保证岛屿一定相连
            i += 1
        j = 0
        while j < col:
            k = 0
            vertical = 0
            while k < row:
                vertical += grid[k][j]
                k += 1
            link += max(0, (vertical - 1))
            j += 1
        print("{island} {link}".format(island=island, link=link))

    # 从正方形四个边入手
    def islandPerimeter2(self, grid: list) -> int:
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

grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
# print(Solution().islandPerimeter(grid))
print(Solution().islandPerimeter2(grid))
