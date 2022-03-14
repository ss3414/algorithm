# ****************************************************************分割线****************************************************************
# todo 0234（Palindrome Linked List）
# 回文链表

import copy

from common import ListNode
from common import linklist2str

# 反转链表再比较，时间复杂度太高
def test(head: ListNode):
    cursor = copy.deepcopy(head)  # 深拷贝
    reverse = None
    while cursor:
        temp = cursor.next
        cursor.next = reverse
        reverse = cursor
        cursor = temp
    while head:
        print("head:{head} reverse:{reverse}".format(head=head.val, reverse=reverse.val))
        if head.val != reverse.val:
            return False
        head = head.next
        reverse = reverse.next
    return True

# 链表前半段入栈与后半段比较，时间复杂度太高
def test2(head: ListNode):
    cursor = copy.deepcopy(head)
    length = 0
    while cursor:
        length += 1
        cursor = cursor.next
    middle = length // 2
    remain = length % 2
    stack = []
    i = 1
    while i <= length:
        if i <= middle:
            stack.append(head.val)
        elif i >= (middle + remain + 1):
            if head.val != stack.pop():
                return False
        head = head.next
        i += 1
    return True

# 链表整体入栈再比较，链表整体入栈再出栈相当于反转链表（能通过AC，但时间复杂度较高）
def test3(head: ListNode):
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

# fixme 快慢指针
def test4(head: ListNode):
    return True

# print(test(ListNode(1,ListNode(2,ListNode(1,None)))))
# print(test(ListNode(1,ListNode(1,None))))

# print(test2(ListNode(1,ListNode(2,ListNode(1,ListNode(1,None))))))
print(test3(ListNode(1, ListNode(2, ListNode(1, ListNode(1, None))))))

# class Solution:
# def isPalindrome(self, head: Optional[ListNode]) -> bool:
