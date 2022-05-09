# ****************************************************************分割线****************************************************************
# todo 0129（Sum Root to Leaf Numbers）
# 从根到叶子构成的数字之和

from common import TreeNode

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        data = []

        def dfs(root: TreeNode, digit: str):
            if not root.left and not root.right:
                data.append(digit)
                return
            if root.left:
                temp = digit + str(root.left.val)
                dfs(root.left, temp)
            if root.right:
                temp = digit + str(root.right.val)
                dfs(root.right, temp)

        dfs(root, str(root.val))
        result = 0
        for i in data:
            result += int(i)
        return result

root = TreeNode(0, left=TreeNode(2), right=TreeNode(3))
print(Solution().sumNumbers(root))
