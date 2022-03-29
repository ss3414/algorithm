# ****************************************************************分割线****************************************************************
# todo 0107（Binary Tree Level Order Traversal II）
# 二叉树层序遍历
# 倒序输出，从底层到顶层

from collections import deque

from common import TreeNode

class Solution:
    # BFS
    def levelOrderBottom(self, root: TreeNode) -> list:
        result = []
        queue = deque([(root, 0)])
        while queue:
            node, level = queue.popleft()
            if node:
                if len(result) < level + 1:  # 每深入一层，插入一个空的数组
                    result.insert(0, [])
                print(result)
                result[-(level + 1)].append(node.val)  # 倒序插入值
                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))
        return result

    # DFS
    def levelOrderBottom2(self, root: TreeNode) -> list:
        result = []
        stack = [(root, 0)]
        while stack:
            node, level = stack.pop()
            if node:
                if len(result) < level + 1:
                    result.insert(0, [])
                print(result)
                result[-(level + 1)].append(node.val)  # 根据level插入
                stack.append((node.right, level + 1))
                stack.append((node.left, level + 1))
        return result

left = TreeNode(2, left=TreeNode(4), right=TreeNode(5))
right = TreeNode(3, left=TreeNode(6), right=TreeNode(7))
root = TreeNode(1, left=left, right=right)
# print(Solution().levelOrderBottom(root))
print(Solution().levelOrderBottom2(root))
