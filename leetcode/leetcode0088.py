# ****************************************************************分割线****************************************************************
# todo 0088（Merge Sorted Array）
# 合并两个有序数组

class Solution:
    # 从末端开始比较，大数往后挪
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        i = m + n - 1
        j = m - 1
        k = n - 1
        while j >= 0 and k >= 0:
            if nums1[j] > nums2[k]:
                temp = nums1[i]
                nums1[i] = nums1[j]
                nums1[j] = temp
                j -= 1
            elif nums1[j] <= nums2[k]:  # 因为nums1容量大于nums2，等号要写在这
                temp = nums1[i]
                nums1[i] = nums2[k]
                nums2[k] = temp
                k -= 1
            i -= 1
            print("nums1:{nums1} nums2:{nums2} i:{i} j:{j} k:{k}".format(nums1=nums1, nums2=nums2, i=i, j=j, k=k))
        while k >= 0:
            nums1[k] = nums2[k]
            k -= 1
        return nums1

    # 简化版
    def merge2(self, nums1: list, m: int, nums2: list, n: int) -> None:
        i = m + n - 1
        j = m - 1
        k = n - 1
        while k >= 0:  # 最极端情况nums2中元素最小，所以用k判断
            if j >= 0 and nums1[j] > nums2[k]:
                nums1[i] = nums1[j]
                j -= 1
            else:
                nums1[i] = nums2[k]
                k -= 1
            i -= 1
            print("nums1:{nums1} nums2:{nums2} i:{i} j:{j} k:{k}".format(nums1=nums1, nums2=nums2, i=i, j=j, k=k))
        return nums1

print(Solution().merge([2, 3, 4, 0, 0, 0], 3, [1, 2, 3], 3))  # 如果nums2中存在比nums1小的数，那么nums1前面会空出
# print(Solution().merge([2,3,4,0,0,0],3,[4,5,6],3))
# print(Solution().merge([1],1,[],0))
# print(Solution().merge([0],0,[1],1))
print(Solution().merge2([2, 3, 4, 0, 0, 0], 3, [1, 2, 3], 3))
