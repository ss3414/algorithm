# ****************************************************************分割线****************************************************************
# todo 0559（Maximum Depth of N-ary Tree）
# N叉树最大深度

from collections import deque

from common import Node

class Solution:
    # DFS
    def maxDepth(self, root: Node) -> int:
        def test(node: Node, depth: int):
            max_val = depth
            if node is None:
                return max_val
            if node.children:
                for child in node.children:
                    temp = test(child, depth + 1)
                    print("depth:{depth} max:{max}".format(depth=temp, max=max_val))
                    max_val = max(temp, max_val)
            return max_val

        if root is None:
            return 0
        return test(root, 1)

    # BFS（时间复杂度太高）
    def maxDepth2(self, root: Node) -> int:
        depth = 0
        if root is None:
            return depth
        input_queue = deque([root])  # LeetCode中使用双端队列
        while len(input_queue) > 0:
            depth += 1
            breadth = len(input_queue)
            i = 0
            while i < breadth:
                node = input_queue.popleft()
                if node and node.children:
                    for child in node.children:
                        input_queue.append(child)
                i += 1
        return depth

node2 = Node(2, children=[Node(5), Node(6)])
root = Node(1, children=[node2, Node(3), None])
# print(Solution().maxDepth(root))
# print(Solution().maxDepth(None))
print(Solution().maxDepth2(root))