# ****************************************************************分割线****************************************************************
# todo 0024（Swap Nodes in Pairs）
# 成对交换链表节点

from common import ListNode
from common import linkedlist2str

class Solution:
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

print(linkedlist2str(Solution().swapPairs(ListNode(1, ListNode(2, ListNode(3, None))))))
