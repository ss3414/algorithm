# ****************************************************************分割线****************************************************************
# todo 0414（Third Maximum Number）
# 第三大数字

class Solution:
    def thirdMax(self, nums: list) -> int:
        first = second = third = -2 ** 31 - 1
        for num in nums:
            if num > first:
                third = second
                second = first
                first = num
            elif first > num > second:
                third = second
                second = num
            elif second > num > third:
                third = num
        # print("{f} {s} {t}".format(f=first,s=second,t=third))
        if third != -2 ** 31 - 1:
            return third
        else:
            return first

print(Solution().thirdMax([1, 6, 3, 4, 5, 2]))
