# 定义链表节点类
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 定义解决方案类
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        carry, curr = 0, dummy
        while l1 or l2 or carry:
            s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry, val = divmod(s, 10)
            curr.next = ListNode(val)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next

# 测试代码
def print_list(node):
    """链表的值"""
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# 创建两个链表
# 第一个链表 342
l1 = ListNode(3)
l1.next = ListNode(4)
l1.next.next = ListNode(2)

# 第二个链表 465
l2 = ListNode(4)
l2.next = ListNode(6)
l2.next.next = ListNode(5)

# 创建解决方案实例
solution = Solution()

# 调用方法并获取结果链表
result = solution.addTwoNumbers(l1, l2)

# 打印结果链表
print("Resulting linked list from adding the two numbers:")
print_list(result)