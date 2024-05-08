import heapq
from typing import List


class Pair:
    def __init__(self, x, y):
        self.index = x
        self.value = y

    # Override the less-than operator __lt__ to make Pair class work with max heap
    def __lt__(self, other):
        return self.value > other.value

    def __repr__(self):
        return f"({self.index}, {self.value})"


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        d = []
        for i, val in enumerate(score):
            d.append(Pair(i, val))
        heapq.heapify(d)
        i = 0
        while d:
            p = heapq.heappop(d)
            if i == 0:
                score[p.index] = "Gold Medal"
            elif i == 1:
                score[p.index] = "Silver Medal"
            elif i == 2:
                score[p.index] = "Bronze Medal"
            else:
                score[p.index] = str(i + 1)
            i += 1
        return score


assert Solution().findRelativeRanks([10, 3, 8, 9, 4]) == [
    "Gold Medal",
    "5",
    "Bronze Medal",
    "Silver Medal",
    "4",
]
