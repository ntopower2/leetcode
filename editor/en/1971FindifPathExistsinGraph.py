from typing import List


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        graph = {i: [] for i in range(n)}
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        visited = set()

        def dfs(s):
            if s == destination:
                return True
            visited.add(s)
            for node in graph[s]:
                if node not in visited:
                    if dfs(node):
                        return True
            return False

        return dfs(source)


print(
    Solution().validPath(
        10,
        [
            [4, 3],
            [1, 4],
            [4, 8],
            [1, 7],
            [6, 4],
            [4, 2],
            [7, 4],
            [4, 0],
            [0, 9],
            [5, 4],
        ],
        5,
        9,
    )
)
