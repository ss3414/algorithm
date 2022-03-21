# ****************************************************************分割线****************************************************************
# todo 0705（Design HashSet）
# 设计HashSet

from common import ListNode
from common import linkedlist2str

# Set无序不重复，HashSet利用哈希函数计算是否重复，HashSet可以在常数时间内判断元素是否存在
class MyHashSet:
    head = tail = None

    def __init__(self):
        self.head = self.tail = ListNode(-1)

    def add(self, key: int) -> None:
        cursor = self.head
        while cursor:
            if cursor.val == key:  # 重复不再添加
                return
            cursor = cursor.next

        node = ListNode(key, None)
        self.tail.next = node
        self.tail = self.tail.next

    def remove(self, key: int) -> None:
        temp = ListNode(-1)
        temp.next = self.head  # 先把head挂到temp上，再复制一个cursor去迭代
        cursor = temp
        while cursor.next:
            if cursor.next.val == key:
                cursor.next = cursor.next.next
            else:
                cursor = cursor.next
        self.head = temp.next
        self.tail = cursor  # 删除后重新指向尾

    def contains(self, key: int) -> bool:
        cursor = self.head
        while cursor:
            if cursor.val == key:
                return True
            cursor = cursor.next
        return False

    def output(self):
        cursor = self.head
        print("tail:{tail} linkedlist:{linkedlist}".format(
            tail=self.tail.val, linkedlist=linkedlist2str(cursor)))

class MyHashSet2:
    data = None

    def __init__(self):
        self.data = [0] * (10 ** 6 + 1)  # 数组实现

    def add(self, key: int) -> None:
        self.data[key] = 1

    def remove(self, key: int) -> None:
        self.data[key] = 0

    def contains(self, key: int) -> bool:
        return self.data[key] == 1

# obj=MyHashSet()
# obj.add(1)
# obj.add(1)
# obj.add(2)
# obj.add(3)
# obj.output()
# obj.remove(1)
# obj.add(4)
# obj.output()
# print(obj.contains(1))
# print(obj.contains(2))
