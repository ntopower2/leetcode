from enum import Enum
from typing import List


class UnionFind:
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = list(range(n))
        self.connectedComponents = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            self.connectedComponents -= 1
            return True
        return False


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        direction = Enum("Direction", ["UP", "RIGHT", "DOWN", "LEFT"], start=0)
        n, parts = len(grid), len(direction)
        uf = UnionFind(n * n * parts)

        for i in range(n):
            for j in range(n):
                currentIndex = parts * (i * n + j)
                # handling of down and/or right neighbors
                if i < n - 1:
                    uf.union(
                        currentIndex + direction.DOWN.value,
                        currentIndex + parts * n + direction.UP.value,
                    )
                if j < n - 1:
                    uf.union(
                        currentIndex + direction.RIGHT.value,
                        currentIndex + parts + direction.LEFT.value,
                    )
                # handling of cell unions
                if grid[i][j] in ("/", " "):
                    uf.union(
                        currentIndex + direction.UP.value,
                        currentIndex + direction.LEFT.value,
                    )
                    uf.union(
                        currentIndex + direction.RIGHT.value,
                        currentIndex + direction.DOWN.value,
                    )
                elif grid[i][j] in ("\\", " "):
                    uf.union(
                        currentIndex + direction.UP.value,
                        currentIndex + direction.RIGHT.value,
                    )
                    uf.union(
                        currentIndex + direction.LEFT.value,
                        currentIndex + direction.DOWN.value,
                    )
                if grid[i][j] == " ":
                    uf.union(
                        currentIndex + direction.UP.value,
                        currentIndex + direction.DOWN.value,
                    )

        return uf.connectedComponents


assert Solution().regionsBySlashes(["/\\", "\\/"]) == 5
