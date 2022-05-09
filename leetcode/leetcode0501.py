# ****************************************************************分割线****************************************************************
# todo 0501（Find Mode in Binary Search Tree）
# 二叉搜索树中的众数

from common import TreeNode

class Solution:
    def findMode(self, root: TreeNode) -> list:
        def dfs(root: TreeNode, data: dict):
            if root is None:
                return
            val = data.get(root.val)
            if val is None:
                val = 1
            else:
                val += 1
            data[root.val] = val
            dfs(root.left, data)
            dfs(root.right, data)

        data = {}
        dfs(root, data)
        max_val = max(data.values())
        result = []
        for key, val in data.items():
            if val == max_val:
                result.append(key)
        return result

left = TreeNode(2, left=TreeNode(1), right=TreeNode(2))
right = TreeNode(6, left=TreeNode(5), right=TreeNode(6))
root = TreeNode(4, left=left, right=right)
print(Solution().findMode(root))
