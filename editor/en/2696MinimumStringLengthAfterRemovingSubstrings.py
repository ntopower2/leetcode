#
# @lc app=leetcode id=2696 lang=python3
#
# [2696] Minimum String Length After Removing Substrings
#


# @lc code=start
class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        removables = {"B": "A", "D": "C"}
        for c in s:
            if not stack:
                stack.append(c)
            elif c in removables and removables[c] == stack[-1]:
                stack.pop()
            else:
                stack.append(c)

        return len(stack)


# @lc code=end

assert Solution().minLength("ACBBD") == 5
