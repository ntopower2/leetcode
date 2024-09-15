#
# @lc app=leetcode id=1371 lang=python3
#
# [1371] Find the Longest Substring Containing Vowels in Even Counts
#


# @lc code=start
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        def getIndexFrom(ltr: str):
            if ltr == "a":
                return 0
            elif ltr == "e":
                return 1
            elif ltr == "i":
                return 2
            elif ltr == "o":
                return 3
            elif ltr == "u":
                return 4
            return -1

        mask = res = 0
        pos = {0: -1}

        for i, ltr in enumerate(s):
            t = getIndexFrom(ltr)
            if t != -1:
                mask ^= 1 << t
            if mask not in pos:
                pos[mask] = i
            else:
                res = max(res, i - pos[mask])

        return res


# @lc code=end
assert Solution().findTheLongestSubstring("leetcodeisgreat") == 5
