#
# @lc app=leetcode id=1405 lang=python3
#
# [1405] Longest Happy String
#


# @lc code=start
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        letters = [[a, "a"], [b, "b"], [c, "c"]]
        res = []
        while True:
            letters.sort()
            if not letters[-1][0]:
                break
            elif (
                len(res) <= 1 or res[-1] != letters[-1][1] or res[-2] != letters[-1][1]
            ):
                res.append(letters[-1][1])
                letters[-1][0] -= 1
            elif letters[-2][0]:
                res.append(letters[-2][1])
                letters[-2][0] -= 1
            else:
                break

        return "".join(res)


# @lc code=end

assert Solution().longestDiverseString(2, 2, 1) == "aabbc"
