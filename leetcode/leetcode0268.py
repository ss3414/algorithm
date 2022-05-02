# ****************************************************************分割线****************************************************************
# todo 0268（Missing Number）
# 丢失的数字

class Solution:
    # 冒泡（超时）
    def missingNumber(self, nums: list) -> int:
        i = 0
        while i < len(nums) - 1:
            j = 0
            while j < len(nums) - 1:
                if nums[j] > nums[j + 1]:
                    temp = nums[j + 1]
                    nums[j + 1] = nums[j]
                    nums[j] = temp
                j += 1
            i += 1

        # 丢失的数字要么在两头，要么在中间
        k = 0
        while k < len(nums) - 1:
            if nums[k] + 1 != nums[k + 1]:
                return nums[k] + 1
            k += 1
        if nums[0] != 0:
            return 0
        else:
            return len(nums)

    # 哈希表
    def missingNumber2(self, nums: list) -> int:
        def test(input, data):
            if input in data.keys():
                data[input] = 2
            else:
                data[input] = 1

        data = {}
        length = len(nums)
        for num in nums:
            test(num, data)
            mirror = length - num
            test(mirror, data)
        # 数组长度为奇数（3），可能有4种数字（0~3）
        for key, val in data.items():
            if val == 1 and key not in nums:
                return key
        # 数组长度为偶数，可能丢失的是中间数字
        return length // 2

    # 等差数列前n项和
    def missingNumber3(self, nums: list) -> int:
        sum = 0
        for num in nums:
            sum += num
        n = len(nums)
        return int(0.5 * n * (n + 1)) - sum

# print(Solution().missingNumber([3,2,1]))
# print(Solution().missingNumber2([1,2,3]))
# print(Solution().missingNumber2([0,1,3,4]))
print(Solution().missingNumber3([0, 1, 3, 4]))
