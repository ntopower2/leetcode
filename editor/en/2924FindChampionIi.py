#
# @lc app=leetcode id=2924 lang=python3
#
# [2924] Find Champion II
#

# @lc code=start
from typing import List


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        strongestTeams = [1] * n
        for u, v in edges:
            strongestTeams[v] = 0

        return -1 if strongestTeams.count(1) > 1 else strongestTeams.index(1)


# @lc code=end

assert Solution().findChampion(4, [[0, 2], [1, 3], [1, 2]]) == -1
