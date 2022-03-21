# ****************************************************************分割线****************************************************************
# todo 0653（Two Sum IV - Input is a BST）
# 在二叉搜索树中求两数和

from collections import deque

from common import TreeNode

# 两数之和优先使用HashTable/HashSet来做
class Solution:
    # DFS
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def test(root: TreeNode, k: int, data: set):
            if root is None:
                return False
            if (k - root.val) in data:
                return True
            data.add(root.val)
            return test(root.left, k, data) or test(root.right, k, data)

        return test(root, k, set())

    # BFS
    def findTarget2(self, root: TreeNode, k: int) -> bool:
        if root is None:
            return False
        data = set()
        input_queue = deque([root])
        while len(input_queue) > 0:
            node = input_queue.popleft()
            if (k - node.val) in data:
                return True
            data.add(node.val)
            if node.left:
                input_queue.append(node.left)
            if node.right:
                input_queue.append(node.right)
        return False

left = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
right = TreeNode(6, left=TreeNode(4), right=TreeNode(7))
root = TreeNode(4, left=left, right=right)
# print(Solution().findTarget(root,9))
print(Solution().findTarget2(root, 9))
