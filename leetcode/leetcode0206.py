# ****************************************************************分割线****************************************************************
# todo 0206（Reverse Linked List）
# 反转链表

from common import ListNode
from common import linkedlist2str

class Solution:
    # 迭代
    def reverseList(self, head: ListNode) -> ListNode:
        new = None
        while head:
            temp = head.next
            head.next = new  # 按顺序迭代链表，把每个节点接在new节点后面，再让其成为新的new节点
            new = head
            head = temp
            print("temp:{temp} next:{next} new:{new} head:{head}".format(
                temp=linkedlist2str(temp), next=linkedlist2str(head.next if head else ""), new=linkedlist2str(new), head=linkedlist2str(head)))
        return new

    # 递归
    def reverseList2(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        new = self.reverseList2(head.next)
        head.next.next = head
        head.next = None
        print("new:{new} head:{head}".format(new=linkedlist2str(new), head=linkedlist2str(head)))
        return new

# print(linkedlist2str(Solution().reverseList(ListNode(1, ListNode(2, ListNode(3, None))))))
print(linkedlist2str(Solution().reverseList2(ListNode(1, ListNode(2, ListNode(3, None))))))
