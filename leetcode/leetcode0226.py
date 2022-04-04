# ****************************************************************分割线****************************************************************
# todo 0226（Invert Binary Tree）
# 翻转二叉树

from common import TreeNode
from common import tree2array

# 栈
class Solution:
    # 池沼算法（只能翻转满二叉树）
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root

        s1 = [root.left]
        s2 = [root.right]
        while s1 and s2:
            left = s1.pop()
            right = s2.pop()
            if left and right:
                temp = right.val
                right.val = left.val
                left.val = temp
                s1.append(left.left)
                s2.append(right.right)
                s1.append(left.right)
                s2.append(right.left)
        return root

    def invertTree2(self, root: TreeNode) -> TreeNode:
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                temp = node.right
                node.right = node.left
                node.left = temp
                stack.append(node.left)
                stack.append(node.right)
        return root

left = TreeNode(2, left=TreeNode(4), right=TreeNode(5))
# right=TreeNode(3,left=TreeNode(6),right=TreeNode(7))
right = None
root = TreeNode(1, left=left, right=right)
print(tree2array(root))
print(tree2array(Solution().invertTree2(root)))
