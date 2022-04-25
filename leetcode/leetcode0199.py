# ****************************************************************分割线****************************************************************
# todo 0199（Binary Tree Right Side View）
# 二叉树的右视图

from collections import deque

from common import TreeNode

class Solution:
    def rightSideView(self, root: TreeNode) -> list:
        result = []
        if root is None:
            return result

        queue = deque([root])
        while queue:
            l = len(queue)
            i = 0
            while i < l:
                if i == 0:
                    result.append(queue[-1].val)
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
print(Solution().rightSideView(root))
