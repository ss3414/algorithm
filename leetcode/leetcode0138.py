# ****************************************************************分割线****************************************************************
# todo 0138（Copy List with Random Pointer）
# 复制带随机指针的链表

class Node:
    def __init__(self, x=0, next=None, random=None):
        self.val = x
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        empty = Node(0)
        node = empty
        data = {}

        temp = head
        while temp:
            next = Node(temp.val)
            data[temp] = next
            node.next = next
            node = node.next
            temp = temp.next

        temp = head
        while temp:
            if temp.random:
                node = data[temp]
                random = data[temp.random]
                node.random = random
            temp = temp.next
        return empty.next

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.next = node2
node2.next = node3
node3.next = node4
node1.random = None
node2.random = node1
node3.random = node4
node4.random = node1
Solution().copyRandomList(node1)
