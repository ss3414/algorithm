# ****************************************************************分割线****************************************************************
# todo 0098（Validate Binary Search Tree）
# 验证二叉搜索树

from collections import deque

from common import TreeNode

class Solution:
    # 池沼算法（BFS）
    # BST不仅要求左小右大，还要求中序遍历升序排列
    def isValidBST(self, root: TreeNode) -> bool:
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                if (node.left and node.left.val >= node.val) or (node.right and node.right.val <= node.val):
                    return False
                queue.append(node.left)
                queue.append(node.right)
        return True

    # DFS
    def isValidBST2(self, root: TreeNode) -> bool:
        result = []

        def dfs(root: TreeNode):
            if root is None:
                return
            if root.left:
                dfs(root.left)
            result.append(root.val)
            if root.right:
                dfs(root.right)

        dfs(root)
        i = 0
        while i < len(result) - 1:
            if result[i] >= result[i + 1]:
                return False
            i += 1
        return True

left = TreeNode(4)
right = TreeNode(6, left=TreeNode(3), right=TreeNode(7))
root = TreeNode(5, left=left, right=right)
# print(Solution().isValidBST(root))
print(Solution().isValidBST2(root))
