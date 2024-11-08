#
# @lc app=leetcode id=1829 lang=python3
#
# [1829] Maximum XOR for Each Query
#

# @lc code=start
from typing import List


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        cumXor = [nums[0]] * len(nums)
        for i, num in enumerate(nums[1:], 1):
            cumXor[i] = cumXor[i - 1] ^ num

        m = (1 << maximumBit) - 1
        cumXor.reverse()
        for i in range(len(cumXor)):
            cumXor[i] ^= m

        return cumXor


# @lc code=end

assert Solution().getMaximumXor([0, 1, 1, 3], 2) == [0, 3, 2, 3]
