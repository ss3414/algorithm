# ****************************************************************分割线****************************************************************
# todo 0100（Same Tree）
# 判断两树是否相同

from common import TreeNode

# 递归
def test(p: TreeNode, q: TreeNode, flag: bool):
    # print("p:{p} q:{q}".format(p=p.val,q=q.val))
    if p is None and q is None:  # 没有节点，递归结束
        return flag
    elif p is None or q is None:  # 某一节点为空，两二叉树不相等
        flag = False
        return flag
    elif p.val != q.val:  # 值不同，不相等
        # print("p:{p} q:{q}".format(p=p.val,q=q.val))
        flag = False
        return flag
    flag = test(p.left, q.left, flag)
    flag = test(p.right, q.right, flag)
    return flag

p = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
# q=TreeNode(1,left=TreeNode(3),right=TreeNode(2))
q = TreeNode(1, left=TreeNode(3), right=None)
print(test(p, q, True))
