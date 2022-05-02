# ****************************************************************分割线****************************************************************
# todo 0021（Merge Two Sorted Lists）
# 合并两个有序链表

from common import ListNode
from common import linkedlist2str

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        empty = cursor = ListNode()  # empty节点，指向最终返回的有序链表
        # 同时遍历两个有序链表，哪个元素小插入cursor中
        while list1 and list2:
            if list1.val < list2.val:
                cursor.next = list1
                list1 = list1.next  # list1前进（移除表头，下一个元素成为新表头）
            else:
                cursor.next = list2
                list2 = list2.next
            cursor = cursor.next
        # 如果list1/list2长度不一致，遍历剩下的链表插入cursor（原链表有序，剩下的一定大于cursor）
        cursor.next = list1 or list2
        return empty.next

list1 = ListNode(1, ListNode(2, ListNode(4, None)))
list2 = ListNode(1, ListNode(3, ListNode(4, None)))
# print(linkedlist2str(Solution().mergeTwoLists(list1,list2)))
print(linkedlist2str(Solution().mergeTwoLists(None, ListNode(1, None))))
