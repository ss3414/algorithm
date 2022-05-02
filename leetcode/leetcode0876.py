# ****************************************************************分割线****************************************************************
# todo 0876（Middle of the Linked List）
# 返回链表中间元素

from common import ListNode

class Solution:
    # 快慢指针
    def middleNode(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        if fast.next is None:
            return slow
        else:
            return slow.next

print(Solution().middleNode(ListNode(1, ListNode(2, None))).val)
