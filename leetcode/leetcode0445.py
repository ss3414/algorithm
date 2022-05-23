# ****************************************************************分割线****************************************************************
# todo 0445（Add Two Numbers II）
# 两数相加II

from common import ListNode
from common import linkedlist2str

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        empty1 = ListNode(val=0, next=l1)
        l1 = empty1
        empty2 = ListNode(val=0, next=l2)
        l2 = empty2
        result = None

        stack1, stack2 = [], []
        while l1:
            stack1.append(l1)
            l1 = l1.next
        while l2:
            stack2.append(l2)
            l2 = l2.next
        temp = 0
        while stack1 or stack2:
            if stack1 and not stack2:
                sum = temp + stack1[-1].val
                temp = sum // 10
                stack1[-1].val = sum % 10
                result = stack1[0]
            elif stack2 and not stack1:
                sum = temp + stack2[-1].val
                temp = sum // 10
                stack2[-1].val = sum % 10
                result = stack2[0]
            else:
                sum = temp + stack1[-1].val + stack2[-1].val
                temp = sum // 10
                stack1[-1].val = sum % 10
                stack2[-1].val = sum % 10
            if len(stack1) == 1 and len(stack2) == 1:
                result = stack1[0]
            if stack1:
                stack1.pop()
            if stack2:
                stack2.pop()
        if result.val != 0:
            return result
        else:
            return result.next

# list1 = ListNode(5, ListNode(6, ListNode(7, None)))
# list2 = ListNode(6, ListNode(7, ListNode(8, None)))
list1 = ListNode(1, None)
list2 = ListNode(9, ListNode(9, None))
print(linkedlist2str(Solution().addTwoNumbers(list1, list2)))
