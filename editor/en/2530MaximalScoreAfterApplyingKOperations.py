#
# @lc app=leetcode id=2530 lang=python3
#
# [2530] Maximal Score After Applying K Operations
#

# @lc code=start
from typing import List
from heapq import heapify, heapreplace
from math import ceil


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        largest = [-num for num in nums]
        heapify(largest)
        tmp = largest[0]
        score = 0
        while k and -tmp:
            tmp = largest[0]
            score += -heapreplace(largest, -ceil(-tmp / 3))
            k -= 1

        return score


# @lc code=end


assert Solution().maxKelements([1, 10, 3, 3, 3], 3) == 17
