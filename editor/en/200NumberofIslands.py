from typing import List, Tuple


class Solution(object):
    def numIslands(self, grid: List[List[str]]) -> int:
        nrows = len(grid)
        ncols = len(grid[0])
        islands = 0

        def dfs(row, col):
            if not 0 <= row < nrows or not 0 <= col < ncols or grid[row][col] == "0":
                return

            grid[row][col] = "0"

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == "1":
                    islands += 1
                    dfs(i, j)
        return islands


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]
print(Solution().numIslands(grid))
