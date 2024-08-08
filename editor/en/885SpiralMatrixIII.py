from typing import List


class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:
        def isInBounds(i, j) -> bool:
            return 0 <= i < rows and 0 <= j < cols

        step = 1
        res = [[rStart, cStart]]
        while len(res) < rows * cols:
            for mr, mc, ms in (
                (0, 1, step),
                (1, 0, step),
                (0, -1, step + 1),
                (-1, 0, step + 1),
            ):
                for _ in range(ms):
                    rStart += mr
                    cStart += mc
                    if isInBounds(rStart, cStart):
                        res.append([rStart, cStart])
            step += 2
        return res


assert Solution().spiralMatrixIII(rows=5, cols=6, rStart=1, cStart=4) == [
    [1, 4],
    [1, 5],
    [2, 5],
    [2, 4],
    [2, 3],
    [1, 3],
    [0, 3],
    [0, 4],
    [0, 5],
    [3, 5],
    [3, 4],
    [3, 3],
    [3, 2],
    [2, 2],
    [1, 2],
    [0, 2],
    [4, 5],
    [4, 4],
    [4, 3],
    [4, 2],
    [4, 1],
    [3, 1],
    [2, 1],
    [1, 1],
    [0, 1],
    [4, 0],
    [3, 0],
    [2, 0],
    [1, 0],
    [0, 0],
]
