#
# @lc app=leetcode id=1590 lang=python3
#
# [1590] Make Sum Divisible by P
#

# @lc code=start
from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        modDict = {0: -1}
        n = len(nums)
        curr = 0
        res = n

        target = sum(nums) % p
        if not target:
            return 0

        for i, num in enumerate(nums):
            curr += num
            curr %= p
            key = (curr - target + p) % p
            if key in modDict:
                res = min(res, i - modDict[key])
            modDict[curr] = i

        return -1 if res == n else res


# @lc code=end
assert Solution().minSubarray(nums=[3, 1, 4, 2], p=6) == 1
