# ****************************************************************分割线****************************************************************
# todo 0437（Path Sum III）
# 路径总和III

from common import TreeNode

class Solution:
    def __init__(self):
        self.count = 0

    # 池沼算法（如果targetSum为0，每个节点都符合条件）
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def dfs(root: TreeNode):
            if root is None:
                return
            target(root, targetSum)
            dfs(root.left)
            dfs(root.right)

        def target(root: TreeNode, sum: int):
            sum -= root.val
            if sum == 0:
                self.count += 1
                return
            if root.left:
                target(root.left, sum)
            if root.right:
                target(root.right, sum)

        dfs(root)
        return self.count

    # 太慢
    def pathSum2(self, root: TreeNode, targetSum: int) -> int:
        def dfs(root: TreeNode, target: int):
            if root:
                return int(root.val == target) + dfs(root.left, target - root.val) + dfs(root.right, target - root.val)
            return 0

        if root:
            return dfs(root, targetSum) + self.pathSum2(root.left, targetSum) + self.pathSum2(root.right, targetSum)
        return 0

left = TreeNode(2, left=TreeNode(4), right=TreeNode(5))
right = TreeNode(3, left=TreeNode(6), right=TreeNode(7))
root = TreeNode(1, left=left, right=right)
# print(Solution().pathSum(root,7))
print(Solution().pathSum2(root, 7))
