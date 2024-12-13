#
# @lc app=leetcode id=2593 lang=python3
#
# [2593] Find Score of an Array After Marking All Elements
#

# @lc code=start
from typing import List
from heapq import heapify, heappop


class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [(num, i) for i, num in enumerate(nums)]
        heapify(nums)
        marked = [0] * n
        score = 0

        while nums:
            tmp, i = heappop(nums)
            if marked[i]:
                continue
            score += tmp
            marked[i] = 1
            if i > 0:
                marked[i - 1] = 1
            if i < n - 1:
                marked[i + 1] = 1

        return score


# @lc code=end

assert (
    Solution().findScore(
        [10, 44, 10, 8, 48, 30, 17, 38, 41, 27, 16, 33, 45, 45, 34, 30, 22, 3, 42, 42]
    )
    == 212
)
