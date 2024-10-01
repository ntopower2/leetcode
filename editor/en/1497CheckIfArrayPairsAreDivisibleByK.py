#
# @lc app=leetcode id=1497 lang=python3
#
# [1497] Check If Array Pairs Are Divisible by k
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        rems = defaultdict(int)
        for num in arr:
            rems[num % k] += 1

        for rem in range(k + 1 // 2):
            if rems[(k - rem) % k] != rems[rem]:
                return False

        if rems[0] % 2:
            return False
        return True


# @lc code=end

assert Solution().canArrange([-1, -1, -1, -1, 2, 2, -2, -2], 3) == False
