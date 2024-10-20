#
# @lc app=leetcode id=1106 lang=python3
#
# [1106] Parsing A Boolean Expression
#


# @lc code=start
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        for c in expression:
            if c == ")":
                seen = set()
                while stack[-1] != "(":
                    seen.add(stack.pop())
                stack.pop()

                operator = stack.pop()

                if operator == "&":
                    stack.append("t" if all(x == "t" for x in seen) else "f")
                elif operator == "|":
                    stack.append("t" if any(x == "t" for x in seen) else "f")
                elif operator == "!":
                    stack.append("t" if "f" in seen else "f")
            elif c != ",":
                stack.append(c)

        return stack.pop() == "t"


# @lc code=end

assert Solution().parseBoolExpr("|(f,f,f,t)") == True
