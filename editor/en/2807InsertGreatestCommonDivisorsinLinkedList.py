# Definition for singly-linked list.
from typing import Optional
from math import gcd


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def createNodesFromList(lst):
    nodes = [ListNode(lst[-1], None)]
    for i, num in enumerate(lst[::-1][1:]):
        nodes.append(ListNode(num, nodes[i]))

    return nodes[-1]


class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not head.next:
            return head
        cur = head
        while cur.next:
            val = gcd(cur.val, cur.next.val)
            nxt = cur.next
            cur.next = ListNode(val, nxt)
            cur = nxt

        return head


assert Solution().insertGreatestCommonDivisors(
    createNodesFromList([18, 6, 10, 3])
) == createNodesFromList([18, 6, 6, 2, 10, 1, 3])
