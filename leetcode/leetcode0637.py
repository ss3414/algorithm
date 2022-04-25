# ****************************************************************分割线****************************************************************
# todo 0637（Average of Levels in Binary Tree）
# 二叉树每层平均值

from collections import deque

from common import TreeNode

class Solution:
    # 池沼算法
    def averageOfLevels(self, root: TreeNode) -> list:
        # BFS将二叉树转数组有问题，None未加入数组
        nodes = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            nodes.append(node.val if node else None)
            if node and (node.left or node.right):
                queue.append(node.left)
                queue.append(node.right)
        print(nodes)

        output = []
        begin, between = 0, 1
        while begin + between <= len(nodes):
            temp = nodes[begin:begin + between]
            sum = 0
            count = 0
            i = 0
            while i < len(temp):
                if temp[i]:
                    sum += temp[i]
                    count += 1
                i += 1
            output.append(float(sum / count))
            begin = begin + between
            between *= 2
        return output

    # BFS
    def averageOfLevels2(self, root: TreeNode) -> list:
        output = []
        if not root:
            return output
        queue = deque([root])
        while queue:
            sum = 0
            count = len(queue)
            i = 0
            while i < count:  # 用count而非完全依赖队列本身控制出入队
                node = queue.popleft()
                sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                i += 1
            output.append(float(sum / count))
        return output

left = TreeNode(9, left=None, right=None)
right = TreeNode(20, left=TreeNode(15), right=TreeNode(7))
root = TreeNode(3, left=left, right=right)
# print(Solution().averageOfLevels(root))
print(Solution().averageOfLevels2(root))
