# ****************************************************************分割线****************************************************************
# LeetCode通用工具

# 链表节点
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 链表转字符串
def linklist2str(input: ListNode):
    result = ""
    while input:
        result += "{val}->".format(val=input.val)
        input = input.next
    return result
