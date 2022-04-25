# ****************************************************************分割线****************************************************************
# todo 0143（Reorder List）
# 重排链表

from collections import deque

from common import ListNode

class Solution:
    def reorderList(self, head: ListNode) -> None:
        temp = head
        queue = deque([])
        while temp:
            queue.append(temp)
            temp = temp.next
        if len(queue) < 3:
            return
        while queue:
            left = queue.popleft()
            right = queue.pop()
            left.next = right
            if len(queue) == 0:
                right.next = None
            elif len(queue) == 1:
                top = queue.popleft()
                right.next = top
                top.next = None
            else:
                right.next = queue[0]

        temp = []
        while head:
            temp.append(head.val)
            head = head.next
        print(temp)

Solution().reorderList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))))
Solution().reorderList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, None)))))
