# ****************************************************************分割线****************************************************************
# todo 0162（Find Peak Element）
# 寻找顶峰元素

class Solution:
    # 二分法
    def findPeakElement(self, nums: list) -> int:
        result = []

        def test(left, right):
            middle = left + (right - left) // 2
            # print("{l} {r} {m}".format(l=left,r=right,m=middle))
            if nums[middle] > nums[middle + 1] and nums[middle] > nums[middle - 1]:
                result.append(middle)
            if left < right:
                test(left, middle)
                test(middle + 1, right)
            else:
                return

        nums.insert(0, -2 ** 31 - 1)
        nums.append(-2 ** 31 - 1)
        left, right = 1, len(nums) - 2
        test(left, right)
        # print(result)
        return result[0] - 1

    # 线性扫描
    def findPeakElement2(self, nums: list) -> int:
        nums.insert(0, -2 ** 31 - 1)
        nums.append(-2 ** 31 - 1)
        i = 1
        while i < len(nums) - 1:
            if nums[i] > nums[i + 1] and nums[i] > nums[i - 1]:
                return i - 1
            i += 1
        return -1

# print(Solution().findPeakElement([0]))
# print(Solution().findPeakElement([1,2,1,3,5,6,4]))
print(Solution().findPeakElement2([1, 2, 1, 3, 5, 6, 4]))
