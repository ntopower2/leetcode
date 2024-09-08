from typing import List, Optional


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
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:

        size = 0
        cur = head
        while cur:
            size += 1
            cur = cur.next

        splitSize, remainder = divmod(size, k)
        res = [None for _ in range(k)]
        node = head

        for partIndex in range(k):
            targetNode = node
            if not targetNode:
                return res
            targetSize = splitSize + (partIndex < remainder)

            for _ in range(targetSize - 1):
                node = node.next

            if node:
                nxt = node.next
                node.next = None
                node = nxt

            res[partIndex] = targetNode

        return res


assert Solution().splitListToParts(createNodesFromList([1, 2, 3]), 5) == [
    [ListNode(1)],
    [ListNode(2)],
    [ListNode(3)],
    [],
    [],
]
