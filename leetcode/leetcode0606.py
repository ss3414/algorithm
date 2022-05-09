# ****************************************************************分割线****************************************************************
# todo 0606（Construct String from Binary Tree）
# 根据二叉树创建字符串

from common import TreeNode

class Solution:
    def tree2str(self, root: TreeNode) -> str:
        def dfs(root: TreeNode):
            if root is None:
                return "()"
            left = dfs(root.left)
            right = dfs(root.right)
            result = "(" + str(root.val) + left + right + ")"
            return result

        result = dfs(root).replace("()()", "").replace(")()", ")")
        return result[1:-1]

# root = TreeNode(1, left=TreeNode(2, left=TreeNode(4)), right=TreeNode(3))
root = TreeNode(1, left=TreeNode(2, right=TreeNode(4)), right=TreeNode(3))
# root = TreeNode(1)
print(Solution().tree2str(root))
