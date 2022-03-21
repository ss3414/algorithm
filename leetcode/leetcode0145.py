# ****************************************************************分割线****************************************************************
# todo 0145（Binary Tree Postorder Traversal）
# 二叉树后序遍历

from common import TreeNode

class Solution:
    # 递归（官方不推荐）
    def postorderTraversal(self, root: TreeNode) -> list:
        def test(root: TreeNode, nodes: list):
            if root is None:
                return
            test(root.left, nodes)
            test(root.right, nodes)
            nodes.append(root.val)

        nodes = []
        test(root, nodes)
        return nodes

    # 迭代
    def postorderTraversal2(self, root: TreeNode) -> list:
        # 后序遍历左右根，根入栈出栈，左入栈再右入栈，出栈顺序根右左，反转后左右根
        stack = [root]
        nodes = []
        while stack:
            node = stack.pop()
            if node:
                nodes.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        nodes.reverse()
        return nodes

left = TreeNode(2, left=TreeNode(4), right=TreeNode(5))
right = TreeNode(3, left=TreeNode(6), right=TreeNode(7))
root = TreeNode(1, left=left, right=right)
# print(Solution().postorderTraversal(root))
print(Solution().postorderTraversal2(root))
