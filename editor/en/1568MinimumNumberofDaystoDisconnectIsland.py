from collections import defaultdict
from typing import List


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        parent = defaultdict(list)
        low = [0 for _ in range(m * n)]
        discovery = [0 for _ in range(m * n)]
        self.time = 0
        self.bridge = False

        def isInBounds(i, j) -> bool:
            return 0 <= i < m and 0 <= j < n

        def oneDimIndex(i, j) -> int:
            return i * n + j

        def dfs(i, j):
            children = 0
            visited.add(oneDimIndex(i, j))
            low[oneDimIndex(i, j)] = self.time
            discovery[oneDimIndex(i, j)] = self.time
            self.time += 1

            for x, y in [
                (i, j + 1),
                (i + 1, j),
                (i, j - 1),
                (i - 1, j),
            ]:
                if isInBounds(x, y) and grid[x][y]:
                    if oneDimIndex(x, y) not in visited:
                        parent[(x, y)] = (i, j)
                        children += 1
                        dfs(x, y)

                        low[oneDimIndex(i, j)] = min(
                            low[oneDimIndex(i, j)], low[oneDimIndex(x, y)]
                        )

                        # finding cut vertex using Tarjan
                        # either root with multiple children
                        # or not root and no back edge in its children
                        if (
                            not self.bridge
                            and (not parent[(i, j)] and children > 1)
                            or (
                                parent[(i, j)]
                                and low[oneDimIndex(x, y)]
                                >= discovery[oneDimIndex(i, j)]
                            )
                        ):
                            self.bridge = True
                    elif parent[(i, j)] != (x, y):
                        low[oneDimIndex(i, j)] = min(
                            low[oneDimIndex(i, j)], discovery[oneDimIndex(x, y)]
                        )

        # search for starting point
        i = j = 0
        while i < m and j < n and not grid[i][j]:
            j += 1
            if j == n:
                i += 1
                if i < m:
                    j = 0

        # no islands
        if i == m and j == n:
            return 0

        dfs(i, j)

        for r in range(i, m):
            for j in range(0, n):
                # existence of another island
                if grid[r][j] and oneDimIndex(r, j) not in visited:
                    return 0

        return 1 if self.bridge or len(visited) == 1 else 2


assert (
    Solution().minDays(
        [
            [0, 1, 1, 1, 1, 0, 1],
            [0, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 0, 1, 1],
            [0, 1, 1, 1, 1, 1, 1],
            [1, 0, 1, 1, 1, 1, 1],
        ]
    )
    == 0
)
assert (
    Solution().minDays(
        [[0, 1, 0, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 0]]
    )
    == 1
)
assert Solution().minDays([[0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]) == 1
