from collections import deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = {i: [] for i in range(n)}
        degree = [0 for i in range(n)]
        minTreeRoots = []
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            degree[edge[0]] += 1
            degree[edge[1]] += 1

        leaves = deque(i for i in range(n) if degree[i] == 1)
        while leaves:
            minTreeRoots.clear()
            for _ in range(len(leaves)):
                s = leaves.popleft()
                minTreeRoots.append(s)
                for n in graph[s]:
                    degree[n] -= 1
                    if degree[n] == 1:
                        leaves.append(n)
        return minTreeRoots


print(Solution().findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]))
