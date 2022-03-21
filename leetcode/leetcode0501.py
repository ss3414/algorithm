# ****************************************************************分割线****************************************************************
# todo 0501（Find Mode in Binary Search Tree）
# 二叉搜索树中的众数

from common import TreeNode

class Solution:
    def findMode(self, root: TreeNode) -> list:
        def test(root: TreeNode, data: dict):
            if root is None:
                return
            val = data.get(root.val)
            if val is None:
                val = 1
            else:
                val += 1
            data.update({root.val: val})
            test(root.left, data)
            test(root.right, data)

        data = {}
        test(root, data)
        max_val = max(data.values())
        result = []
        for key, value in data.items():
            if value == max_val:
                result.append(key)
        return result

left = TreeNode(2, left=TreeNode(1), right=TreeNode(2))
right = TreeNode(6, left=TreeNode(5), right=TreeNode(6))
root = TreeNode(4, left=left, right=right)
print(Solution().findMode(root))