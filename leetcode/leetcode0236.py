# ****************************************************************分割线****************************************************************
# todo 0236（Lowest Common Ancestor of a Binary Tree）
# 最近公共祖先

from common import TreeNode

class Solution:
    # DFS（太慢）
    def lowestCommonAncestor(self, root, p, q):
        def dfs(root: TreeNode, target: TreeNode, paths: list):
            if root is None:
                return None
            if root and root.val == target.val:
                return paths + [root]
            left = dfs(root.left, target, paths + [root])
            right = dfs(root.right, target, paths + [root])
            return left if left else right

        path1, path2 = dfs(root, p, []), dfs(root, q, [])
        # print([i.val for i in path1])
        # print([i.val for i in path2])
        result = None
        l = min(len(path1), len(path2))
        i = 0
        while i < l:
            if path1[i].val == path2[i].val:
                result = path1[i]
            i += 1
        return result

    # 递归
    def lowestCommonAncestor2(self, root, p, q):
        if not root or p.val == root.val or q.val == root.val:
            return root
        left = self.lowestCommonAncestor2(root.left, p, q)
        right = self.lowestCommonAncestor2(root.right, p, q)
        if left and right:  # 如果左右都存在，则表明root为公共祖先
            return root
        # 这里利用递归的特性，如果p和q都在一条子树上，则递归先返回q，再返回p
        node = left if left else right
        # print(node.val if node else None)
        return node

left = TreeNode(2, left=TreeNode(4), right=TreeNode(5))
right = TreeNode(3, left=TreeNode(6), right=TreeNode(7))
root = TreeNode(1, left=left, right=right)
# print(Solution().lowestCommonAncestor(root, TreeNode(2), TreeNode(4)).val)
print(Solution().lowestCommonAncestor2(root, TreeNode(2), TreeNode(4)).val)
