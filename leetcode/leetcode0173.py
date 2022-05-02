# ****************************************************************分割线****************************************************************
# todo 0173（Binary Search Tree Iterator）
# 二叉搜索树迭代器

from common import TreeNode

class BSTIterator:
    def __init__(self, root: TreeNode):
        self.data = []
        self.dfs(root)
        self.index = 0

    def dfs(self, root: TreeNode):
        if root is None:
            return
        if root.left:
            self.dfs(root.left)
        self.data.append(root.val)
        if root.right:
            self.dfs(root.right)

    def next(self) -> int:
        result = -1
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
        return result

    def hasNext(self) -> bool:
        if self.index < len(self.data):
            return True
        return False

left = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
right = TreeNode(6, left=TreeNode(5), right=TreeNode(7))
root = TreeNode(4, left=left, right=right)
obj = BSTIterator(root)
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
