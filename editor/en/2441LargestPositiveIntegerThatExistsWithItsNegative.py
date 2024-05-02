from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        res = None
        for n in nums:
            if (res is None or res < n) and -n in nums:
                res = abs(n)
        return res if res is not None else -1


print(Solution().findMaxK([-10, 8, 6, 7, -2, -3]))
