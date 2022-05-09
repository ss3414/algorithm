# ****************************************************************分割线****************************************************************
# todo 0572（Subtree of Another Tree）
# 另一颗树的子树

from collections import deque

from common import TreeNode

class Solution:
    # 先DFS找与subRoot根节点相同的节点，再BFS比较
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def test(root: TreeNode):
            nodes = []
            queue = deque([root])
            while queue:
                node = queue.popleft()
                nodes.append(node.val if node else None)
                if node and (node.left or node.right):
                    queue.append(node.left)
                    queue.append(node.right)
            return nodes

        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if node.val == subRoot.val:
                    nodes1 = test(node)
                    nodes2 = test(subRoot)
                    print(nodes1)
                    print(nodes2)
                    if nodes1 == nodes2:
                        return True
                stack.append(node.right)
                stack.append(node.left)
        return False

    # 双重递归
    def isSubtree2(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def test(p: TreeNode, q: TreeNode):
            if not p and not q:  # p和q到叶子节点处都相同
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return test(p.left, q.left) and test(p.right, q.right)

        if not root:
            return False
        if test(root, subRoot):
            return True
        return self.isSubtree2(root.left, subRoot) or self.isSubtree2(root.right, subRoot)

root1 = TreeNode(0, left=TreeNode(1, left=TreeNode(2), right=TreeNode(3)), right=TreeNode(0, right=TreeNode(0)))
root2 = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
# print(Solution().isSubtree(root1, root2))
print(Solution().isSubtree2(root1, root2))
