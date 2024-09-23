#
# @lc app=leetcode id=2707 lang=python3
#
# [2707] Extra Characters in a String
#

from typing import List


# @lc code=start
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        words = set(dictionary)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1
            for j in range(i):
                if s[j:i] in words and dp[j] < dp[i]:
                    dp[i] = dp[j]

        return dp[n]


# @lc code=end

assert (
    Solution().minExtraChar(s="sayhelloworld", dictionary=["hello", "world", "hel"])
    == 3
)
