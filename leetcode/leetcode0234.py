# ****************************************************************分割线****************************************************************
# todo 0234（Palindrome Linked List）
# 回文链表

import copy

from common import ListNode

# 反转链表再比较（超时）
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

# 链表前半段入栈与后半段比较（超时）
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

# 链表整体入栈再比较，链表整体入栈再出栈相当于反转链表（慢）
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

# 快慢指针
def test4(head: ListNode):
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

# print(test(ListNode(1,ListNode(2,ListNode(1,None)))))
# print(test(ListNode(1,ListNode(1,None))))

# print(test2(ListNode(1,ListNode(2,ListNode(1,ListNode(1,None))))))
# print(test3(ListNode(1,ListNode(2,ListNode(1,ListNode(1,None))))))

print(test4(ListNode(1, ListNode(2, ListNode(2, ListNode(1, None))))))
