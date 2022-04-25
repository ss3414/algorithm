# ****************************************************************分割线****************************************************************
# todo 0114（Flatten Binary Tree to Linked List）
# 二叉树展开为链表（前序遍历）

from common import TreeNode

class Solution:
    def flatten(self, root: TreeNode) -> None:
        nodes = []

        def dfs(root: TreeNode):
            if root is None:
                return
            nodes.append(root)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        i = len(nodes) - 2
        while i >= 0:
            nodes[i].right = nodes[i + 1]
            nodes[i].left = None
            i -= 1
        for j in nodes:
            print(j.left)

left = TreeNode(2, left=TreeNode(4), right=TreeNode(5))
right = TreeNode(3, left=TreeNode(6), right=TreeNode(7))
root = TreeNode(1, left=left, right=right)
print(Solution().flatten(root))
