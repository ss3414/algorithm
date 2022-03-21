# ****************************************************************分割线****************************************************************
# LeetCode通用工具

# 链表节点
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

# 二叉树节点
class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# N叉树节点
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

# 链表转字符串
def linkedlist2str(input: ListNode):
    result = ""
    while input:
        result += "{val}->".format(val=input.val)
        input = input.next
    return result

# 二叉树转数组
def tree2array(root: TreeNode):
    def test(root: TreeNode, nodes: list):
        if root is None:
            return
        if root.left is None and root.right is None:
            return
        nodes.append(root.left.val if root.left else None)
        nodes.append(root.right.val if root.right else None)
        test(root.left, nodes)
        test(root.right, nodes)

    nodes = []
    nodes.append(root.val if root else None)
    test(root, nodes)
    return nodes
