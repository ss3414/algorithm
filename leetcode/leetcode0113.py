# ****************************************************************分割线****************************************************************
# todo 0112（Path Sum II）
# 路径总和II

import copy

from common import TreeNode

class Solution:
    # 深拷贝（太慢）
    def pathSum(self, root: TreeNode, targetSum: int) -> list:
        result = []

        if root is None:
            return result

        def dfs(root: TreeNode, paths: list):
            if not root.left and not root.right:
                if sum(paths) == targetSum:
                    result.append(paths)
            if root.left:
                temp = copy.deepcopy(paths)
                temp.append(root.left.val)
                dfs(root.left, temp)
            if root.right:
                temp = copy.deepcopy(paths)
                temp.append(root.right.val)
                dfs(root.right, temp)

        dfs(root, [root.val])
        return result

    def pathSum2(self, root: TreeNode, targetSum: int) -> list:
        result = []

        if root is None:
            return result

        def dfs(root: TreeNode, temp: list):
            if not root.left and not root.right:
                if sum(temp) + root.val == targetSum:
                    temp.append(root.val)
                    result.append(temp)
            if root.left:
                dfs(root.left, temp + [root.val])  # 每次递归新生成数组（值引用）
            if root.right:
                dfs(root.right, temp + [root.val])

        dfs(root, [])
        return result

left = TreeNode(2, left=TreeNode(4), right=TreeNode(5))
right = TreeNode(2, left=TreeNode(4), right=TreeNode(5))
root = TreeNode(1, left=left, right=right)
# print(Solution().pathSum(root,7))
print(Solution().pathSum2(root, 7))
