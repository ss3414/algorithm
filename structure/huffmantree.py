# ****************************************************************分割线****************************************************************
# todo 哈夫曼树

class Node:
    def __init__(self, char=None, val=None):
        self.char = char
        self.val = val
        self.left = None
        self.right = None

class HuffmanTree:
    def __init__(self, weights):
        self.nodes = [Node(weight[0], weight[1]) for weight in weights]

        # 构建哈夫曼树
        while len(self.nodes) != 1:
            self.nodes.sort(key=lambda node: node.val, reverse=True)  # 排序
            left = self.nodes.pop()
            right = self.nodes.pop()
            temp = Node(val=left.val + right.val)  # 生成临时父节点
            temp.left = left
            temp.right = right
            self.nodes.append(temp)

        self.root = self.nodes[0]

    # 递归输出哈夫曼树
    def encode(self, root, route):
        if not root:
            return
        elif root.char:
            print("{c} {e}".format(c=root.char, e=route))
            return

        # 左0右1
        self.encode(root.left, route + "0")
        self.encode(root.right, route + "1")

    def output(self):
        self.encode(self.root, "")

weights = [("a", 6), ("b", 4), ("c", 10), ("d", 8), ("f", 12), ("g", 2)]
tree = HuffmanTree(weights)
tree.output()
