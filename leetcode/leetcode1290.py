# ****************************************************************分割线****************************************************************
# todo 1290（Convert Binary Number in a Linked List to Integer）
# 二进制链表转整数

from common import ListNode

class Solution:
    # 栈
    def getDecimalValue(self, head: ListNode) -> int:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        count = 0
        result = 0
        while len(stack) > 0:
            temp = stack.pop()
            result += temp * (2 ** count)
            count += 1
        return result

    # 位运算
    def getDecimalValue2(self, head: ListNode) -> int:
        if head is None:
            return 0
        result = 0
        while head:
            print("result:{result} head:{head}".format(result=result << 1, head=head.val))
            # 二进制数101可以看成1*2^2+0*2^1+1*2^0，node1被左移2次，相当于1*2^2，node2左移1次，node3左移0次
            result = (result << 1) + head.val
            head = head.next
        return result

print(Solution().getDecimalValue(ListNode(1, ListNode(0, ListNode(1, None)))))
print(Solution().getDecimalValue2(ListNode(1, ListNode(0, ListNode(1, None)))))
