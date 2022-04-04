# ****************************************************************分割线****************************************************************
# todo 0563（Binary Tree Tilt）
# 二叉树的坡度之和
# 坡度：左右子树的差

from common import TreeNode

class Solution:
    # DFS
    def findTilt(self, root: TreeNode) -> int:
        def test(root: TreeNode):
            tilt = 0
            stack = [root]
            while stack:
                node = stack.pop()
                if node:
                    tilt += node.val
                    stack.append(node.right)
                    stack.append(node.left)
            return tilt

        sum = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                sum += abs(test(node.left) - test(node.right))
                stack.append(node.right)
                stack.append(node.left)
        return sum

root = TreeNode(1, left=TreeNode(2, left=TreeNode(4)), right=TreeNode(3, right=TreeNode(5)))
print(Solution().findTilt(root))
