# ****************************************************************分割线****************************************************************
# todo 0230（Kth Smallest Element in a BST）
# 二叉搜索树第K小的元素

from common import TreeNode

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        result = []

        def dfs(root: TreeNode):
            if root is None:
                return
            if root.left:
                dfs(root.left)
            result.append(root.val)
            if root.right:
                dfs(root.right)

        dfs(root)
        return result[k - 1]

left = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
right = TreeNode(6, left=TreeNode(5), right=TreeNode(7))
root = TreeNode(4, left=left, right=right)
print(Solution().kthSmallest(root, 3))
