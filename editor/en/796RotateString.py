#
# @lc app=leetcode id=796 lang=python3
#
# [796] Rotate String
#


# @lc code=start
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        indexes = [i for i, c in enumerate(s) if c == goal[0]]
        if not indexes or len(indexes) == 0:
            return False
        res = []
        for index in indexes:
            i = 0
            j = index
            times = 0
            res.append(True)
            while times < len(s):
                j += 1
                j %= len(s)
                i += 1
                i %= len(s)
                if s[j] != goal[i]:
                    res[-1] = False
                    break
                times += 1

        return any(res)


# @lc code=end

assert Solution().rotateString("defdefdefabcabc", "defdefabcabcdef") == True
