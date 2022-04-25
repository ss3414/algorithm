# ****************************************************************分割线****************************************************************
# todo 0061（Rotate List）
# 旋转链表

from common import ListNode
from common import linkedlist2str

class Solution:
    # 超时
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.next is None or k == 0:
            return head
        i = 0
        while i < k:
            cursor = head
            other = cursor.val
            while cursor:
                if cursor.next:
                    temp = cursor.next.val
                    cursor.next.val = other
                    other = temp
                if cursor.next is None:
                    head.val = other
                cursor = cursor.next
            i += 1
        return head

    # 快慢指针
    def rotateRight2(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.next is None:
            return head

        slow = fast = head
        count = 0
        while k > 0:
            count += 1
            k -= 1
            if fast.next:
                fast = fast.next
            else:
                # fast第一次到达末尾，k对count取余获取最终步数
                k %= count
                print("{k} {c}".format(k=k, c=count))
                fast = head
        if fast == head:  # 移动链表长度的倍数等于原地不动
            return head

        while fast.next:
            fast = fast.next
            slow = slow.next
        temp = slow.next
        slow.next = None
        fast.next = head
        return temp

# print(linkedlist2str(Solution().rotateRight(ListNode(1,ListNode(2,ListNode(3,None))),2)))
# print(linkedlist2str(Solution().rotateRight2(ListNode(1, ListNode(2, ListNode(3, None))), 2)))
print(linkedlist2str(Solution().rotateRight2(ListNode(1, ListNode(2, ListNode(3, None))), 7)))
