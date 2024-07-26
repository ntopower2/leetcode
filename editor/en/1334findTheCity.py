from typing import List


class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        dist = [[float("inf")] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0

        for u, v, w in edges:
            dist[u][v] = dist[v][u] = w

        # floyd - warshall
        for mid in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][mid] + dist[mid][j])

        res = [n, n]
        for i in range(n):
            citiesReachable = sum(j <= distanceThreshold for j in dist[i])
            if citiesReachable <= res[1]:
                res = [i, citiesReachable]

        return res[0]


assert (
    Solution().findTheCity(
        n=4, edges=[[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], distanceThreshold=4
    )
    == 3
)
