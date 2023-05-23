# ****************************************************************分割线****************************************************************
# todo 0495（Teemo Attacking）
# 提莫攻击（时间重叠）

class Solution:
    def findPoisonedDuration(self, timeSeries: list, duration: int) -> int:
        sum = 0
        start = timeSeries[0]
        end = timeSeries[0] + duration
        i = 1
        while i < len(timeSeries):
            if timeSeries[i] <= end:  # 重叠
                end = timeSeries[i] + duration
            else:
                sum += (end - start)
                start = timeSeries[i]
                end = timeSeries[i] + duration
            print("{b} {e}".format(b=start, e=end))
            i += 1
        sum += (end - start)
        return sum

print(Solution().findPoisonedDuration([1, 3, 5], 2))
# print(Solution().findPoisonedDuration([1],2))
