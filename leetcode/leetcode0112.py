# ****************************************************************分割线****************************************************************
# todo 0112（Path Sum）
# 判断是否存在路径，使路径上的节点值总和等于目标值

from common import TreeNode

# DFS
class Solution:
    # 包含到叶子节点和None节点的路径
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def test(root: TreeNode, targetSum: int):
            if root is not None:
                return test(root.left, targetSum - root.val) or test(root.right, targetSum - root.val)
            if root is None:
                if targetSum == 0:
                    return True
                else:
                    return False

        if root is None:
            return False
        else:
            return test(root, targetSum)

    # 只包含到叶子节点的路径
    def hasPathSum2(self, root: TreeNode, targetSum: int) -> bool:
        def test(root: TreeNode, targetSum: int):
            if root is not None:
                if root.left is None and root.right is None:
                    if targetSum - root.val == 0:  # 叶子节点
                        return True
                    else:
                        return False
                else:
                    return test(root.left, targetSum - root.val) or test(root.right, targetSum - root.val)
            if root is None:
                return False

        return test(root, targetSum)

# left=TreeNode(2,left=TreeNode(4),right=TreeNode(5))
# right=TreeNode(3,left=TreeNode(6),right=TreeNode(7))
# root=TreeNode(1,left=left,right=right)
# print(Solution().hasPathSum(root,7))

root = TreeNode(1, right=TreeNode(2))
print(Solution().hasPathSum2(root, 1))
