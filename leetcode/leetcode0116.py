# ****************************************************************分割线****************************************************************
# todo 0116（Populating Next Right Pointers in Each Node）
# 填充每个节点下一个右指针

from collections import deque

class Node:
    def __init__(self, val: int = 0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root):
        nodes = []
        queue = deque([root])
        while queue:
            length = len(queue)
            i = 0
            while i < length:
                node = queue.popleft()
                if node:
                    if i < length - 1:
                        node.next = queue[0]
                    nodes.append(node)
                    queue.append(node.left)
                    queue.append(node.right)
                i += 1
        for i in nodes:
            print("{v} {n}".format(v=i.val, n=i.next))
        return root

left = Node(2, left=Node(4), right=Node(5))
right = Node(3, left=Node(6), right=Node(7))
root = Node(1, left=left, right=right)
Solution().connect(root)
