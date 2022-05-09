# ****************************************************************分割线****************************************************************
# todo 0778（Swim in Rising Water）
# 水位上升的泳池中游泳

class Solution:
    # 太慢
    def swimInWater(self, grid: list) -> int:
        def dfs(i, j, h, data):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] > h or (i, j) in data:
                return False

            # 用哈希表存储访问过的节点，避免死循环
            data[(i, j)] = False
            result = False
            if i == m - 1 and j == n - 1 and grid[i][j] <= h:
                result = True
            return result or dfs(i - 1, j, h, data) or dfs(i + 1, j, h, data) or dfs(i, j - 1, h, data) or dfs(i, j + 1, h, data)

        m, n = len(grid), len(grid[0])
        l, r = 0, 0
        for i in grid:
            r = max(r, max(i))
        while l <= r:
            mid = (l + r) // 2
            if dfs(0, 0, mid, {}):
                r = mid - 1
            else:
                l = mid + 1
        return l

grid = [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]
print(Solution().swimInWater(grid))
