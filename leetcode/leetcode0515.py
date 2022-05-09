# ****************************************************************分割线****************************************************************
# todo 0515（Find Largest Value in Each Tree Row）
# 寻找二叉树每层最大值

from collections import deque

from common import TreeNode

class Solution:
    def largestValues(self, root: TreeNode) -> list:
        result = []
        if not root:
            return result

        queue = deque([root])
        while queue:
            l = len(queue)
            i = 0
            max_val = 0
            while i < l:
                node = queue.popleft()
                # 每层开始重置最大值，每层结束添加
                if i == 0:
                    max_val = node.val
                max_val = max(max_val, node.val)
                if i == l - 1:
                    result.append(max_val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                i += 1
        return result

left = TreeNode(2, left=TreeNode(4), right=TreeNode(5))
right = TreeNode(3, left=TreeNode(6), right=TreeNode(7))
root = TreeNode(1, left=left, right=right)
print(Solution().largestValues(root))
