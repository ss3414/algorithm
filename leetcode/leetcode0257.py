# ****************************************************************分割线****************************************************************
# todo 0257（Binary Tree Paths）
# 二叉树所有路径

from common import TreeNode

class Solution:
    # DFS
    def binaryTreePaths(self, root: TreeNode) -> list:
        def dfs(root: TreeNode, path: str, paths: list):
            if not root.left and not root.right:  # 叶子节点
                path += "{val}".format(val=root.val)
                paths.append(path)
                return
            path += "{val}->".format(val=root.val)
            if root.left:
                dfs(root.left, path, paths)
            if root.right:
                dfs(root.right, path, paths)

        paths = []
        dfs(root, "", paths)
        return paths

left = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
right = TreeNode(6, left=TreeNode(5), right=TreeNode(7))
root = TreeNode(4, left=left, right=right)
print(Solution().binaryTreePaths(root))
