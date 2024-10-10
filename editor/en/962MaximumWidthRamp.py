#
# @lc app=leetcode id=962 lang=python3
#
# [962] Maximum Width Ramp
#

# @lc code=start
from typing import List


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        res = 0
        for i, num in enumerate(nums):
            if not stack or nums[stack[-1]] > num:
                stack.append(i)

        for i in range(len(nums) - 1, -1, -1):
            if not stack:
                break

            while stack and nums[stack[-1]] <= nums[i]:
                res = max(res, i - stack.pop())
        return res


# @lc code=end

assert Solution().maxWidthRamp([1, 1, 1]) == 2
assert Solution().maxWidthRamp([9, 8, 1, 0, 1, 9, 4, 0, 4, 1]) == 7
