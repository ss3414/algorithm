# ****************************************************************分割线****************************************************************
# todo 链表

class Node:
    data = 0
    next = None

    def __init__(self, data):
        self.data = data

class LinkedList:
    head = None  # 头节点
    last = None  # 尾节点
    size = 0

    def insert(self, index, data):
        insert_node = Node(data)
        if self.size == 0:  # 空链表
            self.head = insert_node
            self.last = insert_node
        elif index == 0:  # 插入头部
            insert_node.next = self.head
            self.head = insert_node
        elif index == self.size:  # 插入尾部
            self.last.next = insert_node
            self.last = insert_node
        else:  # 插入中间
            prve_node = self.get(index - 1)
            insert_node.next = prve_node.next  # 插入节点指向下一个节点
            prve_node.next = insert_node  # 前一个节点指向插入节点
        self.size += 1

    def remove(self, index):
        if index == 0:  # 删除头部
            self.head = self.head.next
        elif index == self.size - 1:  # 删除尾部（链表下标从0开始）
            prve_node = self.get(index - 1)
            prve_node.next = None
            self.last = prve_node
        else:  # 删除中间
            prve_node = self.get(index - 1)  # 前一个节点
            next_node = prve_node.next.next  # 下一个节点
            prve_node.next = next_node
        self.size -= 1

    def get(self, index):
        temp_node = self.head
        i = 0
        while i < index:
            temp_node = temp_node.next
            i += 1
        return temp_node

    def output(self):
        temp_node = self.head
        str = ""
        while temp_node is not None:
            str += "{data}->".format(data=temp_node.data)
            temp_node = temp_node.next
        print(str)

linkedlist = LinkedList()
linkedlist.insert(0, 3)
linkedlist.insert(0, 1)
linkedlist.insert(linkedlist.size, 4)  # 尾部插入
linkedlist.insert(1, 2)  # 中间插入
linkedlist.output()

linkedlist.remove(0)
linkedlist.output()

linkedlist.remove(1)
linkedlist.output()

linkedlist.remove(linkedlist.size - 1)
linkedlist.output()
