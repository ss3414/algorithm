# ****************************************************************分割线****************************************************************
# todo 0349（Intersection of Two Arrays）
# 数组的交集
# 交集中的元素必须唯一

class Solution:
    # 哈希表
    def intersection(self, nums1: list, nums2: list) -> list:
        data = {}
        for num in nums1:
            data.update({num: 1})
        for num in nums2:
            if num in data.keys():
                data.update({num: 2})
        result = []
        for key, val in data.items():
            if val == 2:
                result.append(key)
        return result

    # 数组
    def intersection2(self, nums1: list, nums2: list) -> list:
        result = []
        for num in nums1:
            if num not in result and num in nums2:
                result.append(num)
        return result

# print(Solution().intersection([1,2,2,1],[2,2]))
print(Solution().intersection2([1, 2, 2, 1], [2, 2]))
