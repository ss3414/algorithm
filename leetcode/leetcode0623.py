# ****************************************************************分割线****************************************************************
# todo 0623（Add One Row to Tree）
# 给二叉树添加一行

from common import TreeNode
from common import tree2array

class Solution:
    # 池沼算法
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        def left(root: TreeNode, depth: int):
            if root.left:
                if depth == 0:  # 中间插入
                    temp = root.left
                    root.left = TreeNode(val)
                    root.left.left = temp
                else:
                    left(root.left, depth - 1)
            else:
                if depth == 0:  # 末尾插入
                    root.left = TreeNode(val)
                else:  # 深度大于零且不存在子树直接返回
                    return

        def right(root: TreeNode, depth: int):
            if root.right:
                if depth == 0:
                    temp = root.right
                    root.right = TreeNode(val)
                    root.right.right = temp
                else:
                    right(root.right, depth - 1)
            else:
                if depth == 0:
                    root.right = TreeNode(val)
                else:
                    return

        if depth == 1:  # 开头插入
            node = TreeNode(val)
            node.left = root
            return node
        else:
            left(root, depth - 2)
            right(root, depth - 2)
            return root

    def addOneRow2(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        def dfs(root: TreeNode, depth: int):
            if not root:
                return

            if depth == 0:
                left = root.left
                root.left = TreeNode(val)
                root.left.left = left
                right = root.right
                root.right = TreeNode(val)
                root.right.right = right
            else:
                dfs(root.left, depth - 1)
                dfs(root.right, depth - 1)

        if depth == 1:
            node = TreeNode(val)
            node.left = root
            return node
        else:
            dfs(root, depth - 2)
            return root

# print(tree2array(Solution().addOneRow(TreeNode(1, left=TreeNode(2)),1,1)))
# print(tree2array(Solution().addOneRow(TreeNode(1, left=TreeNode(2)),1,2)))
print(tree2array(Solution().addOneRow(TreeNode(1, left=TreeNode(2)), 1, 3)))
# print(tree2array(Solution().addOneRow2(TreeNode(1, left=TreeNode(2)),1,1)))
# print(tree2array(Solution().addOneRow2(TreeNode(1, left=TreeNode(2)),1,2)))
print(tree2array(Solution().addOneRow2(TreeNode(1, left=TreeNode(2)), 1, 3)))
