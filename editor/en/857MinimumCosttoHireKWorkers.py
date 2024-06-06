from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    def mincostToHireWorkers(
        self, quality: List[int], wage: List[int], k: int
    ) -> float:
        ratios = sorted([(w / q, q) for w, q in zip(wage, quality)])
        cost = None
        totalQuality = 0
        hq = []
        for r, q in ratios:
            heappush(hq, -q)
            totalQuality += q
            if len(hq) > k:
                totalQuality += heappop(hq)
            if len(hq) == k:
                cost = (
                    min(cost, totalQuality * r)
                    if cost is not None
                    else totalQuality * r
                )
        return cost


assert Solution().mincostToHireWorkers([10, 20, 5], [70, 50, 30], 2) == 105
