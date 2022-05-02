# ****************************************************************分割线****************************************************************
# todo 0148（Sort List）
# 链表排序

from common import ListNode
from common import linkedlist2str

class Solution:
    def test(self, left: ListNode, right: ListNode) -> ListNode:
        empty = cursor = ListNode()
        cursor = empty
        while left and right:
            if left.val <= right.val:
                cursor.next = left
                cursor = cursor.next
                left = left.next
            else:
                cursor.next = right
                cursor = cursor.next
                right = right.next
        cursor.next = left or right
        return empty.next

    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None
        return self.test(self.sortList(head), self.sortList(slow))

print(linkedlist2str(Solution().sortList(ListNode(4, ListNode(3, ListNode(2, ListNode(1, None)))))))
