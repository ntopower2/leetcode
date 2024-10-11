#
# @lc app=leetcode id=1942 lang=python3
#
# [1942] The Number of the Smallest Unoccupied Chair
#

# @lc code=start
from typing import List
from heapq import heappop, heappush


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        target = times[targetFriend][0]
        times.sort()
        chairsAvailable = list(range(len(times)))
        chairsTaken = []

        for arrival, leave in times:
            while chairsTaken and chairsTaken[0][0] <= arrival:
                _, chair = heappop(chairsTaken)
                heappush(chairsAvailable, chair)

            chair = heappop(chairsAvailable)
            if arrival == target:
                return chair

            heappush(chairsTaken, (leave, chair))

        return -1


# @lc code=end
assert Solution().smallestChair([[3, 10], [1, 5], [2, 6]], 0) == 2
