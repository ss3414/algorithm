# ****************************************************************分割线****************************************************************
# todo 0575（Distribute Candies）
# 分糖果

class Solution:
    def distributeCandies(self, candyType: list) -> int:
        data = {}
        for i in candyType:
            data[i] = 0
        return len(candyType) // 2 if len(data) >= len(candyType) // 2 else len(data)

print(Solution().distributeCandies([1, 1, 2, 2, 3, 3]))
