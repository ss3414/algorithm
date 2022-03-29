# ****************************************************************分割线****************************************************************
# todo 0495（Teemo Attacking）
# 提莫攻击（时间重叠）

class Solution:
    def findPoisonedDuration(self, timeSeries: list, duration: int) -> int:
        sum = 0
        begin = timeSeries[0]
        end = timeSeries[0] + duration
        i = 1
        while i < len(timeSeries):
            if timeSeries[i] <= end:  # 重叠
                end = timeSeries[i] + duration
            else:
                sum += (end - begin)
                begin = timeSeries[i]
                end = timeSeries[i] + duration
            print("{b} {e}".format(b=begin, e=end))
            i += 1
        sum += (end - begin)
        return sum

print(Solution().findPoisonedDuration([1, 3, 5], 2))
# print(Solution().findPoisonedDuration([1],2))
