#
# @lc app=leetcode id=2064 lang=python3
#
# [2064] Minimized Maximum of Products Distributed to Any Store
#

# @lc code=start
from typing import List
from math import ceil


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        if n == len(quantities):
            return max(quantities)
        if len(quantities) == 1:
            d, m = divmod(quantities[0], n)
            if not m:
                return d
            return d + 1

        def canAllocate(size: int) -> bool:
            stores = 0
            for q in quantities:
                if stores > n:
                    return False
                d, m = divmod(q, size)
                stores += d if not m else d + 1

            return stores <= n

        s = ceil(sum(quantities) / n)
        t = max(quantities)
        while s < t:
            mid = s + t
            mid >>= 1
            if canAllocate(mid):
                t = mid
            else:
                s = mid + 1

        return s


# @lc code=end

assert Solution().minimizedMaximum(6, [11, 6]) == 3
assert (
    Solution().minimizedMaximum(22, [25, 11, 29, 6, 24, 4, 29, 18, 6, 13, 25, 30]) == 13
)
