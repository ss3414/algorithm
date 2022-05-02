# ****************************************************************分割线****************************************************************
# todo 0011（Container With Most Water）
# 盛最多水的容器

class Solution:
    def maxArea(self, height: list) -> int:
        i, j = 0, len(height) - 1
        result = 0
        while i < j:
            result = max(result, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return result

print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
