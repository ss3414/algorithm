# ****************************************************************分割线****************************************************************
# todo 0133（Clone Graph）
# 克隆无向图

from collections import deque

class Node:
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors

class Solution:
    # DFS
    def cloneGraph(self, node):
        def test(node, data):
            if node is None:
                return None
            if node in data:
                return data[node]
            clone = Node(node.val)
            data[node] = clone
            for i in node.neighbors:
                print("{p} {s}".format(p=clone.val, s=i.val))
                clone.neighbors.append(test(i, data))
            return clone

        data = {}
        return test(node, data)

    # BFS
    def cloneGraph2(self, node):
        if node is None:
            return None
        queue = deque([node])
        data = {}
        clone = Node(node.val)
        data[node] = clone
        while queue:
            temp = queue.popleft()
            for i in temp.neighbors:
                if i not in data:
                    data[i] = Node(i.val)
                    queue.append(i)
                print("{p} {s}".format(p=data[temp].val, s=i.val))
                data[temp].neighbors.append(data[i])
        return clone

node1, node2, node3, node4 = Node(1), Node(2), Node(3), Node(4)
node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]
# Solution().cloneGraph(node1)
Solution().cloneGraph2(node1)
