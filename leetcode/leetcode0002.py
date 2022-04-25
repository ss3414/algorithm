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

list1 = ListNode(2, ListNode(4, ListNode(3, None)))
list2 = ListNode(5, ListNode(6, ListNode(4, None)))
print(linkedlist2str(Solution().addTwoNumbers(list1, list2)))
