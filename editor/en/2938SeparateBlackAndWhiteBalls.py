#
# @lc app=leetcode id=2938 lang=python3
#
# [2938] Separate Black and White Balls
#


# @lc code=start
class Solution:
    def minimumSteps(self, s: str) -> int:
        zeros = s.count("0")
        if not zeros or zeros == len(s):
            return 0
        res = i = 0
        j = len(s) - 1
        while i < zeros and i < j:
            if s[i] == "0":
                i += 1
            elif s[j] == "1":
                j -= 1
            else:
                res += j - i
                i += 1
                j -= 1
        return res


# @lc code=end

assert Solution().minimumSteps("0111") == 0
