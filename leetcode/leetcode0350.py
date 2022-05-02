# ****************************************************************分割线****************************************************************
# todo 0350（Intersection of Two Arrays II）
# 数组的交集II
# 允许交集元素重复

class Solution:
    # 哈希表
    def intersect(self, nums1: list, nums2: list) -> list:
        result = []
        data = {}
        for num in nums1:
            if num in data.keys():
                data[num] = data[num] + 1
            else:
                data[num] = 1
        for num in nums2:
            if num in data.keys() and data[num] > 0:
                data[num] = data[num] - 1
                result.append(num)
        return result

    # 双指针
    def intersect2(self, nums1: list, nums2: list) -> list:
        result = []
        nums1, nums2 = sorted(nums1), sorted(nums2)
        index1 = index2 = 0
        while True:
            try:
                if nums1[index1] > nums2[index2]:
                    index2 += 1
                elif nums1[index1] < nums2[index2]:
                    index1 += 1
                else:
                    result.append(nums1[index1])
                    index1 += 1
                    index2 += 1
            except IndexError:
                break
        return result

# print(Solution().intersect([1,2,2,1],[2,2]))
print(Solution().intersect2([1, 2, 2, 1], [2, 2]))
