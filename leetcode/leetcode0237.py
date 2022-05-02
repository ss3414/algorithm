# ****************************************************************分割线****************************************************************
# todo 0237（Delete Node in a Linked List）
# 删除链表中的节点
# 不给头结点，只给删除节点

from common import ListNode

class Solution:
    # 把删除节点后所有节点的值向前挪一位，再断开最后一个节点的连接
    def deleteNode(self, node):
        while node:
            node.val = node.next.val
            if node.next.next is None:
                node.next = None
            node = node.next

Solution().deleteNode(ListNode(1, ListNode(2, ListNode(3, None))))
