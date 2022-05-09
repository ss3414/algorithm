# ****************************************************************分割线****************************************************************
# todo 0589（N-ary Tree Preorder Traversal）
# N叉树前序遍历（根左右）

from common import Node

class Solution:
    # 递归
    def preorder(self, root: Node) -> list:
        def dfs(node: Node, nodes: list):
            if node is None:
                return
            nodes.append(node.val)
            if node.children:
                for child in node.children:
                    dfs(child, nodes)

        nodes = []
        if root is None:
            return nodes
        dfs(root, nodes)
        return nodes

    # 栈
    def preorder2(self, root: Node) -> list:
        nodes = []
        if root is None:
            return nodes

        stack = [root]
        while len(stack) > 0:
            node = stack.pop()
            nodes.append(node.val)
            if node.children:
                i = len(node.children) - 1
                while i >= 0:
                    stack.append(node.children[i])
                    i -= 1
        return nodes

node2 = Node(2, children=[Node(5), Node(6)])
root = Node(1, children=[node2, Node(3), Node(4)])
print(Solution().preorder(root))
print(Solution().preorder2(root))
