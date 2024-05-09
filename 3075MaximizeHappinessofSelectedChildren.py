from typing import List
import heapq


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness = [-h for h in happiness]
        heapq.heapify(happiness)
        res = i = 0
        while happiness and happiness[0] + i < 0 and i < k:
            res -= heapq.heappop(happiness) + i
            i += 1
        return res


assert Solution().maximumHappinessSum([7, 50, 3], 3) == 57
assert Solution().maximumHappinessSum([2, 3, 4, 5], 1) == 5
assert Solution().maximumHappinessSum([1, 1, 1, 1], 2) == 1
