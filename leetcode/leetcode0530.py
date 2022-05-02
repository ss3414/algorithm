# ****************************************************************分割线****************************************************************
# todo 0530（Minimum Absolute Difference in BST）
# 二叉搜索树中任意两个节点的最小差值

from common import TreeNode

# DFS
class Solution:
    # 池沼算法（只计算了相邻节点的差）
    def getMinimumDifference(self, root: TreeNode) -> int:
        def test(root: TreeNode, node: TreeNode):
            if node is None:
                return 10 ** 5  # 遍历到末梢返回最大值
            diff = abs(root.val - node.val)
            left = test(node, node.left)
            right = test(node, node.right)
            print("diff:{diff} left:{left} right:{right}".format(diff=diff, left=left, right=right))
            return min(diff, left, right)

        return min(test(root, root.left), test(root, root.right))

    # BST的中序遍历能得到一个有序数组，最小差值在数组相邻元素中产生
    def getMinimumDifference2(self, root: TreeNode) -> int:
        def test(root: TreeNode, nodes: list):
            if root is None:
                return
            test(root.left, nodes)
            nodes.append(root.val)
            test(root.right, nodes)

        nodes = []
        test(root, nodes)
        min_val = abs(nodes[0] - nodes[1])  # 注意规避0
        i = 0
        while i < len(nodes) - 1:
            min_val = min(min_val, abs(nodes[i] - nodes[i + 1]))
            i += 1
        return min_val

left = TreeNode(20, left=TreeNode(10), right=TreeNode(39))
right = TreeNode(60, left=TreeNode(41), right=TreeNode(70))
root = TreeNode(40, left=left, right=right)
# print(Solution().getMinimumDifference(root))
print(Solution().getMinimumDifference2(root))
