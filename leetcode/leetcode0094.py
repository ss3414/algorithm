# ****************************************************************分割线****************************************************************
# todo 0094（Binary Tree Inorder Traversal）
# 二叉树的中序遍历（左根右）

from common import TreeNode

# 递归
def test(root: TreeNode, results: list):
    if root is None:
        return
    if root.left is not None:
        print("direction:{direction} node:{node}".format(direction="左", node=root.left.val))
        test(root.left, results)
    # 递归查询左子节点，直到没有左子节点时，输出当前节点
    results.append(root.val)
    if root.right is not None:
        print("direction:{direction} node:{node}".format(direction="右", node=root.right.val))
        test(root.right, results)

# 栈
def test2(root: TreeNode):
    results, stack = [], [(root, False)]
    while stack:
        node, visited = stack.pop()
        if node:
            if visited:
                results.append(node.val)
            # 中序遍历左根右，栈先进后出，按右根左顺序入栈
            else:
                stack.append((node.right, False))
                stack.append((node, True))  # 末端节点/根节点为True
                stack.append((node.left, False))

                i = 0
                str = ""
                while i < len(stack):
                    if stack[i][0] is not None:
                        str += "{value},{boolean} ".format(value=stack[i][0].val, boolean=stack[i][1])
                    i += 1
                print(str)
    return results

left = TreeNode(2, left=TreeNode(4), right=TreeNode(5))
right = TreeNode(3, left=TreeNode(6), right=TreeNode(7))
root = TreeNode(1, left=left, right=right)

# results=[]
# test(root,results)
# print(results)

print(test2(root))

# ************************************************************半分割线******************************

# LeetCode提交代码（递归写法）
# class Solution:
#     def test(self,root:TreeNode,results:list):
#         if root is None:
#             return
#         if root.left is not None:
#             self.test(root.left,results)
#         results.append(root.val)
#         if root.right is not None:
#             self.test(root.right,results)

#     def inorderTraversal(self,root:TreeNode)->list:
#         results=[]
#         self.test(root,results)
#         return results
