from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagic(si, sj) -> bool:
            if len(grid) < si + 3 or len(grid[si]) < sj + 3:
                return False
            nums = set(
                [grid[i][j] for i in range(si, si + 3) for j in range(sj, sj + 3)]
            )
            if len(nums) != 9 or max(nums) > 9 or min(nums) < 1:
                return False

            target = sum(grid[si][sj : sj + 3])
            if target != sum([grid[si + i][sj + i] for i in range(3)]):
                return False
            if target != sum([grid[si + i][sj + 2 - i] for i in range(3)]):
                return False
            if any(sum(row[sj : sj + 3]) != target for row in grid[si : si + 3]):
                return False
            if any(
                sum(grid[i][j] for i in range(si, si + 3)) != target
                for j in range(sj, sj + 3)
            ):
                return False

            return True

        counts = sum(
            isMagic(i, j) for i in range(len(grid) - 2) for j in range(len(grid[i]) - 2)
        )

        return counts


assert (
    Solution().numMagicSquaresInside(
        [
            [3, 10, 2, 3, 4],
            [4, 5, 6, 8, 1],
            [8, 8, 1, 6, 8],
            [1, 3, 5, 7, 1],
            [9, 4, 9, 2, 9],
        ]
    )
    == 1
)
assert Solution().numMagicSquaresInside([[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]) == 1
