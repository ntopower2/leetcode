#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#

# @lc code=start
from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = sorted(
            map(str, nums),
            key=cmp_to_key(lambda n1, n2: -1 if n1 + n2 > n2 + n1 else 1),
        )
        if nums[0] == "0":
            return "0"
        return "".join(nums)


# @lc code=end

assert Solution().largestNumber([0, 0]) == "0"
assert Solution().largestNumber([3, 30, 34, 5, 9]) == "9534330"
