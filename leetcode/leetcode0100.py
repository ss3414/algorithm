# ****************************************************************分割线****************************************************************
# todo 0100（Same Tree）
# 判断两树是否相同

from common import TreeNode

class Solution:
    # 递归
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def test(p: TreeNode, q: TreeNode):
            # print("p:{p} q:{q}".format(p=p.val,q=q.val))
            if p is None and q is None:  # 没有节点，递归结束
                return True
            elif p is None or q is None:  # 某一节点为空，两二叉树不相等
                return False
            elif p.val != q.val:  # 值不同，不相等
                # print("p:{p} q:{q}".format(p=p.val,q=q.val))
                return False
            return test(p.left, q.left) and test(p.right, q.right)

        return test(p, q)

p = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
q = TreeNode(1, left=TreeNode(3), right=None)
print(Solution().isSameTree(p, q))
