# ****************************************************************分割线****************************************************************
# todo 0105（Construct Binary Tree from Preorder and Inorder Traversal）
# 根据前序、中序遍历构造二叉树

from common import TreeNode

class Solution:
    def buildTree(self, preorder: list, inorder: list) -> TreeNode:
        if inorder:
            ind = inorder.index(preorder.pop(0))  # 前序遍历，所有根节点在数组前半段
            root = TreeNode(inorder[ind])
            # print("{i} {p} {n}".format(i=inorder[ind],p=inorder[0:ind],n=inorder[ind+1:]))
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind + 1:])
            return root

Solution().buildTree([1, 2, 4, 5, 3, 6, 7], [4, 2, 5, 1, 6, 3, 7])
