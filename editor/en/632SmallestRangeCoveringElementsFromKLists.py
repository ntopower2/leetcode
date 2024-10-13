#
# @lc app=leetcode id=632 lang=python3
#
# [632] Smallest Range Covering Elements from K Lists
#

# @lc code=start
from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        smallest = []
        largestNum = -float("inf")
        currentRange = [-float("inf"), float("inf")]

        for i in range(len(nums)):
            smallest.append((nums[i][0], i, 0))
            largestNum = max(largestNum, nums[i][0])
        heapify(smallest)

        while smallest:
            num, lstIndex, numIndex = heappop(smallest)
            if largestNum - num < currentRange[1] - currentRange[0]:
                currentRange = [num, largestNum]

            if len(nums[lstIndex]) == numIndex + 1:
                break

            nxt = nums[lstIndex][numIndex + 1]
            heappush(smallest, (nxt, lstIndex, numIndex + 1))
            largestNum = max(largestNum, nxt)
        return currentRange


# @lc code=end
