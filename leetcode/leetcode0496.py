# ****************************************************************分割线****************************************************************
# todo 0496（Next Greater Element I）
# 下一个更大元素

class Solution:
    # 嵌套循环（太慢）
    def nextGreaterElement(self, nums1: list, nums2: list) -> list:
        result = [-1] * len(nums1)
        i = 0
        while i < len(nums1):
            k = 0
            j = 0
            while j < len(nums2):
                if nums1[i] == nums2[j]:
                    k = j + 1
                    break
                j += 1
            while k < len(nums2):
                if nums2[k] > nums1[i]:
                    result[i] = nums2[k]
                    break
                k += 1
            i += 1
        return result

    # 哈希表存储nums2，nums1为nums2子集
    def nextGreaterElement2(self, nums1: list, nums2: list) -> list:
        result = [-1] * len(nums1)
        data = {}
        i = 0
        while i < len(nums2):
            data[nums2[i]] = i
            i += 1
        j = 0
        while j < len(nums1):
            k = data[nums1[j]]
            while k < len(nums2):
                if nums2[k] > nums1[j]:
                    result[j] = nums2[k]
                    break
                k += 1
            j += 1
        return result

    # 栈+哈希表
    def nextGreaterElement3(self, nums1: list, nums2: list) -> list:
        result = []
        stack = []
        data = {}
        # 把nums2中每个元素和右边更大元素建立对应关系
        for num in nums2:
            while len(stack) > 0 and stack[-1] < num:  # 碰到小的入栈，碰到大的全部出栈
                data[stack[-1]] = num
                stack.pop()
            stack.append(num)
        for num in nums1:
            result.append(data[num] if num in data else -1)
        return result

# print(Solution().nextGreaterElement([4,1,2],[1,3,4,2]))
# print(Solution().nextGreaterElement2([4,1,2],[1,3,4,2]))
print(Solution().nextGreaterElement3([1, 3, 5, 2, 4], [6, 5, 4, 3, 2, 1, 7]))
