# ****************************************************************分割线****************************************************************
# todo 0661（Image Smoother）
# 图片平滑
# 取每个元素及其周边8个元素的平均值

class Solution:
    def imageSmoother(self, img: list) -> list:
        r = len(img)
        c = len(img[0])
        result = [[0 for i in range(c)] for j in range(r)]
        x = 0
        while x < r:
            y = 0
            while y < c:
                average = 0
                count = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if x + i >= 0 and x + i < r and y + j >= 0 and y + j < c:
                            try:
                                average += img[x + i][y + j]
                                count += 1
                            except Exception as e:
                                print("{x},{y}".format(x=x + i, y=y + j))
                result[x][y] = average // count
                y += 1
            x += 1
        return result

# grid=[[1,2,3],[4,5,6],[7,8,9]]
grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
print(Solution().imageSmoother(grid))
