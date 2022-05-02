# ****************************************************************分割线****************************************************************
# todo 0328（Odd Even Linked List）
# 奇偶链表

from common import ListNode
from common import linkedlist2str

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        l1 = l2 = ListNode()
        r1 = r2 = ListNode()
        odd = head
        even = head.next
        while odd or even:
            if odd:
                l2.next = ListNode(odd.val)
                l2 = l2.next
                if odd.next:
                    odd = odd.next.next
                else:
                    odd = None
            if even:
                r2.next = ListNode(even.val)
                r2 = r2.next
                if even.next:
                    even = even.next.next
                else:
                    even = None
        # print(linkedlist2str(l1.next))
        # print(linkedlist2str(r1.next))
        l2.next = r1.next
        return l1.next

print(linkedlist2str(Solution().oddEvenList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, None)))))))
print(linkedlist2str(Solution().oddEvenList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))))))
