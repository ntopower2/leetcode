from typing import List
from heapq import heappop, heappush


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:
        graph = [[] for _ in range(n)]
        dist = [0] * n
        dist[start_node] = 1

        queue = [(-dist[start_node], start_node)]

        for edge, prob in zip(edges, succProb):
            graph[edge[0]].append((edge[1], prob))
            graph[edge[1]].append((edge[0], prob))

        while queue:
            _, u = heappop(queue)
            if u == end_node:
                break
            for v, w in graph[u]:
                if dist[v] < dist[u] * w:
                    dist[v] = dist[u] * w
                    heappush(queue, (-dist[v], v))

        return dist[end_node]


assert (
    Solution().maxProbability(
        n=3,
        edges=[[0, 1], [1, 2], [0, 2]],
        succProb=[0.5, 0.5, 0.3],
        start_node=0,
        end_node=2,
    )
    == 0.3
)
