# ****************************************************************分割线****************************************************************
# todo 0897（Increasing Order Search Tree）
# 升序二叉搜索树

from common import TreeNode

class Solution:
    # 太慢
    def increasingBST(self, root: TreeNode) -> TreeNode:
        data = []

        def dfs(root: TreeNode):
            if not root:
                return
            dfs(root.left)
            data.append(root)
            dfs(root.right)

        dfs(root)
        i = 0
        while i < len(data) - 1:
            data[i].right = data[i + 1]
            i += 1
        for j in data:
            j.left = None
        return data[0]

left = TreeNode(2)
right = TreeNode(6, left=TreeNode(5), right=TreeNode(7))
root = TreeNode(4, left=left, right=right)
Solution().increasingBST(root)
