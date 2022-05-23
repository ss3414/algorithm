# ****************************************************************分割线****************************************************************
# todo 0002（Add Two Numbers）
# 两数相加

from common import ListNode
from common import linkedlist2str

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def test(node: ListNode):
            result = ""
            while node:
                result = str(node.val) + result
                node = node.next
            return int(result)

        sum = test(l1) + test(l2)
        number = str(sum)
        head = ListNode()
        node = head
        i = len(number) - 1
        while i >= 0:
            node.val = int(number[i])
            if i != 0:
                node.next = ListNode()
                node = node.next
            i -= 1
        return head

    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        node1 = l1
        node2 = l2
        temp = 0
        while l1 or l2:
            if l1 and not l2:
                sum = temp + l1.val
                temp = sum // 10
                l1.val = sum % 10
                if temp != 0 and not l1.next:
                    l1.next = ListNode(temp)
                    return node1
                elif temp == 0:
                    return node1
            elif l2 and not l1:
                sum = temp + l2.val
                temp = sum // 10
                l2.val = sum % 10
                if temp != 0 and not l2.next:
                    l2.next = ListNode(temp)
                    return node2
                elif temp == 0:
                    return node2
            else:
                sum = temp + l1.val + l2.val
                temp = sum // 10
                l1.val = sum % 10
                l2.val = sum % 10
                if not l1.next and not l2.next:
                    if temp == 0:
                        return node1
                    else:
                        l1.next = ListNode(temp)
                        return node1
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

# list1 = ListNode(2, ListNode(4, ListNode(3, None)))
# list2 = ListNode(5, ListNode(6, ListNode(4, None)))
# print(linkedlist2str(Solution().addTwoNumbers(list1, list2)))
list1 = ListNode(9, None)
list2 = ListNode(9, ListNode(9, ListNode(9, None)))
print(linkedlist2str(Solution().addTwoNumbers2(list1, list2)))
