# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x, next):
        self.val = x
        self.next = next


def createNodesFromList(lst):
    nodes = [ListNode(lst[-1], None)]
    for i, num in enumerate(lst[::-1][1:]):
        nodes.append(ListNode(num, nodes[i]))

    return nodes[-1]


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        zeroNode = None
        while cur:
            if not cur.val:
                if not zeroNode:
                    zeroNode = cur
                elif cur.next:
                    zeroNode.next = cur
                    zeroNode = cur
                else:
                    zeroNode.next = None
            else:
                zeroNode.val += cur.val

            cur = cur.next

        return head


assert Solution().mergeNodes(createNodesFromList([0, 3, 1, 0, 4, 5, 2, 0])) == ListNode(
    4, ListNode(11, None)
)
