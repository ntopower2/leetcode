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
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        ufAlice = UnionFind(n)
        ufBob = UnionFind(n)
        removableEdges = 0
        for edgeType, u, v in edges:
            u -= 1
            v -= 1
            if edgeType == 3:
                # add to UF for both and mark for removal if uv does not connect
                if not ufAlice.union(u, v) or not ufBob.union(u, v):
                    removableEdges += 1
        for edgeType, u, v in edges:
            u -= 1
            v -= 1
            if edgeType == 1:
                if not ufAlice.union(u, v):
                    removableEdges += 1
            elif edgeType == 2:
                if not ufBob.union(u, v):
                    removableEdges += 1

        return (
            -1
            if ufAlice.connectedComponents * ufBob.connectedComponents > 1
            else removableEdges
        )


assert (
    Solution().maxNumEdgesToRemove(
        4, [[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]
    )
    == 2
)
