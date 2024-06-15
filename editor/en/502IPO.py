from typing import List
from heapq import heapify, heappop, heappush


class Investment:
    def __init__(self, capital, profit) -> None:
        self.cap = capital
        self.prof = profit
        self.isUsed = False

    def use(self):
        self.isUsed = True


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        affordable = []
        notYetAffordable = []
        for prof, cap in zip(profits, capital):
            if cap <= w:
                affordable.append((-prof, cap))
            else:
                notYetAffordable.append((cap, prof))
        heapify(affordable)
        heapify(notYetAffordable)
        if not affordable:
            return w
        while k and affordable:
            tmp = heappop(affordable)
            w -= tmp[0]
            while notYetAffordable and w >= notYetAffordable[0][0]:
                tmp = heappop(notYetAffordable)
                heappush(affordable, (-tmp[1], tmp[0]))
            k -= 1
        return w


assert Solution().findMaximizedCapital(2, 0, [1, 3, 2], [0, 1, 1]) == 4
assert Solution().findMaximizedCapital(1, 0, [1, 2, 3], [1, 1, 2]) == 0
