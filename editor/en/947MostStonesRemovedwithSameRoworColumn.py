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
    def removeStones(self, stones: List[List[int]]) -> int:
        rows = {}
        cols = {}
        n = len(stones)
        uf = UnionFind(n)

        for i, (x, y) in enumerate(stones):
            if x not in rows:
                rows[x] = i
            else:
                uf.union(i, rows[x])

            if y not in cols:
                cols[y] = i
            else:
                uf.union(i, cols[y])

        return len(stones) - uf.connectedComponents


assert Solution().removeStones([[0, 1], [1, 0], [1, 1]]) == 2
assert Solution().removeStones([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]) == 5
