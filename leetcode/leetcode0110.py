# ****************************************************************分割线****************************************************************
# todo 0110（Balanced Binary Tree）
# 判断是否为平衡二叉树

from common import TreeNode

def test(root: TreeNode, depth: int, diffs: list):
    if root is None:  # 叶子节点，直接返回长度
        return depth
    left_depth = test(root.left, depth + 1, diffs)
    right_depth = test(root.right, depth + 1, diffs)
    print("root:{root} left:{left} right:{right}".format(root=root.val, left=left_depth, right=right_depth))
    diffs.append(abs(left_depth - right_depth))
    # if abs(left_depth-right_depth)>1:  # 无法翻转全局flag
    #     flag=False
    return max(left_depth, right_depth)  # 非叶子节点，返回左右最长子树长度

# DFS（LeetCode无法AC）
def test2(root: TreeNode):
    diffs = []
    test(root, 0, diffs)
    return max(diffs) <= 1

left = TreeNode(2, left=TreeNode(4, left=TreeNode(6)), right=TreeNode(5))
right = TreeNode(3)
root = TreeNode(1, left=left, right=right)

# print(test2(root))

class Solution:
    # DFS+双层递归
    def isBalanced(self, root: TreeNode) -> bool:
        def test(root: TreeNode):
            if root is None:
                return 0
            max_val = max(test(root.left), test(root.right)) + 1
            print("left:{left} right:{right} max:{max}".format(
                left=left.val, right=right.val, max=max_val))
            return max_val  # 返回输入节点左右子树最大深度

        if root is None:
            return True
        if abs(test(root.left) - test(root.right)) > 1:  # 左右节点
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)  # 左右子树

    # DFS（用-1代替flag层层返回，避免重复计算）
    def isBalanced2(self, root: TreeNode) -> bool:
        def test(root: TreeNode):
            if root is None:
                return 0

            left = test(root.left)
            if left == -1:
                return -1
            right = test(root.right)
            if right == -1:
                return -1
            diff = abs(left - right)
            if diff > 1:
                return -1

            max_val = max(left, right) + 1
            return max_val

        if test(root) == -1:
            return False
        else:
            return True

# print(Solution().isBalanced(root))
print(Solution().isBalanced2(root))
