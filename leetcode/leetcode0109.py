# ****************************************************************分割线****************************************************************
# todo 0109（Convert Sorted List to Binary Search Tree）
# 有序链表转换为高度平衡二叉搜索树

from common import ListNode
from common import TreeNode

class Solution:
    # 二分法+递归（太慢）
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def test(nums, left, right):
            if left > right:
                return None

            middle = (left + right) // 2
            root = TreeNode(nums[middle])
            # print(nums[middle])
            root.left = test(nums, left, middle - 1)
            root.right = test(nums, middle + 1, right)
            return root

        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return test(nums, 0, len(nums) - 1)

    # 二分法+快慢指针
    def sortedListToBST2(self, head: ListNode) -> TreeNode:
        if head is None:
            return None
        if head.next is None:
            return TreeNode(head.val)

        slow = fast = head
        last = slow
        while fast.next and fast.next.next:
            last = slow
            slow = slow.next
            fast = fast.next.next
        fast = slow.next  # 后半段
        last.next = None  # 截断链表
        root = TreeNode(slow.val)  # 中间值
        if head != slow:
            root.left = self.sortedListToBST2(head)
        root.right = self.sortedListToBST2(fast)
        return root

# Solution().sortedListToBST(ListNode(1, ListNode(2, ListNode(3, None))))
Solution().sortedListToBST2(ListNode(1, ListNode(2, ListNode(3, None))))
