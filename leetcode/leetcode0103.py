# ****************************************************************分割线****************************************************************
# todo 0103（Binary Tree Zigzag Level Order Traversal）
# 二叉树Z字型顺序
# 先从左到右，再从右到左

from collections import deque

from common import TreeNode

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> list:
        result = []
        if root is None:
            return result

        queue = deque([root])
        count = 0
        while queue:
            level = []
            i = len(queue)
            while i > 0:
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                i -= 1
            print("{c} {l}".format(c=count, l=level))
            if count % 2 == 1:
                level.reverse()
            result.append(level)
            count += 1
        return result

left = TreeNode(2, left=TreeNode(4), right=TreeNode(5))
right = TreeNode(3, left=TreeNode(6), right=TreeNode(7))
root = TreeNode(1, left=left, right=right)
print(Solution().zigzagLevelOrder(root))
