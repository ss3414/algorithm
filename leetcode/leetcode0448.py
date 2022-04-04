# ****************************************************************分割线****************************************************************
# todo 0448（Find All Numbers Disappeared in an Array）
# 寻找缺少的数字

class Solution:
    # 哈希表
    def findDisappearedNumbers(self, nums: list) -> list:
        data = {}
        for i in range(1, len(nums) + 1):
            data.update({i: 0})
        for num in nums:
            data.update({num: data[num] + 1})
        result = []
        for key, val in data.items():
            if val == 0:
                result.append(key)
        return result

    # 数组
    def findDisappearedNumbers2(self, nums: list) -> list:
        i = 0
        while i < len(nums):
            if nums[i] != nums[nums[i] - 1]:
                temp = nums[i]
                nums[i] = nums[temp - 1]
                nums[temp - 1] = temp
                # print(nums)
                i -= 1  # 交换完后退一步，避免大数被交换到前面
            i += 1
        result = []
        j = 0
        while j < len(nums):
            if nums[j] - 1 != j:
                result.append(j + 1)
            j += 1
        return result

# print(Solution().findDisappearedNumbers([1,1,4,5,1,4]))
print(Solution().findDisappearedNumbers2([1, 1, 4, 5, 1, 4]))
