# ****************************************************************分割线****************************************************************
# todo 0222（Count Complete Tree Nodes）
# 求完全二叉树节点数

from common import TreeNode

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        return (1 + self.countNodes(root.left) + self.countNodes(root.right)) if root else 0

left = TreeNode(2, left=TreeNode(4), right=TreeNode(5))
right = TreeNode(3, left=TreeNode(6))
root = TreeNode(1, left=left, right=right)
print(Solution().countNodes(root))
