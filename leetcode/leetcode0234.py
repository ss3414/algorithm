# ****************************************************************分割线****************************************************************
# todo 0234（Palindrome Linked List）
# 回文链表

import copy

from common import ListNode

class Solution:
    # 链表整体入栈再比较，链表整体入栈再出栈相当于反转链表（太慢）
    def isPalindrome(self, head: ListNode) -> bool:
        cursor = copy.deepcopy(head)
        stack = []
        while cursor:
            stack.append(cursor.val)
            cursor = cursor.next
        while head:
            if head.val != stack.pop():
                return False
            head = head.next
        return True

    # 快慢指针
    def isPalindrome2(self, head: ListNode) -> bool:
        slow = fast = head
        stack = [head.val]
        # 快指针走完时，慢指针走到中间，再用栈储存前半段比较后半段
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            stack.append(slow.val)
        if fast.next is None:  # 如果链表为偶数，中间元素出栈（快慢指针是从第一个元素开始前进）
            stack.pop()
        while slow.next:
            slow = slow.next
            temp = stack.pop()
            print("temp:{temp} slow:{slow}".format(temp=temp, slow=slow.val))
            if temp != slow.val:
                return False
        return True

print(Solution().isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1, None))))))
print(Solution().isPalindrome2(ListNode(1, ListNode(2, ListNode(2, ListNode(1, None))))))
