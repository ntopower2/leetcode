from typing import List
from heapq import heapify, heappop, heappush, heappushpop


class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        if max(worker) < min(difficulty):
            return 0
        worker.sort()
        res = 0

        canDoMaxProfit = []
        cannotDoMinDif = []
        for d, p in zip(difficulty, profit):
            if d <= worker[0]:
                heappush(canDoMaxProfit, (-p, d))
            else:
                heappush(cannotDoMinDif, (d, p))

        prof, _ = None, None
        for w in worker:
            while cannotDoMinDif and cannotDoMinDif[0][0] <= w:
                d, p = heappop(cannotDoMinDif)
                heappush(canDoMaxProfit, (-p, d))
            if not canDoMaxProfit:
                if prof:
                    res += prof
                continue
            if not prof or -canDoMaxProfit[0][0] > prof:
                prof, _ = heappop(canDoMaxProfit)
                prof = -prof
            res += prof
        return res


assert Solution().maxProfitAssignment([10, 55, 60], [46, 57, 96], [97, 31, 49]) == 188
assert (
    Solution().maxProfitAssignment([2, 4, 6, 8, 10], [10, 20, 30, 40, 50], [4, 5, 6, 7])
    == 100
)
