# ****************************************************************分割线****************************************************************
# todo 0228（Summary Ranges）
# 汇总区间

class Solution:
    def summaryRanges(self, nums: list) -> list:
        def test(begin, end, result):
            if begin != end:
                result.append("{begin}->{end}".format(begin=begin, end=end))
            else:
                result.append(str(begin))

        result = []
        length = len(nums)
        if length > 0:
            begin, end = nums[0], nums[0]
            i = 0
            while i < length - 1:
                if nums[i] + 1 != nums[i + 1]:
                    end = nums[i]
                    test(begin, end, result)
                    begin, end = nums[i + 1], nums[i + 1]
                i += 1
            test(begin, nums[length - 1], result)
        return result

print(Solution().summaryRanges([0, 1, 2, 4, 5, 6]))
# print(Solution().summaryRanges([0,1,2,4,5,7]))
