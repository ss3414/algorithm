# ****************************************************************分割线****************************************************************
# todo 0449（Serialize and Deserialize BST）
# 二叉搜索树序列化与反序列化

from collections import deque

from common import TreeNode

class Codec:
    def serialize(self, root: TreeNode) -> str:
        data = []

        def bfs(root: TreeNode):
            if root is None:
                return
            queue = deque([root])
            while queue:
                node = queue.popleft()
                data.append(node.val if node else None)
                if node:
                    queue.append(node.left if node.left else None)
                    queue.append(node.right if node.right else None)

        bfs(root)
        # 去除末端None
        i = len(data) - 1
        while i >= 0:
            if data[i] is not None:
                break
            i -= 1
        data = data[0:i + 1]

        result = ""
        for j in data:
            result += "{j},".format(j=j)
        return result

    # LeetCode的池沼检测机制无法把None识别为Null
    def deserialize(self, data: str) -> TreeNode:
        if data == "":
            return None
        vals = data.split(",")
        vals = vals[:-1]
        length = len(vals)
        nodes = [None] * (length - 1)
        nodes.insert(0, TreeNode(vals[0]))

        i = 0
        while i < length:
            if vals[i] != -1:
                l, r = 2 * i + 1, 2 * i + 2
                left, right = None, None
                if l < length and vals[l] != -1:
                    left = TreeNode(vals[l])
                    nodes[l] = left
                if r < length and vals[r] != -1:
                    right = TreeNode(vals[r])
                    nodes[r] = right
                node = nodes[i]
                node.left = left
                node.right = right
            i += 1
        return nodes[0]

    # 前序遍历
    def serialize2(self, root: TreeNode) -> str:
        vals = []

        def dfs(root: TreeNode):
            if root:
                vals.append(root.val)
                dfs(root.left)
                dfs(root.right)

        dfs(root)
        return " ".join(map(str, vals))

    def deserialize2(self, data: str) -> TreeNode:
        vals = deque(int(val) for val in data.split())
        print(vals)

        def test(minVal, maxVal):
            # 利用BST左小右大特性，若下一个节点小于当前则为左节点，否则跳过
            if vals and minVal < vals[0] < maxVal:
                val = vals.popleft()
                node = TreeNode(val)
                node.left = test(minVal, val)
                node.right = test(val, maxVal)
                return node

        return test(float("-infinity"), float("infinity"))

ser = Codec()
deser = Codec()
left = TreeNode(2)
right = TreeNode(6, left=TreeNode(5), right=TreeNode(7))
root = TreeNode(4, left=left, right=right)
# tree = ser.serialize(root)
# print(tree)
# ans = deser.deserialize(tree)

tree = ser.serialize2(root)
print(tree)
ans = deser.deserialize2(tree)
