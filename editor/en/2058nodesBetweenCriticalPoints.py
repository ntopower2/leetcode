# Definition for singly-linked list.
from typing import List, Optional


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
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        cur = head.next
        prev = head.val
        prevPos, i = 0, 2
        vals = [0, -1, -1]
        while cur:
            if cur.next:
                if cur.val > max(prev, cur.next.val) or cur.val < min(
                    prev, cur.next.val
                ):
                    if not vals[0]:
                        vals[0] = i
                    else:
                        vals[2] = i - vals[0]
                        vals[1] = (
                            i - vals[0] if vals[1] == -1 else min(i - prevPos, vals[1])
                        )
                        prevPos = i
            prev = cur.val
            cur = cur.next
            i += 1

        return vals[1:]


assert Solution().nodesBetweenCriticalPoints(
    createNodesFromList([10, 1, 2, 3, 3, 9, 6, 1, 10])
) == [2, 6]
assert Solution().nodesBetweenCriticalPoints(
    createNodesFromList([5, 3, 1, 2, 5, 1, 2])
) == [1, 3]
