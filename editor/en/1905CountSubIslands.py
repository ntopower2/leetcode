from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        islands = 0
        rows = len(grid2)
        cols = len(grid2[0])

        def dfs(row, col):
            if not 0 <= row < rows or not 0 <= col < cols or not grid2[row][col]:
                return True

            grid2[row][col] = 0
            existsInOther = grid1[row][col] == 1

            existsInOther &= dfs(row + 1, col)
            existsInOther &= dfs(row - 1, col)
            existsInOther &= dfs(row, col + 1)
            existsInOther &= dfs(row, col - 1)

            return existsInOther

        for i in range(rows):
            for j in range(cols):
                if grid2[i][j]:
                    if dfs(i, j):
                        islands += 1

        return islands


assert (
    Solution().countSubIslands(
        grid1=[
            [1, 1, 1, 0, 0],
            [0, 1, 1, 1, 1],
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 1, 0, 1, 1],
        ],
        grid2=[
            [1, 1, 1, 0, 0],
            [0, 0, 1, 1, 1],
            [0, 1, 0, 0, 0],
            [1, 0, 1, 1, 0],
            [0, 1, 0, 1, 0],
        ],
    )
    == 3
)
