# ****************************************************************分割线****************************************************************
# todo 0117（Populating Next Right Pointers in Each Node II）
# 填充每个节点下一个右指针II

class Node:
    def __init__(self, val: int = 0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    # 递归
    def connect(self, root):
        if root is None:
            return None
        node = root.next
        while node:
            if node.left:
                node = node.left
                break
            if node.right:
                node = node.right
                break
            node = node.next
        if root.right:
            root.right.next = node
        if root.left:
            root.left.next = root.right if root.right else node
        self.connect(root.right)
        self.connect(root.left)
        return root

left = Node(2, left=Node(4), right=Node(5))
right = Node(3, left=Node(6), right=Node(7))
root = Node(1, left=left, right=right)
Solution().connect(root)
