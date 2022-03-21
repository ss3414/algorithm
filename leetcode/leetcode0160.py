# ****************************************************************分割线****************************************************************
# todo 0160（Intersection of Two Linked Lists）
# 相交链表

from common import ListNode
from common import linkedlist2str

# 获取链表长度
def test(head: ListNode):
    length = 0
    while head is not None:
        length += 1
        head = head.next
    return length

# 两个链表一定是末尾段相交，如果两个链表不一样长，截成一样长再比较
def test2(headA: ListNode, headB: ListNode):
    if headA is None or headB is None:
        return None
    lengthA = test(headA)
    lengthB = test(headB)
    if lengthA > lengthB:
        i = 0
        while i < lengthA - lengthB:
            headA = headA.next
            i += 1
    else:
        i = 0
        while i < lengthB - lengthA:
            headB = headB.next
            i += 1
    # 这里用（headA is not headB）无法判断Python对象是否相等，LeetCode环境可能重写了__eq__方法
    while headA is not None and headB is not None and headA is not headB:
        # print("headA:{headA}".format(headA=linkedlist2str(headA)))
        # print("headB:{headB}".format(headB=linkedlist2str(headB)))
        headA = headA.next
        headB = headB.next
    if headA is not None and headB is not None:
        return headA
    else:
        return None

# 环形思路
def test3(headA: ListNode, headB: ListNode):
    if headA is None or headB is None:
        return None
    tempA = headA
    tempB = headB
    while tempA is not tempB:
        print("tempA:{tempA}".format(tempA=linkedlist2str(tempA)))
        print("tempB:{tempB}".format(tempB=linkedlist2str(tempB)))
        # 当headA遍历完之后再遍历headB，相当于headA+headB与headB+headA比较
        # 一定是在相等处或末尾相等
        tempA = headB if tempA is None else tempA.next  # 三目运算符
        tempB = headA if tempB is None else tempB.next
    return tempA

# headA=ListNode(1,ListNode(2,ListNode(3,ListNode(4,None))))
# headB=ListNode(1,ListNode(3,ListNode(4,None)))
# output=test2(headA,headB)
# print(linkedlist2str(output))

# headA+headB：1,2,3,4,1,3,4
# headB+headA：1,3,4,1,2,3,4
headA = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
headB = ListNode(1, ListNode(3, ListNode(4, None)))
output = test3(headA, headB)
print(linkedlist2str(output))
