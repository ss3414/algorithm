# ****************************************************************分割线****************************************************************
# todo 0124（Binary Tree Maximum Path Sum）
# 二叉树最大路径和

from common import TreeNode

class Solution:
    def __init__(self) -> int:
        self.result = -1001

    def maxPathSum(self, root: TreeNode) -> int:
        def test(root: TreeNode):
            if not root:
                return 0
            left = max(test(root.left), 0)  # 左右都是负数，不加上
            right = max(test(root.right), 0)
            self.result = max(self.result, left + right + root.val)  # self.result记录最大路径和
            return max(left, right) + root.val  # 每次递归返回左右子树中的最大值

        test(root)
        return self.result

root = TreeNode(-1, right=TreeNode(1, left=TreeNode(2), right=TreeNode(3)))
print(Solution().maxPathSum(root))
