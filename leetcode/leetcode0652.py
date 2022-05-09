# ****************************************************************分割线****************************************************************
# todo 0652（Find Duplicate Subtrees）
# 寻找所有重复子树

from common import TreeNode

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> list:
        result = []
        data = {}

        def test(root: TreeNode):
            if not root:
                return "#"
            temp = "{v},{l},{r}".format(v=root.val, l=test(root.left), r=test(root.right))
            if temp in data:
                if data[temp] == 1:
                    result.append(root)
                    data[temp] += 1
            else:
                data[temp] = 1
            return temp

        test(root)
        print(data)
        print([i.val for i in result])
        return result

left = TreeNode(2, left=TreeNode(4))
right = TreeNode(3, left=TreeNode(2, left=TreeNode(4)), right=TreeNode(4))
root = TreeNode(1, left=left, right=right)
Solution().findDuplicateSubtrees(root)
