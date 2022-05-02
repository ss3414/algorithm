# ****************************************************************分割线****************************************************************
# todo 0083（Remove Duplicates from Sorted List）
# 删除有序链表中的重复元素

from common import ListNode
from common import linkedlist2str

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cursor = head
        while cursor:
            # 如果下一个节点存在且值相同，则cursor指向下下个节点（相当于抛弃重复节点）
            while cursor.next and cursor.next.val == cursor.val:
                cursor.next = cursor.next.next
            cursor = cursor.next
        return head

print(linkedlist2str(Solution().deleteDuplicates(ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3, None))))))))
