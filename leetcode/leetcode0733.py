# ****************************************************************分割线****************************************************************
# todo 0733（Flood Fill）
# 图像渲染

class Solution:
    def floodFill(self, image: list, sr: int, sc: int, newColor: int) -> list:
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or image[i][j] != color:
                return

            image[i][j] = newColor
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        m, n = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor:  # 新旧颜色相同
            return image
        dfs(sr, sc)
        return image

print(Solution().floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
# print(Solution().floodFill([[0,0,0],[0,1,1]],1,1,1))
