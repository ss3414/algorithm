# ****************************************************************分割线****************************************************************
# todo 0671（Second Minimum Node In a Binary Tree）
# 二叉树第二小节点

from common import TreeNode

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        data = {}

        def dfs(root: TreeNode):
            if not root:
                return
            data[root.val] = root.val
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        vals = sorted(data.values())
        if len(vals) > 1:
            return vals[1]
        else:
            return -1

left = TreeNode(2, right=TreeNode(4))
right = TreeNode(3, left=TreeNode(2, right=TreeNode(4)))
root = TreeNode(1, left=left, right=right)
print(Solution().findSecondMinimumValue(root))
