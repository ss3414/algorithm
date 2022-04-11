# ****************************************************************分割线****************************************************************
# todo 二叉树

from queue import Queue

class Node:
    data = 0
    left_child = None
    right_child = None

    def __init__(self, data):
        self.data = data

# 构建二叉树
def build(index: int, input: list):
    tree_node = Node(input[index])
    try:
        if input[2 * index + 1] is not None:
            tree_node.left_child = build(2 * index + 1, input)
        if input[2 * index + 2] is not None:
            tree_node.right_child = build(2 * index + 2, input)
        return tree_node
    except Exception:
        return tree_node

# 输出二叉树
def output(node: Node):
    if node.left_child is not None or node.right_child is not None:
        print("root:{root} left:{left} right:{right}".format(
            root=node.data,
            left=None if node.left_child is None else node.left_child.data,
            right=None if node.right_child is None else node.right_child.data))
    if node.left_child is not None:
        output(node.left_child)
    if node.right_child is not None:
        output(node.right_child)

# 前序遍历（根/左/右）
def pre_order_traversal(node: Node):
    if node is None:
        return
    print(node.data)
    pre_order_traversal(node.left_child)
    pre_order_traversal(node.right_child)

# 中序遍历（左/根/右）
def in_order_traversal(node: Node):
    if node is None:
        return
    in_order_traversal(node.left_child)
    print(node.data)
    in_order_traversal(node.right_child)

# 后序遍历（左/右/根）
def post_order_traversal(node: Node):
    if node is None:
        return
    post_order_traversal(node.left_child)
    post_order_traversal(node.right_child)
    print(node.data)

# 层序遍历
def level_order_traversal(root: Node):
    input_queue = Queue()
    input_queue.put(root)
    # 利用队列先进先出的特性，父节点出队子节点入队同时完成
    while not input_queue.empty():
        output_node = input_queue.get()
        print(output_node.data)
        if output_node.left_child is not None:
            input_queue.put(output_node.left_child)
        if output_node.right_child is not None:
            input_queue.put(output_node.right_child)

# 构建二叉树
test = [1, 2, 3, 4, 5, 6, 7]
binary_tree = build(0, test)
# output(binary_tree)

# 深度优先遍历
# pre_order_traversal(binary_tree)
# in_order_traversal(binary_tree)
# post_order_traversal(binary_tree)

# 广度优先遍历
level_order_traversal(binary_tree)
