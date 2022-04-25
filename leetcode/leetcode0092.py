# ****************************************************************分割线****************************************************************
# todo 0092（Reverse Linked List II）
# 反转链表II

from common import ListNode
from common import linkedlist2str

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        node = ListNode(next=head)  # 虚拟节点
        slow = fast = node
        i = 0
        while i < left - 1:
            slow = slow.next
            i += 1
        cursor = slow.next
        new = None
        while cursor and i < right:
            temp = cursor.next
            cursor.next = new  # 迭代法反转链表
            new = cursor
            cursor = temp
            print(linkedlist2str(new))
            i += 1
        if cursor:  # 末尾还剩
            slow.next.next = cursor
        # print(linkedlist2str(slow))
        slow.next = new
        return node.next

node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
# print(linkedlist2str(Solution().reverseBetween(node,1,4)))
# print(linkedlist2str(Solution().reverseBetween(node,2,4)))
print(linkedlist2str(Solution().reverseBetween(node, 2, 2)))
