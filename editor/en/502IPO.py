from typing import List
from heapq import heapify, heappop, heappush, nlargest


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        investments = [(cap, prof) for prof, cap in zip(profits, capital)]
        profitable = []
        heapify(investments)
        while k:
            while investments and w >= investments[0][0]:
                tmp = heappop(investments)
                heappush(profitable, (-tmp[1], tmp[0]))
            if not profitable:
                return w
            tmp = heappop(profitable)
            w -= tmp[0]
            k -= 1
        return w


assert Solution().findMaximizedCapital(2, 0, [1, 3, 2], [0, 1, 1]) == 4
assert Solution().findMaximizedCapital(1, 0, [1, 2, 3], [1, 1, 2]) == 0
