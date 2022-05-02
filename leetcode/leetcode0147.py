# ****************************************************************分割线****************************************************************
# todo 0147（Insertion Sort List）
# 链表插入排序

from common import ListNode
from common import linkedlist2str

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        empty = cursor = ListNode()
        while head:
            temp = head.next
            cursor = empty
            while cursor.next and cursor.next.val <= head.val:
                cursor = cursor.next
            head.next = cursor.next
            cursor.next = head
            head = temp
        return empty.next

head = ListNode(3, ListNode(1, ListNode(2, ListNode(4, None))))
print(linkedlist2str(Solution().insertionSortList(head)))
