# ****************************************************************分割线****************************************************************
# todo 0203（Remove Linked List Elements）
# 删除链表元素

from common import ListNode
from common import linkedlist2str

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        empty = cursor = ListNode()
        empty.next = head
        while cursor.next:
            if cursor.next.val == val:  # 值相等则跳过这个元素
                cursor.next = cursor.next.next
            else:
                cursor = cursor.next
        return empty.next

print(linkedlist2str(Solution().removeElements(ListNode(1, ListNode(2, ListNode(3, None))), 2)))
