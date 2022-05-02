# ****************************************************************分割线****************************************************************
# todo 0095（Unique Binary Search Trees II）
# 不同的二叉搜索树II

from common import TreeNode

class Solution:
    def generateTrees(self, n: int) -> list:
        def test(start: int, end: int):
            if start > end:
                return None

            result = []
            i = start
            while i <= end:
                left, right = test(start, i - 1), test(i + 1, end)
                for j in left or [None]:
                    for k in right or [None]:
                        node = TreeNode(i)
                        node.left = j
                        node.right = k
                        result.append(node)
                i += 1
            return result

        return test(1, n)

print(len(Solution().generateTrees(1)))
print(len(Solution().generateTrees(3)))
