# ****************************************************************分割线****************************************************************
# todo 0102（Binary Tree Level Order Traversal）
# 二叉树层序遍历

from collections import deque

from common import TreeNode

class Solution:
    # BFS
    def levelOrder(self, root: TreeNode) -> list:
        result = []
        if root is None:
            return result
        input_queue = deque([root])
        while len(input_queue) > 0:
            breadth = len(input_queue)
            i = 0
            temp = []
            while i < breadth:
                node = input_queue.popleft()
                temp.append(node.val)
                if node.left:
                    input_queue.append(node.left)
                if node.right:
                    input_queue.append(node.right)
                i += 1
            result.append(temp)
        return result

left = TreeNode(2, left=TreeNode(4), right=TreeNode(5))
right = TreeNode(3, left=TreeNode(6), right=TreeNode(7))
root = TreeNode(1, left=left, right=right)
print(Solution().levelOrder(root))
