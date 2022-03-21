# ****************************************************************分割线****************************************************************
# todo 0235（Lowest Common Ancestor of a Binary Search Tree）
# 找二叉搜索树两节点的最近公共祖先

from common import TreeNode

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def test(root: TreeNode, node: TreeNode):
            paths = [root]
            while root.val != node.val:
                if root.val > node.val:
                    root = root.left
                elif root.val < node.val:
                    root = root.right
                paths.append(root)
            return paths

        path1 = test(root, p)
        path2 = test(root, q)
        # 找最后一个相同的节点
        result = None
        i = 0
        while i < len(path1) and i < len(path2):
            if path1[i].val == path2[i].val:
                result = path1[i]
            i += 1
        return result

left = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
right = TreeNode(6, left=TreeNode(5), right=TreeNode(7))
root = TreeNode(4, left=left, right=right)
# print(Solution().lowestCommonAncestor(root,TreeNode(2),TreeNode(3)).val)
print(Solution().lowestCommonAncestor(root, TreeNode(3), TreeNode(3)).val)
