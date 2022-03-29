# ****************************************************************分割线****************************************************************
# todo 0746（Min Cost Climbing Stairs）
# 爬楼梯最小花费
# 可以从index=0/1处开始爬，每次爬1/2步楼梯

class Solution:
    # DP（内存过大）
    def minCostClimbingStairs(self, cost: list) -> int:
        l = len(cost)
        dp = [[] for i in range(l + 1)]
        dp[0] = [[0]]
        dp[1] = [[0, 1], [1]]  # 坐标（走2个一步，走1个两步）
        i = 2
        while i < l + 1:
            for j in dp[i - 1]:
                temp = list(j)
                temp.append(temp[-1] + 1)
                dp[i].append(temp)
            for k in dp[i - 2]:
                temp = list(k)
                temp.append(temp[-1] + 2)
                dp[i].append(temp)
            i += 1
        # print(dp[2])

        min_val = sum(cost)
        for m in dp[l]:  # 这里是l而非l-1（顶层也算上），搭配n<len(cost)使用
            temp = 0
            for n in m:
                if n < len(cost):
                    temp += cost[n]
            min_val = min(min_val, temp)
        return min_val

    # fixme 焯
    # 每次可以走一步或两步，从第三步起，算下每次走路的最小花费
    def minCostClimbingStairs2(self, cost: list) -> int:
        l = len(cost)
        dp = [0] * (l + 1)
        i = 2
        while i < l + 1:
            dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])
            i += 1
        return dp[-1]

# print(Solution().minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
# print(Solution().minCostClimbingStairs([10,15,20]))

print(Solution().minCostClimbingStairs2([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
