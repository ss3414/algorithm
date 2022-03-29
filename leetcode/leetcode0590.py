# ****************************************************************分割线****************************************************************
# todo 0590（N-ary Tree Postorder Traversal）
# N叉树后序遍历（左右根）

from common import Node

class Solution:
    # 递归
    def postorder(self, root: Node) -> list:
        def test(node: Node, nodes: list):
            if node is None:
                return
            if node.children:
                for child in node.children:
                    test(child, nodes)
            nodes.append(node.val)
            return

        nodes = []
        if root is None:
            return nodes
        test(root, nodes)
        return nodes

    # 栈（后序遍历用栈最后需要反转）
    def postorder2(self, root: Node) -> list:
        nodes = []
        if root is None:
            return nodes

        stack = [root]
        while len(stack) > 0:
            node = stack.pop()
            nodes.append(node.val)
            if node.children:
                i = 0
                while i < len(node.children):
                    stack.append(node.children[i])
                    i += 1
        nodes.reverse()
        return nodes

node2 = Node(2, children=[Node(5), Node(6)])
node3 = Node(3, children=[Node(7), Node(8)])
root = Node(1, children=[node2, node3, Node(4)])
# print(Solution().postorder(root))
print(Solution().postorder2(root))
