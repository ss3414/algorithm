# ****************************************************************分割线****************************************************************
# todo 0653（Two Sum IV - Input is a BST）
# 在二叉搜索树中求两数和

from collections import deque

from common import TreeNode

# 两数之和优先使用HashTable/HashSet来做
class Solution:
    # DFS
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def dfs(root: TreeNode, k: int, data: set):
            if root is None:
                return False
            if (k - root.val) in data:
                return True
            data.add(root.val)
            return dfs(root.left, k, data) or dfs(root.right, k, data)

        return dfs(root, k, set())

    # BFS
    def findTarget2(self, root: TreeNode, k: int) -> bool:
        if root is None:
            return False
        data = set()
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if (k - node.val) in data:
                return True
            data.add(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False

left = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
right = TreeNode(6, left=TreeNode(4), right=TreeNode(7))
root = TreeNode(4, left=left, right=right)
# print(Solution().findTarget(root,9))
print(Solution().findTarget2(root, 9))
