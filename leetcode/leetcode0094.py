# ****************************************************************分割线****************************************************************
# todo 0094（Binary Tree Inorder Traversal）
# 二叉树的中序遍历（左根右）

from common import TreeNode

class Solution:
    # 递归
    def inorderTraversal(self, root: TreeNode) -> list:
        def test(root: TreeNode, result: list):
            if root is None:
                return
            if root.left:
                print("direction:{direction} node:{node}".format(direction="左", node=root.left.val))
                test(root.left, result)
            # 递归搜索左子节点，直到没有左子节点时，输出当前节点
            result.append(root.val)
            if root.right:
                print("direction:{direction} node:{node}".format(direction="右", node=root.right.val))
                test(root.right, result)

        result = []
        test(root, result)
        return result

    # 栈
    def inorderTraversal2(self, root: TreeNode):
        result, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    result.append(node.val)
                # 中序遍历左根右，栈先进后出，按右根左顺序入栈
                else:
                    stack.append((node.right, False))
                    stack.append((node, True))  # 末端节点/根节点为True
                    stack.append((node.left, False))

                    i = 0
                    str = ""
                    while i < len(stack):
                        if stack[i][0]:
                            str += "{value},{boolean} ".format(value=stack[i][0].val, boolean=stack[i][1])
                        i += 1
                    print(str)
        return result

left = TreeNode(2, left=TreeNode(4), right=TreeNode(5))
right = TreeNode(3, left=TreeNode(6), right=TreeNode(7))
root = TreeNode(1, left=left, right=right)
print(Solution().inorderTraversal(root))
print(Solution().inorderTraversal2(root))
