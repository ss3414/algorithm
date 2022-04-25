# ****************************************************************分割线****************************************************************
# todo 0700（Search in a Binary Search Tree）
# 使用二叉搜索树

from common import TreeNode

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root and root.val > val:
            return self.searchBST(root.left, val)
        if root and root.val < val:
            return self.searchBST(root.right, val)
        return root

left = TreeNode(2)
right = TreeNode(6, left=TreeNode(5), right=TreeNode(7))
root = TreeNode(4, left=left, right=right)
print(Solution().searchBST(root, 1))
