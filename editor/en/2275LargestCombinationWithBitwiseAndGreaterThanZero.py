#
# @lc app=leetcode id=2275 lang=python3
#
# [2275] Largest Combination With Bitwise AND Greater Than Zero
#

# @lc code=start
from typing import List


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        res = [0] * 31
        for canditate in candidates:
            for i, bit in enumerate(reversed(bin(canditate)[2:])):
                if bit == "1":
                    res[i] += 1

        return max(res)


# @lc code=end

assert Solution().largestCombination([16, 17, 71, 62, 12, 24, 14]) == 4
