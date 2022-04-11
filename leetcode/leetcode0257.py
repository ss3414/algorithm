# ****************************************************************分割线****************************************************************
# todo 0257（Binary Tree Paths）
# 二叉树所有路径

from common import TreeNode

class Solution:
    # DFS
    def binaryTreePaths(self, root: TreeNode) -> list:
        def test(root: TreeNode, path: str, paths: list):
            if root.left is None and root.right is None:  # 叶子节点
                path += "{val}".format(val=root.val)
                paths.append(path)
                return
            path += "{val}->".format(val=root.val)
            if root.left:
                test(root.left, path, paths)
            if root.right:
                test(root.right, path, paths)

        paths = []
        test(root, "", paths)
        return paths

left = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
right = TreeNode(6, left=TreeNode(5), right=TreeNode(7))
root = TreeNode(4, left=left, right=right)
print(Solution().binaryTreePaths(root))
