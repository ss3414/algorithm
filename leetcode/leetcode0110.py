# ****************************************************************分割线****************************************************************
# todo 0110（Balanced Binary Tree）
# 判断是否为平衡二叉树

from common import TreeNode

class Solution:
    # DFS+双层递归
    def isBalanced(self, root: TreeNode) -> bool:
        def test(root: TreeNode):
            if root is None:
                return 0
            max_val = max(test(root.left), test(root.right)) + 1
            print("left:{left} right:{right} max:{max}".format(
                left=left.val, right=right.val, max=max_val))
            return max_val  # 返回输入节点左右子树最大深度

        if root is None:
            return True
        if abs(test(root.left) - test(root.right)) > 1:  # 左右节点
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)  # 左右子树

    # DFS（用-1代替flag层层返回，避免重复计算）
    def isBalanced2(self, root: TreeNode) -> bool:
        def test(root: TreeNode):
            if root is None:
                return 0

            left = test(root.left)
            if left == -1:
                return -1
            right = test(root.right)
            if right == -1:
                return -1
            diff = abs(left - right)
            if diff > 1:
                return -1

            max_val = max(left, right) + 1
            return max_val

        if test(root) == -1:
            return False
        else:
            return True

left = TreeNode(2, left=TreeNode(4, left=TreeNode(6)), right=TreeNode(5))
right = TreeNode(3)
root = TreeNode(1, left=left, right=right)
# print(Solution().isBalanced(root))
print(Solution().isBalanced2(root))
