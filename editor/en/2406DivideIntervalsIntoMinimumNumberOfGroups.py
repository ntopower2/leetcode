#
# @lc app=leetcode id=2406 lang=python3
#
# [2406] Divide Intervals Into Minimum Number of Groups
#

# @lc code=start
from typing import List
from heapq import heappop, heappush


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        endTimes = []
        intervals.sort()
        for s, t in intervals:
            if endTimes and endTimes[0] < s:
                heappop(endTimes)
            heappush(endTimes, t)
        return len(endTimes)


# @lc code=end

assert Solution().minGroups([[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]) == 3
