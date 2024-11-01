#
# @lc app=leetcode id=1957 lang=python3
#
# [1957] Delete Characters to Make Fancy String
#


# @lc code=start
class Solution:
    def makeFancyString(self, s: str) -> str:
        count = 1
        res = [s[0]]
        for c in s[1:]:
            if res[-1] == c:
                count += 1
                if count < 3:
                    res.append(c)
            else:
                res.append(c)
                count = 1

        return "".join(res)


# @lc code=end

assert Solution().makeFancyString("aaabaaaa") == "aabaa"
