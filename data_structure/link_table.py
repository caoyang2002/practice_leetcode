class Node:
    def __init__(self, data):
        self.data = data  # 节点存储的数据
        self.next = None  # 指向下一个节点的指针

class LinkedList:
    def __init__(self):
        self.head = None  # 链表的头节点

    def append(self, data):
        ""“在链表尾部添加一个新节点”""
        new_node = Node(data)
        if not self.head:  # 如果链表为空，头节点即为新节点
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:  # 找到最后一个节点
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        ""“在链表头部添加一个新节点”""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        """打印链表中的所有元素"""
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

# 使用LinkedList类
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.prepend(0)
linked_list.print_list()  # 输出: 0 -> 1 -> 2 -> 3 -> None
