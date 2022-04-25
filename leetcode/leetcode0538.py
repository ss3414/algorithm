# ****************************************************************分割线****************************************************************
# todo 0538（Convert BST to Greater Tree）
# 二叉搜索树转换成累加树

from common import TreeNode

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root is None or (root.left is None and root.right is None):
            return root

        nodes = []

        def dfs(root: TreeNode):
            if root is None:
                return
            if root.left:
                dfs(root.left)
            nodes.append(root)
            if root.right:
                dfs(root.right)

        dfs(root)
        sums = [nodes[-1].val]
        l = len(nodes)
        i = l - 2
        while i >= 0:
            sums.append(sums[-1] + nodes[i].val)
            i -= 1
        j = 0
        print(sums)
        while j < l:
            nodes[j].val = sums[l - 1 - j]
            j += 1
        print([node.val for node in nodes])
        return root

root = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
Solution().convertBST(root)
