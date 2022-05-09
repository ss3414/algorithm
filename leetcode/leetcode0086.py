# ****************************************************************分割线****************************************************************
# todo 0086（Partition List）
# 分隔链表

from common import ListNode
from common import linkedlist2str

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head is None or head.next is None:
            return head

        # 找分隔点
        slow = fast = head
        count = 0
        while fast:
            count += 1
            if fast.val >= x:
                break
            fast = fast.next
        if fast is None:  # 没有分隔点
            return head
        for i in range(count - 2):
            slow = slow.next
        flag = False
        if slow == fast:  # 首节点>=x
            flag = True
            slow = ListNode(next=head)
        point = fast
        while fast.next:
            if fast.next.val < x:
                temp = fast.next  # 保存挪动节点
                fast.next = fast.next.next  # fast前进
                temp.next = point  # 挪动指向分隔点
                slow.next = temp  # slow指向挪动
                slow = slow.next
                if flag:
                    head = slow
                    flag = False
                print(linkedlist2str(slow))
                print(linkedlist2str(point))
            else:
                fast = fast.next
        return head

# print(linkedlist2str(Solution().partition(ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(2, None))))),3)))
# print(linkedlist2str(Solution().partition(ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1, None))))),5)))
print(linkedlist2str(Solution().partition(ListNode(1, ListNode(1, ListNode(1, ListNode(1, ListNode(1, None))))), 5)))
