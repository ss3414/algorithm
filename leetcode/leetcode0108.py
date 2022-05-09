# ****************************************************************分割线****************************************************************
# todo 0108（Convert Sorted Array to Binary Search Tree）
# 有序数组转换为高度平衡二叉搜索树

from common import TreeNode

class Solution:
    # 二分法+递归
    def sortedArrayToBST(self, nums: list) -> TreeNode:
        def test(nums, left, right):
            if left > right:
                return None

            middle = (left + right) // 2
            root = TreeNode(nums[middle])
            print(nums[middle])
            root.left = test(nums, left, middle - 1)
            root.right = test(nums, middle + 1, right)
            return root

        return test(nums, 0, len(nums) - 1)

Solution().sortedArrayToBST([1, 2, 3, 4, 5, 6, 7])
