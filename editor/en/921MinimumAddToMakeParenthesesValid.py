#
# @lc app=leetcode id=921 lang=python3
#
# [921] Minimum Add to Make Parentheses Valid
#


# @lc code=start
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        res = 0
        for c in s:
            if c == ")":
                if not stack or stack[-1] == ")":
                    res += 1
                else:
                    stack.pop()
            else:
                stack.append(c)
        return len(stack) + res


# @lc code=end

assert Solution().minAddToMakeValid(")()") == 1
