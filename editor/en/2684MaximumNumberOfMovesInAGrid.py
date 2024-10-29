#
# @lc app=leetcode id=2684 lang=python3
#
# [2684] Maximum Number of Moves in a Grid
#

# @lc code=start
from typing import List
from collections import deque


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dist = [[0] * m for _ in range(n)]
        directions = ((-1, 1), (0, 1), (1, 1))
        queue = deque((i, 0) for i in range(n))
        maxDist = 0

        while queue:
            (i, j) = queue.popleft()
            for direction in directions:
                newRow, newCol = i + direction[0], j + direction[1]
                if (
                    0 <= newRow < n
                    and 0 <= newCol < m
                    and grid[i][j] < grid[newRow][newCol]
                    and dist[newRow][newCol] < dist[i][j] + 1
                ):
                    dist[newRow][newCol] = max(dist[newRow][newCol], dist[i][j] + 1)
                    queue.append((newRow, newCol))
                    maxDist = max(maxDist, dist[newRow][newCol])

        return maxDist


# @lc code=end
assert (
    Solution().maxMoves([[2, 4, 3, 5], [5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]])
    == 3
)
assert Solution().maxMoves([[3, 2, 4], [2, 1, 9], [1, 1, 7]]) == 0
