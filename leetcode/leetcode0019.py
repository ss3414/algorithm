# ****************************************************************分割线****************************************************************
# todo 0019（Remove Nth Node From End of List）
# 删除链表倒数第N个节点

from common import ListNode
from common import linkedlist2str

class Solution:
    # 遍历两次
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cursor = head
        count = 0
        while cursor:
            count += 1
            cursor = cursor.next
        k = count - n
        if k == 0:
            return head.next
        cursor = head
        while cursor:
            k -= 1
            if k == 0:
                cursor.next = cursor.next.next
            cursor = cursor.next
        return head

    # 快慢指针
    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        slow = fast = head
        while n > 0:
            fast = fast.next
            n -= 1
        if fast is None:
            return head.next
        while fast:
            fast = fast.next
            if fast:
                slow = slow.next
            else:
                slow.next = slow.next.next
        return head

# print(linkedlist2str(Solution().removeNthFromEnd(ListNode(1,ListNode(2,ListNode(3,None))),2)))
# print(linkedlist2str(Solution().removeNthFromEnd(ListNode(1,ListNode(2,ListNode(3,None))),3)))
print(linkedlist2str(Solution().removeNthFromEnd2(ListNode(1, ListNode(2, ListNode(3, None))), 2)))
