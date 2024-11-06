#
# @lc app=leetcode id=3011 lang=python3
#
# [3011] Find if Array Can Be Sorted
#

# @lc code=start
from typing import List


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        digitsToMinMax = {}
        prev = None
        cur = None
        for num in nums:
            ones = bin(num).count("1")
            if not cur:
                prev = cur = ones

            if cur != ones:
                prev = cur
                cur = ones

            if prev != cur and digitsToMinMax[prev][1] > num:
                return False

            if ones not in digitsToMinMax:
                digitsToMinMax[ones] = [num, num]
            else:
                digitsToMinMax[ones][0] = min(digitsToMinMax[ones][0], num)
                digitsToMinMax[ones][1] = max(digitsToMinMax[ones][1], num)

        return True


# @lc code=end

assert Solution().canSortArray([3, 16, 8, 4, 2]) == False
