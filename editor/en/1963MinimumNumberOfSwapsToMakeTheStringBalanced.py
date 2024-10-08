#
# @lc app=leetcode id=1963 lang=python3
#
# [1963] Minimum Number of Swaps to Make the String Balanced
#


# @lc code=start
class Solution:
    def minSwaps(self, s: str) -> int:
        unpaired = 0
        for c in s:
            if c == "[":
                unpaired += 1
            elif unpaired:
                unpaired -= 1
        return (unpaired + 1) >> 1


# @lc code=end

assert Solution().minSwaps("]]][[[") == 2
