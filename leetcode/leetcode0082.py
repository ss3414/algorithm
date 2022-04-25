# ****************************************************************分割线****************************************************************
# todo 0082（Remove Duplicates from Sorted List II）
# 删除有序链表中的重复元素
# 有重复的全部删掉

from common import ListNode
from common import linkedlist2str

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        result = ListNode()
        cursor = result
        count = 0
        while head:
            if head.next and head.val == head.next.val:
                count += 1
            if head.next is None or head.val != head.next.val:
                if count == 0:
                    cursor.next = ListNode(val=head.val)
                    cursor = cursor.next
                count = 0
            head = head.next
        return result.next

print(linkedlist2str(Solution().deleteDuplicates(ListNode(1, ListNode(2, ListNode(2, ListNode(3, ListNode(3, None))))))))
