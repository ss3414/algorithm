# ****************************************************************分割线****************************************************************
# todo 0429（N-ary Tree Level Order Traversal）
# N叉树层序遍历

from collections import deque

from common import Node

class Solution:
    # BFS
    def levelOrder(self, root: Node) -> list:
        result = []
        if root is None:
            return result
        queue = deque([root])
        while len(queue) > 0:
            breadth = len(queue)  # 用宽度控制每层出队数量
            i = 0
            temp = []
            while i < breadth:
                node = queue.popleft()
                temp.append(node.val)
                if node and node.children:
                    for child in node.children:
                        queue.append(child)
                i += 1
            result.append(temp)
        return result

node2 = Node(2, children=[Node(5), Node(6)])
root = Node(1, children=[node2, Node(3), Node(4)])
print(Solution().levelOrder(root))
