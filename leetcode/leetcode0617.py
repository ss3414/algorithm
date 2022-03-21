# ****************************************************************分割线****************************************************************
# todo 0617（Merge Two Binary Trees）
# 合并二叉树

from collections import deque

from common import TreeNode
from common import tree2array

class Solution:
    # 池沼算法（BFS把二叉树转换成数组表示再合并）
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        def test(root: TreeNode):
            output = []
            input_queue = deque([root])
            while len(input_queue) > 0:
                node = input_queue.popleft()
                output.append(node)
                if node and (node.left or node.right):
                    input_queue.append(node.left)
                    input_queue.append(node.right)
            return output

        output1 = test(root1)
        output2 = test(root2)
        result = []
        length = min(len(output1), len(output2))
        i = 0
        while i < length:
            if output1[i] and output2[i]:
                output1[i].val += output2[i].val
                result.append(output1[i])
            elif output1[i] and not output2[i]:
                result.append(output1[i])
            elif not output1[i] and output2[i]:
                result.append(output2[i])
            else:
                result.append(output1[i])
            i += 1
        if len(output1) > len(output2):
            result.extend(output1[length:len(output1)])
        else:
            result.extend(output2[length:len(output2)])
        j = 0
        while j < len(result):
            # None节点，奇数给父节点的左节点赋值，偶数右节点
            if j > 0 and j % 2 == 1:
                result[int(0.5 * (j - 1))].left = result[j]
            if j > 0 and j % 2 == 0:
                result[int(0.5 * (j - 2))].right = result[j]
            j += 1
        return result[0]

    # fixme 递归
    def mergeTrees2(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1
        root = TreeNode(root1.val + root2.val)
        root.left = self.mergeTrees2(root1.left, root2.left)
        root.right = self.mergeTrees2(root1.right, root2.right)
        return root

root1 = TreeNode(1, left=TreeNode(2, left=TreeNode(3)))
root2 = TreeNode(1, right=TreeNode(2, right=TreeNode(3)))
print(tree2array(root1))
print(tree2array(root2))
# print(tree2array(Solution().mergeTrees(root1,root2)))
print(tree2array(Solution().mergeTrees2(root1, root2)))
