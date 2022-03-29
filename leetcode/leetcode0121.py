# ****************************************************************分割线****************************************************************
# todo 0121（Best Time to Buy and Sell Stock）
# 买卖股票的最佳时机
# 低价买高价卖，没有低价则不买

class Solution:
    # 池沼算法
    def maxProfit(self, prices: list) -> int:
        min, max = [0, prices[0]], [0, prices[0]]
        i = 0
        while i < len(prices):
            if prices[i] < min[1]:
                min[0] = max[0] = i
                min[1] = max[1] = prices[i]
            if prices[i] > max[1]:
                max[0] = i
                max[1] = prices[i]
            # print("max:{max} min:{min}".format(max=max,min=min))
            if i == len(prices) - 1 and max[0] > min[0]:
                return max[1] - min[1]
            i += 1
        return 0

    def maxProfit2(self, prices: list) -> int:
        result = 0
        data1, data2 = [0, prices[0]], [0, prices[0]]
        i = 0
        # 碰到小的data1,data2重新赋值，碰到大的data2赋值，取data1,data2最大差值
        while i < len(prices):
            if prices[i] < data1[1]:
                data1[0] = data2[0] = i
                data1[1] = data2[1] = prices[i]
            if prices[i] > data2[1]:
                data2[0] = i
                data2[1] = prices[i]
            result = max(result, data2[1] - data1[1])
            i += 1
        return result

    # maxProfit2的简化版
    def maxProfit3(self, prices: list) -> int:
        result = 0
        buy = 10 ** 4 + 1
        for price in prices:
            buy = min(buy, price)
            result = max(result, price - buy)
        return result

# print(Solution().maxProfit([7,1,5,3,6,4]))
# print(Solution().maxProfit2([2,4,1]))
print(Solution().maxProfit3([2, 4, 1]))
