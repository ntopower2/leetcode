from collections import deque
from typing import List


class Solution:
    def buildMatrix(
        self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]
    ) -> List[List[int]]:

        def processConditions(arr: List[List[int]]) -> List[int]:
            ordering = []
            neighbors = [[] for _ in range(k)]
            inDeg = [0] * k

            for x, y in arr:
                neighbors[y - 1].append(x - 1)
                inDeg[x - 1] += 1

            queueCol = deque([v for v in range(k) if not inDeg[v]])

            while queueCol:
                x = queueCol.popleft()
                ordering.append(x)
                for node in neighbors[x]:
                    inDeg[node] -= 1
                    if not inDeg[node]:
                        queueCol.append(node)

            return ordering

        rowConditions = processConditions(rowConditions)
        colConditions = processConditions(colConditions)

        if len(rowConditions) != k or len(colConditions) != k:
            return []

        positions = [[0, 0] for _ in range(k)]

        for i, pos in enumerate(rowConditions):
            positions[pos][0] = k - i - 1

        for i, pos in enumerate(colConditions):
            positions[pos][1] = k - i - 1

        matrix = [[0 for _ in range(k)] for _ in range(k)]

        for idx, (row, col) in enumerate(positions):
            matrix[row][col] = idx + 1

        return matrix


assert Solution().buildMatrix(
    k=3, rowConditions=[[1, 2], [3, 2]], colConditions=[[2, 1], [3, 2]]
) == [[3, 0, 0], [0, 0, 1], [0, 2, 0]]
