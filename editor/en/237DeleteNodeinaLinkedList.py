# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next):
        self.val = x
        self.next = next


def printNextNodes(x):
    while x:
        print(x.val, end=" ")
        x = x.next
    print()


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        tmp = node.next
        node.val = tmp.val
        while tmp.next:
            tmp.val = tmp.next.val
            node = tmp
            tmp = tmp.next
        node.next = None


x4 = ListNode(9, None)
x3 = ListNode(1, x4)
x2 = ListNode(5, x3)
x1 = ListNode(4, x2)
printNextNodes(x1)
Solution().deleteNode(x3)
printNextNodes(x1)
