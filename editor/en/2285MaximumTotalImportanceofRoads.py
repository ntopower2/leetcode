from typing import List
from heapq import *


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        nodeMap = {u: [0, []] for u in range(n)}
        edgeHeap = []
        for u, v in roads:
            nodeMap[u][1].append(v)
            nodeMap[v][1].append(u)

        for u in range(n):
            heappush(edgeHeap, (-len(nodeMap[u][1]), u))
        while edgeHeap:
            _, x = heappop(edgeHeap)
            nodeMap[x][0] = n
            n -= 1

        res = 0
        for u, v in roads:
            res += nodeMap[u][0] + nodeMap[v][0]

        return res


assert (
    Solution().maximumImportance(5, [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]])
    == 43
)
