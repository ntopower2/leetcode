#
# @lc app=leetcode id=1652 lang=python3
#
# [1652] Defuse the Bomb
#

# @lc code=start
from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        if k < 0:
            code.reverse()
            res = self.decrypt(code, -k)
            res.reverse()
            return res
        runningSum = sum(code[1 : k + 1])
        res = [0] * n
        for i in range(n):
            res[i] = runningSum
            runningSum -= code[(i + 1) % n]
            runningSum += code[(k + i + 1) % n]

        return res


# @lc code=end
assert Solution().decrypt([3, 9, 4, 2], 2) == [13, 6, 5, 12]
assert Solution().decrypt([2, 4, 9, 3], -2) == [12, 5, 6, 13]
assert Solution().decrypt([5, 7, 1, 4], 3) == [12, 10, 16, 13]
