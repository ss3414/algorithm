# ****************************************************************分割线****************************************************************
# todo 0236（Lowest Common Ancestor of a Binary Tree）
# 最近公共祖先

from common import TreeNode

class Solution:
    # 太慢
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
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
        print(result.val)
        return result

left = TreeNode(2, left=TreeNode(4), right=TreeNode(5))
right = TreeNode(3, left=TreeNode(6), right=TreeNode(7))
root = TreeNode(1, left=left, right=right)
Solution().lowestCommonAncestor(root, TreeNode(2), TreeNode(4))
