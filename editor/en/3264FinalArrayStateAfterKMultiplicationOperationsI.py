#
# @lc app=leetcode id=3264 lang=python3
#
# [3264] Final Array State After K Multiplication Operations I
#

# @lc code=start
from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        nums = [(num, i) for i, num in enumerate(nums)]
        res = [0] * len(nums)
        heapify(nums)
        for _ in range(k):
            num, i = heappop(nums)
            num *= multiplier
            heappush(nums, (num, i))

        for num, i in nums:
            res[i] = num

        return res


# @lc code=end

assert Solution().getFinalState([2, 1, 3, 5, 6], 5, 2) == [8, 4, 6, 5, 6]
