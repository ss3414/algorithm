# ****************************************************************分割线****************************************************************
# todo 0144（Binary Tree Preorder Traversal）
# 二叉树前序遍历

from common import TreeNode

class Solution:
    # 递归
    def preorderTraversal(self, root: TreeNode) -> list:
        def test(root: TreeNode, nodes: list):
            if root is None:
                return
            nodes.append(root.val)
            test(root.left, nodes)
            test(root.right, nodes)

        nodes = []
        test(root, nodes)
        return nodes

    # 栈
    def preorderTraversal2(self, root: TreeNode) -> list:
        if root is None:
            return []
        # 前序遍历根左右，根入栈出栈，右入栈再左入栈
        stack = [root]
        nodes = []
        while len(stack) > 0:
            node = stack.pop()
            nodes.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return nodes

    # 迭代（preorderTraversal2的简化版）
    def preorderTraversal3(self, root: TreeNode) -> list:
        stack = [root]
        nodes = []
        while stack:
            node = stack.pop()
            if node:
                nodes.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return nodes

left = TreeNode(2, left=TreeNode(4), right=TreeNode(5))
right = TreeNode(3, left=TreeNode(6), right=TreeNode(7))
root = TreeNode(1, left=left, right=right)
# print(Solution().preorderTraversal(root))
# print(Solution().preorderTraversal2(root))
print(Solution().preorderTraversal3(root))
