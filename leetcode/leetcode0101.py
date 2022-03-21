# ****************************************************************分割线****************************************************************
# todo 0101（Symmetric Tree）
# 对称二叉树

from common import TreeNode

def test(root: TreeNode, nodes: list):
    if root is None:
        return
    test(root.left, nodes)
    nodes.append(root.val)
    test(root.right, nodes)

# 中序遍历加比较值
def test2(root: TreeNode):
    nodes = []
    test(root, nodes)
    print(nodes)
    i, j = 0, len(nodes) - 1
    while i <= j:
        if nodes[i] != nodes[j]:
            return False
        i += 1
        j -= 1
    return True

def test3(left: TreeNode, right: TreeNode):
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False

    if left.val == right.val:
        result1 = test3(left.left, right.right)  # 外侧与外侧比
        result2 = test3(left.right, right.left)  # 内侧与内侧比
        return result1 and result2
    else:
        return False

# 广度优先遍历
def test4(root: TreeNode):
    if root is None:
        return True
    else:
        return test3(root.left, root.right)

left = TreeNode(2, left=TreeNode(3), right=TreeNode(4))
right = TreeNode(2, left=TreeNode(4), right=TreeNode(3))
root = TreeNode(1, left=left, right=right)
# print(test2(root))
print(test4(root))

# test2无法判断非满二叉树，节点为None会被直接忽略
left = TreeNode(2, left=TreeNode(2), right=None)
right = TreeNode(2, left=TreeNode(2))
root = TreeNode(1, left=left, right=right)
# print(test2(root))
# print(test4(root))
