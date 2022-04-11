# ****************************************************************分割线****************************************************************
# todo 0104（Maximum Depth of Binary Tree）
# 二叉树最大深度

from common import TreeNode

class Solution:
    # DFS
    def maxDepth(self, root: TreeNode) -> int:
        def test(root: TreeNode, depth: int):
            if root is None:
                return depth
            return max(test(root.left, depth + 1), test(root.right, depth + 1))

        return test(root, 0)

root = TreeNode(1, left=None, right=TreeNode(2))
print(Solution().maxDepth(root))
