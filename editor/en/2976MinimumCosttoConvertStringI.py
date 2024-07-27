from typing import List


class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:

        def convertCharToNum(c):
            return ord(c) - ord("a")

        res = 0

        weights = [[float("inf")] * 26 for _ in range(26)]
        for u, v, w in zip(
            map(convertCharToNum, original), map(convertCharToNum, changed), cost
        ):
            weights[u][v] = min(weights[u][v], w)
            weights[u][u] = 0
            weights[v][v] = 0

        for k in range(26):
            for i in range(26):
                for j in range(26):
                    weights[i][j] = min(
                        weights[i][j],
                        weights[i][k] + weights[k][j],
                    )
        for u, v in zip(map(convertCharToNum, source), map(convertCharToNum, target)):
            if weights[u][v] == float("inf"):
                return -1
            res += weights[u][v]

        return res


assert (
    Solution().minimumCost(
        source="bcaabaddac",
        target="bdccbdaadc",
        original=["c", "d", "a", "a", "c", "a", "d"],
        changed=["a", "a", "d", "b", "d", "c", "c"],
        cost=[4, 3, 6, 3, 11, 6, 4],
    )
    == 40
)
assert (
    Solution().minimumCost(
        source="abcd",
        target="acbe",
        original=["a", "b", "c", "c", "e", "d"],
        changed=["b", "c", "b", "e", "b", "e"],
        cost=[2, 5, 5, 1, 2, 20],
    )
    == 28
)
