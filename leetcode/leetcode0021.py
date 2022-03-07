# ****************************************************************分割线****************************************************************
# todo 0021（Merge Two Sorted Lists）
# 合并两个有序链表

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 把链表节点打散冒泡排序，时间复杂度高
def test(list1: ListNode, list2: ListNode):
    sort_list = []
    if list1 is not None:
        while list1.next is not None:
            sort_list.append(list1)
            list1 = list1.next
        sort_list.append(list1)
    if list2 is not None:
        while list2.next is not None:
            sort_list.append(list2)
            list2 = list2.next
        sort_list.append(list2)
    i = 0
    while i < len(sort_list) - 1:
        j = 0
        is_sorted = True
        while j < len(sort_list) - 1:
            if sort_list[j].val > sort_list[j + 1].val:
                temp = sort_list[j]
                sort_list[j] = sort_list[j + 1]
                sort_list[j + 1] = temp
                is_sorted = False
            j += 1
        if is_sorted:
            break
        i += 1
    k = 0
    while k < len(sort_list) - 1:
        sort_list[k].next = sort_list[k + 1]
    if len(sort_list) > 0:
        return sort_list[0]
    else:
        return None

# 两个链表本身是有序的
def test2(list1: ListNode, list2: ListNode):
    temp = cursor = ListNode()  # temp节点，指向最终返回的有序链表
    # 同时遍历两个有序链表，哪个元素小插入cursor中
    while list1 and list2:
        if list1.val < list2.val:
            cursor.next = list1
            list1 = list1.next  # list1前进（移除表头，下一个元素成为新表头）
        else:
            cursor.next = list2
            list2 = list2.next
        cursor = cursor.next
    # 若list1/list2长度不一致，遍历剩下的链表插入cursor（原链表有序，剩下的一定大于cursor）
    cursor.next = list1 or list2
    return temp.next

# list1=ListNode(1,ListNode(2,ListNode(4,None)))
# list2=ListNode(1,ListNode(3,ListNode(4,None)))
# output=test(list1,list2)

list1 = None
list2 = ListNode(1, None)
output = test2(list1, list2)

while output is not None:
    print(output.val)
    output = output.next
