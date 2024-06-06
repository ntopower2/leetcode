from typing import List
from heapq import heapify, heappop, heappush, heapreplace


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        if len(arr) == 2:
            return arr
        if k == 1:
            return [arr[0], arr[-1]]

        fracHeap = [(arr[0] / val, 0, i + 1) for i, val in enumerate(arr[1:])]
        heapify(fracHeap)

        for _ in range(k - 1):
            _, nom, denom = fracHeap[0]
            if nom + 1 < denom:
                heapreplace(fracHeap, (arr[nom + 1] / arr[denom], nom + 1, denom))
            else:
                heappop(fracHeap)

        return [arr[fracHeap[0][1]], arr[fracHeap[0][2]]]


assert Solution().kthSmallestPrimeFraction([1, 2, 3, 5], 3) == [2, 5]
assert Solution().kthSmallestPrimeFraction([1, 7], 1) == [1, 7]
assert Solution().kthSmallestPrimeFraction([1, 29, 47], 1) == [1, 47]
