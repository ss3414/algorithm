# ****************************************************************分割线****************************************************************
# todo 0297（Serialize and Deserialize Binary Tree）
# 二叉树序列化与反序列化

from collections import deque

from common import TreeNode
from common import tree2array

# 池沼算法（层序遍历丢失空节点）
class Codec:
    def __init__(self):
        self.data = []
        self.length = -1

    def clear(self):
        self.data.clear()
        self.length = -1

    def serialize(self, root):
        def bfs(root: TreeNode):
            if root is None:
                return
            queue = deque([root])
            while queue:
                node = queue.popleft()
                self.data.append(node.val if node else "")
                if node:
                    queue.append(node.left if node.left else "")
                    queue.append(node.right if node.right else "")

        bfs(root)
        result = ""
        for i in self.data:
            result += "{i},".format(i=i)
        self.clear()
        return result

    # 递归构建
    def build(self, index):
        root = TreeNode(int(self.data[index]))
        left = 2 * index + 1
        if left < self.length and self.data[left] != "":
            root.left = self.build(left)
        right = 2 * index + 2
        if right < self.length and self.data[right] != "":
            root.right = self.build(right)
        return root

    def deserialize(self, data):
        if data == "":
            return None
        self.data = data.split(",")
        print(self.data)
        self.length = len(self.data)
        root = self.build(0)
        self.clear()
        return root

class Codec2:
    # 层序遍历/数组表示
    def serialize(self, root):
        result = []
        data = [root]
        while data:
            temp = []
            for i in data:
                if i == None:
                    result.append(str(None))
                    continue
                result += [str(i.val)]
                temp.append(i.left if i.left else None)
                temp.append(i.right if i.right else None)
                data = temp
            if data.count(None) == len(data):
                break
        return " ".join(result)

    def deserialize(self, data):
        temp = data.split()
        nodes = []
        for i in temp:
            nodes.append(None if i == "None" else TreeNode(i))
        k = 1
        for j in range(len(temp)):
            if nodes[j] is None:
                continue
            if k >= len(temp):
                break
            nodes[j].left = nodes[k]
            # print("j:{j} k:{k}".format(j=j,k=k))
            k += 1
            nodes[j].right = nodes[k]
            # print("j:{j} k:{k}".format(j=j,k=k))
            k += 1
        return nodes[0]

left = TreeNode(2)
right = TreeNode(3, left=TreeNode(4, left=TreeNode(6), right=TreeNode(7)), right=TreeNode(5))
root = TreeNode(1, left=left, right=right)
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# print(tree)
# print(tree2array(deser.deserialize(tree)))
ser = Codec2()
deser = Codec2()
tree = ser.serialize(root)
print(tree)
print(tree2array(deser.deserialize(tree)))
