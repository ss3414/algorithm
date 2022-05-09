# ****************************************************************分割线****************************************************************
# todo 0513（Find Bottom Left Tree Value）
# 寻找二叉树左下角

from collections import deque

from common import TreeNode

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        result = root.val
        queue = deque([root])
        while queue:
            l = len(queue)
            i = 0
            while i < l:
                if i == 0:
                    result = queue[0].val
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                i += 1
        return result

left = TreeNode(2, left=TreeNode(4), right=TreeNode(5))
right = TreeNode(3, left=TreeNode(6), right=TreeNode(7))
root = TreeNode(1, left=left, right=right)
print(Solution().findBottomLeftValue(root))
