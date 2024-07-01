from typing import List
from collections import deque


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adjList = [[] for _ in range(n)]
        inDegree = [0] * n
        ancestors = [set() for _ in range(n)]
        for u, v in edges:
            adjList[u].append(v)
            inDegree[v] += 1

        q = deque([v for v in range(n) if not inDegree[v]])
        while q:
            node = q.popleft()
            for neighbor in adjList[node]:
                ancestors[neighbor].add(node)
                ancestors[neighbor].update(ancestors[node])
                inDegree[neighbor] -= 1
                if not inDegree[neighbor]:
                    q.append(neighbor)

        return [sorted(list(nodeSet)) for nodeSet in ancestors]


assert Solution().getAncestors(
    8, [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]]
) == [[], [], [], [0, 1], [0, 2], [0, 1, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3]]
