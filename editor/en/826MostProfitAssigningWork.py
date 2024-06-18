from typing import List
from heapq import heapify, heappop, heappush, heappushpop


class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        if max(worker) < min(difficulty):
            return 0
        worker.sort()
        jobs = sorted(zip(difficulty, profit))

        i = curProfit = res = 0
        for w in worker:
            while i < len(jobs) and jobs[i][0] <= w:
                curProfit = max(curProfit, jobs[i][1])
                i += 1
            res += curProfit

        return res


assert (
    Solution().maxProfitAssignment([2, 4, 6, 8, 10], [10, 20, 30, 40, 50], [4, 5, 6, 7])
    == 100
)
assert Solution().maxProfitAssignment([10, 55, 60], [46, 57, 96], [97, 31, 49]) == 188
