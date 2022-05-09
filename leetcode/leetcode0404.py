# ****************************************************************分割线****************************************************************
# todo 0404（Sum of Left Leaves）
# 所有左叶子节点值的和

from common import TreeNode

class Solution:
    # DFS
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, flag: bool):
            if root is None:
                return 0
            if not root.left and not root.right:
                if flag:
                    return root.val
                else:
                    return 0
            return dfs(root.left, True) + dfs(root.right, False)

        return dfs(root, False)

# left=TreeNode(2,left=TreeNode(4),right=TreeNode(5))
# right=TreeNode(3,left=TreeNode(6),right=TreeNode(7))
# root=TreeNode(1,left=left,right=right)
root = TreeNode(1, left=TreeNode(2))
print(Solution().sumOfLeftLeaves(root))
