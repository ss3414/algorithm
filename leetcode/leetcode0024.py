# ****************************************************************分割线****************************************************************
# todo 0024（Swap Nodes in Pairs）
# 成对交换链表节点

from common import ListNode
from common import linkedlist2str

class Solution:
    # 池沼算法（不符合要求）
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        count = 1
        cursor = head
        while cursor:
            if count % 2 == 1 and cursor.next:
                temp = cursor.val
                cursor.val = cursor.next.val
                cursor.next.val = temp
            count += 1
            cursor = cursor.next
        return head

    def swapPairs2(self, head: ListNode) -> ListNode:
        empty = cursor = ListNode()
        while head:
            if head.next:
                temp = head
                head = head.next.next
                cursor.next = temp.next
                cursor.next.next = temp
                temp.next = None
                cursor = cursor.next.next
            else:
                cursor.next = head
                head = head.next
        return empty.next

# print(linkedlist2str(Solution().swapPairs(ListNode(1, ListNode(2, ListNode(3, None))))))
print(linkedlist2str(Solution().swapPairs2(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))))))
