# ****************************************************************分割线****************************************************************
# todo 0106（Construct Binary Tree from Inorder and Postorder Traversal）
# 根据中序、后序遍历构造二叉树

from common import TreeNode

class Solution:
    def buildTree(self, inorder: list, postorder: list) -> TreeNode:
        if inorder:
            ind = inorder.index(postorder.pop())
            root = TreeNode(inorder[ind])
            print("{i} {p} {n}".format(i=inorder[ind], p=inorder[0:ind], n=inorder[ind + 1:]))
            root.right = self.buildTree(inorder[ind + 1:], postorder)
            root.left = self.buildTree(inorder[0:ind], postorder)
            return root

Solution().buildTree([4, 2, 5, 1, 6, 3, 7], [4, 5, 2, 6, 7, 3, 1])
