# ****************************************************************分割线****************************************************************
# todo 0141（Linked List Cycle）
# 环形链表

from common import ListNode

# 快慢指针，慢指针1次1步，快指针1次2步，如果链表有环形，则两个指针必定相遇
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            # print("slow:{slow} fast:{fast}".format(slow=slow.val,fast=fast.val))
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

node2 = ListNode(2, None)
node3 = ListNode(3, None)
node2.next = node3
node3.next = node2
head = ListNode(1, node2)
print(Solution().hasCycle(head))
