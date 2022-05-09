# ****************************************************************分割线****************************************************************
# todo 0508（Most Frequent Subtree Sum）
# 高频子树和

from common import TreeNode

class Solution:
    def __init__(self):
        self.data = {}

    def findFrequentTreeSum(self, root: TreeNode) -> list:
        def test(val: int):
            if val in self.data:
                self.data[val] += 1
            else:
                self.data[val] = 1

        def dfs(root: TreeNode):
            if not root.left and not root.right:
                val = root.val
                test(val)
                return val

            left, right = 0, 0
            if root.left:
                left = dfs(root.left)
            if root.right:
                right = dfs(root.right)
            val = root.val
            val += (left + right)
            test(val)
            return val

        dfs(root)
        # print(self.data)
        max_val = max(self.data.values())
        result = []
        for key, val in self.data.items():
            if val == max_val:
                result.append(key)
        return result

left = TreeNode(2, left=TreeNode(4), right=TreeNode(5))
right = TreeNode(3, left=TreeNode(6), right=TreeNode(7))
root = TreeNode(1, left=left, right=right)
# print(Solution().findFrequentTreeSum(root))
print(Solution().findFrequentTreeSum(TreeNode(5, left=TreeNode(2), right=TreeNode(-5))))
