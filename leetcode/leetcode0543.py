# ****************************************************************分割线****************************************************************
# todo 0543（Diameter of Binary Tree）
# 二叉树的直径
# 直径：任意两节点间的最大距离，任意节点左右子树深度和的最大值

from common import TreeNode

class Solution:
    # fixme 双重递归
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        data = {}

        # 计算每个节点左右子树深度和
        def test(root: TreeNode):
            if root is None:
                return 0
            if root in data.keys():
                return data[root]
            h = max(test(root.left), test(root.right)) + 1
            data.update({root: h})
            return h

        if root is None:
            return 0
        result = test(root.left) + test(root.right)
        return max(result, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

root = TreeNode(1, left=TreeNode(2, left=TreeNode(3, left=TreeNode(5)), right=TreeNode(4, right=TreeNode(6))))
print(Solution().diameterOfBinaryTree(root))
