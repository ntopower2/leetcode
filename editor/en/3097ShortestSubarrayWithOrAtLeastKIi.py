#
# @lc app=leetcode id=3097 lang=python3
#
# [3097] Shortest Subarray With OR at Least K II
#

# @lc code=start
from typing import List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if nums[0] >= k:
            return 1
        NUM_SIZE = 32
        bitCounts = [0] * NUM_SIZE
        res = None
        left = 0

        def addToCount(num: int) -> None:
            i = 0
            while num:
                bitCounts[i] += num & 1
                num >>= 1
                i += 1

        def removeFromCount(num: int) -> None:
            i = 0
            while num:
                bitCounts[i] -= num & 1
                num >>= 1
                i += 1

        def isGeqThanK():
            tmp = 0
            for i in range(NUM_SIZE):
                if bitCounts[i]:
                    tmp |= 1 << i
                if tmp >= k:
                    return True
            return False

        for right in range(len(nums)):
            addToCount(nums[right])
            while isGeqThanK() and left <= right:
                if not res:
                    res = right - left + 1
                else:
                    res = min(res, right - left + 1)
                removeFromCount(nums[left])
                left += 1

        return res if res else -1


# @lc code=end

assert Solution().minimumSubarrayLength([2, 1, 8], 10) == 3
