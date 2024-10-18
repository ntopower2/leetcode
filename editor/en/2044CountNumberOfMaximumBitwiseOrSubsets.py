#
# @lc app=leetcode id=2044 lang=python3
#
# [2044] Count Number of Maximum Bitwise-OR Subsets
#

# @lc code=start
from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        res = m = 0
        for num in nums:
            m |= num

        def dfs(i, val):
            nonlocal res
            if i == len(nums):
                if val == m:
                    res += 1
                return
            dfs(i + 1, val | nums[i])
            dfs(i + 1, val)
            return

        dfs(0, 0)
        return res


# @lc code=end

assert Solution().countMaxOrSubsets([3, 2, 1, 5]) == 6
