# Definition for singly-linked list.
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
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        def isInBounds(i, j) -> bool:
            return 0 <= i < m and 0 <= j < n

        i, j = 0, 0
        direction = 0
        res = [[-1] * n for _ in range(m)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while head:
            if isInBounds(i, j):
                res[i][j] = head.val
                head = head.next
            ti, tj = i + directions[direction][0], j + directions[direction][1]
            if not (isInBounds(ti, tj) and res[ti][tj] == -1):
                direction += 1
                direction %= len(directions)
                ti, tj = i + directions[direction][0], j + directions[direction][1]
            i, j = ti, tj
        return res


assert Solution().spiralMatrix(
    13, 1, createNodesFromList([3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0])
) == [[3, 0, 2, 6, 8], [5, 0, -1, -1, 1], [5, 2, 4, 9, 7]]
