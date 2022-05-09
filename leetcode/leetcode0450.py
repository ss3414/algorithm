# ****************************************************************分割线****************************************************************
# todo 0450（Delete Node in a BST）
# 删除二叉搜索树中的节点

from common import TreeNode
from common import tree2array

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

            middle = (left + right) // 2
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

    # 池沼算法（左右子树都满时会丢失节点）
    def deleteNode2(self, root: TreeNode, key: int) -> TreeNode:
        def delete(root: TreeNode):
            left = root.left
            right = root.right
            if not left and not right:  # 左右都不存在
                root = None
            if left:
                left.right = right
                root = left
            elif right:
                right.left = left
                root = right
            return root

        def dfs(root: TreeNode):
            if root.left and root.left.val == key:
                root.left = delete(root.left)
                return
            if root.right and root.right.val == key:
                root.right = delete(root.right)
                return

            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)

        if not root:
            return root
        if root.val == key:
            root = delete(root)
            return root

        dfs(root)
        return root

    # 递归
    def deleteNode3(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        if root.val > key:  # 利用BST特性寻找key
            root.left = self.deleteNode3(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode3(root.right, key)
        else:
            if not root.left or not root.right:  # 左右子树有一个为空
                root = root.left if root.left else root.right
            else:
                # 左右均为满二叉树，寻找右子树左下角最小值，和root交换后删除
                cursor = root.right
                while cursor.left:
                    cursor = cursor.left
                root.val = cursor.val
                root.right = self.deleteNode3(root.right, cursor.val)
        return root

left = TreeNode(2)
right = TreeNode(6, left=TreeNode(5), right=TreeNode(7))
root = TreeNode(4, left=left, right=right)
# Solution().deleteNode(root, 5)
print(tree2array(root))
# print(tree2array(Solution().deleteNode2(root, 2)))
# print(tree2array(Solution().deleteNode2(root, 4)))
print(tree2array(Solution().deleteNode3(root, 4)))
