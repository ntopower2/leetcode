#
# @lc app=leetcode id=440 lang=python3
#
# [440] K-th Smallest in Lexicographical Order
#


# @lc code=start
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def skipSteps() -> int:
            steps = 0
            first = last = cur
            while first <= n:
                steps += min(last, n) - first + 1
                first *= 10
                last = last * 10 + 9
            return steps

        cur = 1
        k -= 1
        while k:
            steps = skipSteps()
            if steps <= k:
                cur += 1
                k -= steps
            else:
                cur *= 10
                k -= 1
        return cur


# @lc code=end

assert Solution().findKthNumber(13, 2) == 10
