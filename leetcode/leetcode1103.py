# ****************************************************************分割线****************************************************************
# todo 1103（Distribute Candies to People）
# 分糖果

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> list:
        result = [0] * num_people
        i = 0
        while candies > 0:
            for j in range(num_people):
                val = min(candies, i * num_people + j + 1)
                result[j] += val
                candies -= val
            i += 1
        return result

print(Solution().distributeCandies(7, 4))
