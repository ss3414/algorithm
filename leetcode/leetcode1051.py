# ****************************************************************分割线****************************************************************
# todo 1051（Height Checker）
# 高度检查

class Solution:
    def heightChecker(self, heights: list) -> int:
        count = 0
        temp = sorted(heights)
        i = 0
        while i < len(heights):
            if heights[i] != temp[i]:
                count += 1
            i += 1
        return count

print(Solution().heightChecker([1, 1, 4, 5, 1, 4]))
