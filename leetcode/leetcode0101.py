# ****************************************************************分割线****************************************************************
# todo 0101（Symmetric Tree）
# 对称二叉树

from common import TreeNode

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def test(left: TreeNode, right: TreeNode):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False

            if left.val == right.val:
                result1 = test(left.left, right.right)  # 外侧与外侧比
                result2 = test(left.right, right.left)  # 内侧与内侧比
                return result1 and result2
            else:
                return False

        if root is None:
            return True
        else:
            return test(root.left, root.right)

left = TreeNode(2, left=TreeNode(3), right=TreeNode(4))
right = TreeNode(2, left=TreeNode(4), right=TreeNode(3))
root = TreeNode(1, left=left, right=right)
print(Solution().isSymmetric(root))
