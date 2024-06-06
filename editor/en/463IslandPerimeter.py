from typing import List, Tuple


class Solution(object):
    def islandPerimeter(self, grid: List[List[str]]) -> int:
        ret = 0
        nrows = len(grid)
        ncols = len(grid[0])
        for i in range(nrows):
            ret += sum(grid[i]) * 4
            for j in range(ncols):
                if grid[i][j] == 1:
                    if j + 1 < ncols and grid[i][j + 1] == 1:
                        ret -= 2
                    if i + 1 < nrows and grid[i + 1][j] == 1:
                        ret -= 2
        return ret


grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
print(Solution().islandPerimeter(grid))
