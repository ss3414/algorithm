# ****************************************************************分割线****************************************************************
# todo 0142（Linked List Cycle II）
# # 环形链表II

from common import ListNode

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if fast is None or fast.next is None:
            return None
        # 环形链表的快慢指针一定在环头或环尾遭遇
        slow = head
        while slow != fast:
            # print("slow:{slow} fast:{fast}".format(slow=slow.val,fast=fast.val))
            slow = slow.next
            fast = fast.next
        return fast

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2
print(Solution().detectCycle(node1).val)
