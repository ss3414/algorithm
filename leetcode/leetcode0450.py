# ****************************************************************分割线****************************************************************
# todo 0450（Delete Node in a BST）
# 删除二叉搜索树中的节点

from common import TreeNode

class Solution:
    # DFS+二分法（太慢）
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        data = []

        def dfs(root: TreeNode):
            if root is None:
                return
            if root.left:
                dfs(root.left)
            data.append(root.val)
            if root.right:
                dfs(root.right)

        def test(nums, left, right):
            if left > right:
                return None
            middle = left + (right - left) // 2
            root = TreeNode(nums[middle])
            root.left = test(nums, left, middle - 1)
            root.right = test(nums, middle + 1, right)
            return root

        dfs(root)
        print(data)
        if key not in data:
            return root
        data.remove(key)
        root = test(data, 0, len(data) - 1)
        data.clear()
        dfs(root)
        print(data)
        return root

left = TreeNode(2)
right = TreeNode(6, left=TreeNode(5), right=TreeNode(7))
root = TreeNode(4, left=left, right=right)
Solution().deleteNode(root, 5)
