# ****************************************************************分割线****************************************************************
# todo 0083（Remove Duplicates from Sorted List）
# 删除有序链表中的重复元素

from common import ListNode
from common import linkedlist2str

# 时间复杂度太高
def test(head: ListNode):
    if head is None:
        return None

    # temps=[ListNode(head.val,None)]  # LeetCode环境不能调用ListNode()新建节点
    temps = [head]
    while head.next is not None:
        if head.val != head.next.val:
            # output.next=ListNode(head.next.val,None)
            temps.append(head.next)
        head = head.next
    temps[len(temps) - 1].next = None  # 把最后一个元素的next置空
    i = 0
    while i < len(temps) - 1:
        temps[i].next = temps[i + 1]
        i += 1
    return temps[0]

# 链表从逻辑上是一个节点指向一个节点，从代码上是一个节点嵌套一个节点
def test2(head):
    cursor = head
    while cursor:  # 不能为None
        # 如果下一个节点存在且值相同，则cursor指向下下个节点（相当于抛弃重复节点）
        while cursor.next and cursor.next.val == cursor.val:
            cursor.next = cursor.next.next
        cursor = cursor.next
    return head

# output=test(ListNode(1,ListNode(1,ListNode(2,ListNode(3,ListNode(3,None))))))
# print(linkedlist2str(output))

# print(test2(None))
output = test2(ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3, None))))))
print(linkedlist2str(output))
