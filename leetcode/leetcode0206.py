# ****************************************************************分割线****************************************************************
# todo 0206（Reverse Linked List）
# 反转链表

from common import ListNode
from common import linkedlist2str

# 太慢
def test(head: ListNode):
    nodes = []
    cursor = head
    while cursor:
        nodes.append(cursor)
        cursor = cursor.next
    if len(nodes) <= 1:
        return head
    nodes[0].next = None
    i = len(nodes) - 1
    while i > 0:
        nodes[i].next = nodes[i - 1]
        i -= 1
    return nodes[len(nodes) - 1]

# fixme 迭代
def test2(head: ListNode):
    new = None
    while head:
        temp = head.next
        head.next = new  # 按顺序迭代链表，把每个节点接在new节点后面，再让其成为新的new节点
        new = head
        head = temp
        print("temp:{temp} next:{next} new:{new} head:{head}".format(
            temp=linkedlist2str(temp), next=linkedlist2str(head.next if head is not None else ""), new=linkedlist2str(new), head=linkedlist2str(head)))
    return new

# fixme 递归
def test3(head: ListNode):
    if head is None or head.next is None:
        return head
    new = test3(head.next)
    head.next.next = head
    head.next = None
    print("new:{new} head:{head}".format(new=linkedlist2str(new), head=linkedlist2str(head)))
    return new

# output=test(ListNode(1,ListNode(2,ListNode(3,None))))
# output=test(ListNode(1,None))
# output=test2(ListNode(1,ListNode(2,ListNode(3,None))))
output = test3(ListNode(1, ListNode(2, ListNode(3, None))))
print(linkedlist2str(output))
