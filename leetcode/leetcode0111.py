# ****************************************************************分割线****************************************************************
# todo 0111（Minimum Depth of Binary Tree）
# 二叉树最小深度

from common import TreeNode

class Solution:
    # DFS
    def minDepth(self, root: TreeNode) -> int:
        def test(root: TreeNode, depth: int):
            if root is None:  # 根节点为空，深度为0
                return depth

            if root.left and root.right:  # 左右子树最小深度
                return min(test(root.left, depth + 1), test(root.right, depth + 1))
            if root.left and root.right is None:  # 左子树
                return test(root.left, depth + 1)
            if root.left is None and root.right:  # 右子树
                return test(root.right, depth + 1)
            if not root.left and not root.right:  # 叶子节点，返回深度
                return depth + 1

        return test(root, 0)

# root=TreeNode(1,right=TreeNode(2,right=TreeNode(3,right=TreeNode(4,right=TreeNode(5)))))
root = TreeNode(1)
print(Solution().minDepth(root))
