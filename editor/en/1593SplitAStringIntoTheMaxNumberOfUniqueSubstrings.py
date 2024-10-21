#
# @lc app=leetcode id=1593 lang=python3
#
# [1593] Split a String Into the Max Number of Unique Substrings
#


# @lc code=start
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        res = 0
        seen = set()

        def dfs(i, unq):
            nonlocal res
            if i >= len(s):
                res = max(res, unq)
                return
            for j in range(i + 1, len(s) + 1):
                tmp = s[i:j]
                if tmp not in seen:
                    seen.add(tmp)
                    dfs(j, unq + 1)
                    seen.remove(tmp)

        dfs(0, 0)
        return res


# @lc code=end

assert Solution().maxUniqueSplit("ababccc") == 5
