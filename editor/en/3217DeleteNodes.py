# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, obj: object) -> bool:
        return self.val == obj.val and self.next == obj.next


def createNodesFromList(lst):
    nodes = [ListNode(lst[-1], None)]
    for i, num in enumerate(lst[::-1][1:]):
        nodes.append(ListNode(num, nodes[i]))

    return nodes[-1]


class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        def findNext(node) -> Optional[ListNode]:
            cur = node.next
            while cur and cur.val in nums:
                cur = cur.next

            node.next = cur
            return cur

        nums = set(nums)
        newHead = ListNode(next=head)
        cur = findNext(newHead)
        while cur:
            cur = findNext(cur)

        return newHead.next


assert Solution().modifiedList([6, 4], createNodesFromList([5, 6, 1, 4])) == ListNode(
    5, ListNode(1)
)
