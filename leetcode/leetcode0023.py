# ****************************************************************分割线****************************************************************
# todo 0023（Merge k Sorted Lists）
# 合并K个有序链表

from common import ListNode
from common import linkedlist2str

class Solution:
    def sort(self, left: ListNode, right: ListNode) -> ListNode:
        empty = cursor = ListNode()
        cursor = empty
        while left and right:
            if left.val <= right.val:
                cursor.next = left
                cursor = cursor.next
                left = left.next
            else:
                cursor.next = right
                cursor = cursor.next
                right = right.next
        cursor.next = left or right
        return empty.next

    def merge(self, lists: list) -> ListNode:
        length = len(lists)
        if length <= 1:
            return lists[0]

        middle = length // 2
        return self.sort(self.merge(lists[0:middle]), self.merge(lists[middle:]))

    def mergeKLists(self, lists: list) -> ListNode:
        length = len(lists)
        if length == 0:
            return None

        return self.merge(lists)

test = [ListNode(1, ListNode(2, ListNode(3, None))),
        ListNode(4, ListNode(5, ListNode(6, None))),
        ListNode(7, ListNode(8, ListNode(9, None)))]
# print(linkedlist2str(Solution().mergeKLists(test)))
# print(linkedlist2str(Solution().mergeKLists([])))
print(linkedlist2str(Solution().mergeKLists([[]])))
