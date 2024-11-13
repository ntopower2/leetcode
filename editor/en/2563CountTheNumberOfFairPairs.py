#
# @lc app=leetcode id=2563 lang=python3
#
# [2563] Count the Number of Fair Pairs
#

# @lc code=start
from typing import List
from bisect import bisect_left


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        res = 0

        for i, num in enumerate(nums):
            s = bisect_left(nums, lower - num, lo=i + 1)
            t = bisect_left(nums, upper - num + 1, lo=i + 1)
            res += t - s

        return res


# @lc code=end

assert Solution().countFairPairs([0, 1, 7, 4, 4, 5], 3, 6) == 6
