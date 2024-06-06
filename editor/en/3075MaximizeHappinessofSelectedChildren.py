from typing import List
import heapq


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        n = len(happiness)
        res = 0
        for i in range(k):
            if (happiness[i] - i) <= 0:
                return res
            res += happiness[i] - i
        return res


assert Solution().maximumHappinessSum([12, 1, 42], 3) == 53
assert Solution().maximumHappinessSum([2, 3, 4, 5], 1) == 5
assert Solution().maximumHappinessSum([1, 1, 1, 1], 2) == 1
