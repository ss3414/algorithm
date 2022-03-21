# ****************************************************************分割线****************************************************************
# todo 0104（Maximum Depth of Binary Tree）
# 二叉树最大深度

from common import TreeNode

depths = []

def test(root: TreeNode, depth: int):
    if root is None:
        depths.append(depth)
        return
    test(root.left, depth + 1)
    test(root.right, depth + 1)

# 深度优先遍历DFS（LeetCode无法AC）
def test2(root: TreeNode):
    test(root, 0)
    print(depths)
    return max(depths)

# left=TreeNode(2,left=TreeNode(3),right=TreeNode(4))
# right=TreeNode(2,left=TreeNode(4),right=TreeNode(3))
# root=TreeNode(1,left=left,right=right)
# print(test2(root))

root = TreeNode(1, left=None, right=TreeNode(2))

# print(test2(root))

# 等价于test2，但test2无法AC
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def test(root: TreeNode, depth: int):
            if root is None:
                return depth
            return max(test(root.left, depth + 1), test(root.right, depth + 1))

        return test(root, 0)

print(Solution().maxDepth(root))
