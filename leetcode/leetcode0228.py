# ****************************************************************分割线****************************************************************
# todo 0228（Summary Ranges）
# 汇总区间

class Solution:
    def summaryRanges(self, nums: list) -> list:
        def test(start, end, result):
            if start != end:
                result.append("{start}->{end}".format(start=start, end=end))
            else:
                result.append(str(start))

        result = []
        length = len(nums)
        if length > 0:
            start, end = nums[0], nums[0]
            i = 0
            while i < length - 1:
                if nums[i] + 1 != nums[i + 1]:
                    end = nums[i]
                    test(start, end, result)
                    start, end = nums[i + 1], nums[i + 1]
                i += 1
            test(start, nums[length - 1], result)
        return result

print(Solution().summaryRanges([0, 1, 2, 4, 5, 6]))
# print(Solution().summaryRanges([0,1,2,4,5,7]))
