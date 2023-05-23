# ****************************************************************分割线****************************************************************
# todo 0099（Recover Binary Search Tree）
# 恢复二叉搜索树

from common import TreeNode

class Solution:
    # DFS
    def recoverTree(self, root: TreeNode) -> None:
        nodes = []

        def dfs(root: TreeNode):
            if root is None:
                return
            if root.left:
                dfs(root.left)
            nodes.append(root)
            if root.right:
                dfs(root.right)

        dfs(root)
        order = [i.val for i in nodes]
        order.sort()
        # print(order)
        i = 0
        while i < len(nodes):
            nodes[i].val = order[i]
            i += 1

root = TreeNode(1, left=TreeNode(3, right=TreeNode(2)))
print(Solution().recoverTree(root))
