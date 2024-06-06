from heapq import heappop, heappush
from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        graph = {}
        n = len(grid)
        for i in range(n - 1):
            for j in range(n):
                graph[str(i) + str(j)] = {
                    str(i + 1) + str(k): grid[i + 1][k] for k in range(n) if k != j
                }
        graph["0"] = {f"0{i}": grid[0][i] for i in range(n)}
        for i in range(n):
            graph[f"{n-1}{i}"] = {"1": 0}
        graph["1"] = {}

        def bellman_ford(graph, start, end):
            """
            Bellman-Ford algorithm to find the shortest path in a graph with negative weights.

            Args:
            graph: A dictionary representing the graph. Keys are nodes, values are dictionaries
                with outgoing neighbors as keys and edge weights as values.
            start: The starting node.
            end: The ending node.

            Returns:
            The cost of the shortest path from start to end, or float('inf') if no such path exists.
            """

            n = len(graph)
            distance = {node: float("inf") for node in graph}
            distance[start] = 0

            for _ in range(n - 1):
                for node, neighbors in graph.items():
                    for neighbor, weight in neighbors.items():
                        distance[neighbor] = min(
                            distance[neighbor], distance[node] + weight
                        )

            # Check for negative-weight cycles
            for node, neighbors in graph.items():
                for neighbor, weight in neighbors.items():
                    if distance[neighbor] > distance[node] + weight:
                        return float("inf")

            return distance[end]

        return bellman_ford(graph, "0", "1")


print(Solution().minFallingPathSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
