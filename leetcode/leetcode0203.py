# ****************************************************************分割线****************************************************************
# todo 0203（Remove Linked List Elements）
# 删除链表元素

from common import ListNode
from common import linklist2str

def test(head: ListNode, val: int):
    output = ListNode(0, None)  # 开头一个空节点
    output.next = head
    cursor = output
    while cursor.next:
        if cursor.next.val == val:  # 值相等则跳过这个元素
            cursor.next = cursor.next.next
        else:
            cursor = cursor.next
    return output.next

output = test(ListNode(1, ListNode(2, ListNode(3, None))), 2)
print(linklist2str(output))
