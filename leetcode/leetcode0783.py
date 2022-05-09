# ****************************************************************分割线****************************************************************
# todo 0783（Minimum Distance Between BST Nodes）
# 二叉搜索树节点最短距离

from common import TreeNode

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        data = []

        def dfs(root: TreeNode):
            if not root:
                return
            dfs(root.left)
            data.append(root.val)
            dfs(root.right)

        dfs(root)
        min_val = abs(data[0] - data[1])
        i = 1
        while i < len(data) - 1:
            min_val = min(min_val, abs(data[i] - data[i + 1]))
            i += 1
        return min_val

left = TreeNode(2)
right = TreeNode(6, left=TreeNode(5), right=TreeNode(7))
root = TreeNode(4, left=left, right=right)
print(Solution().minDiffInBST(root))
