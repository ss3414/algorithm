# ****************************************************************分割线****************************************************************
# todo 0027（Remove Element）
# 删除数组中指定元素，返回最终数组长度

class Solution:
    # ①题目要求只允许对输入数组进行操作，不允许新建其他数据结构
    # ②LeetCode根据返回值截取nums数组判断是否符合条件，即便nums中重复元素没删完不影响判断
    # ③有些语言不允许更改数组长度，LeetCode只能使用这种机制检测
    def removeElement(self, nums: list, val: int) -> int:
        result = 0
        i = 0
        while i < len(nums):
            if nums[i] != val:
                nums[result] = nums[i]
                result += 1
            i += 1
            # result是截取数组的边界，在不允许新建其他数据结构的情况下，把原数组前半段看做新数组
            print(nums[0:result])
        return result

print(Solution().removeElement([3, 2, 2, 3], 3))
print(Solution().removeElement([2], 3))
